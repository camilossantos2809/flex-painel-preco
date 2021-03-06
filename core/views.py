from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from .models import Produtos, PromotionsProd, Screen, Unidades


def index(request):
    screens = Screen.objects.all()
    return render(request, 'index.html', {'screens': screens})


def screen_promotion(request, screen):
    screen = Screen.objects.filter(cod=screen).get()
    promotions = PromotionsProd.objects \
        .filter(screen=screen, prod__prun__unid=screen.unid.cod,
                show_promotion=True, image__isnull=False)
    return render(request, 'screen_promotion.html', {'promotions': promotions, 'screen': screen})


def screen_prices_list(request, screen):
    screen = Screen.objects.filter(cod=screen).get()
    promotions = PromotionsProd.objects \
        .filter(screen=screen, prod__prun__unid=screen.unid.cod,
                show_list=True, prod__prun__preco__gt=0)
    return render(request, 'screen_prices_list.html', {'promotions': promotions, 'screen': screen})


def add_update_promotion(request, id=None):
    screens = Screen.objects.all()

    prod_promo = None
    if id:
        prod_promo = PromotionsProd.objects.get(id=id)

    if request.method == 'POST':
        if not id:
            prod_promo = PromotionsProd()
        if 'image' in request.FILES:
            prod_promo.image = request.FILES['image']
        prod_promo.prod = Produtos.objects.filter(
            cod=request.POST['produto']).get()
        prod_promo.screen = Screen.objects.get(cod=request.POST['screen'])

        if 'show-list' in request.POST:
            prod_promo.show_list = True
        else:
            prod_promo.show_list = False

        if 'show-promotion' in request.POST:
            prod_promo.show_promotion = True
        else:
            prod_promo.show_promotion = False

        prod_promo.save()
        messages.success(
            request, f'Produto {prod_promo.prod.cod} gravado')
        return render(request, 'add_promotion.html', {'promo': prod_promo, 'screens': screens})
    return render(request, 'add_promotion.html', {'promo': prod_promo, 'screens': screens})


def list_products(request):
    fields = [
        'cod', 'cod_barra', 'descricao', 'descricao_comp', 'marca',
        'dpto_cod', 'grupo_nome'
    ]

    filters = {}
    for field in fields:
        if request.GET.get(field):
            if field in ['cod', 'cod_barra']:
                filters[f'{field}'] = request.GET.get(field)
            else:
                filters[f'{field}__icontains'] = request.GET[field]

    products_list = Produtos.objects.filter(**filters).values(*fields)

    paginator = Paginator(products_list, 25)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return JsonResponse(list(products), safe=False)


def add_update_screen(request, id=None):
    screen = None
    unidades = Unidades.objects.all()
    if id:
        screen = Screen.objects.get(cod=id)

    if request.method == 'POST':
        if not id:
            screen = Screen()
        screen.unid = Unidades.objects.filter(cod=request.POST['unid']).get()
        screen.descricao = request.POST['desc']
        screen.seconds_promotion = request.POST['time-promotion']
        if 'image-promo' in request.FILES:
            screen.background = request.FILES['image-promo']
        if 'image-list' in request.FILES:
            screen.background_list = request.FILES['image-list']
        screen.save()
        messages.success(request, f"Screen {screen.cod}-{screen.descricao} gravado")
        return render(request, 'add_screen.html', {'unidades': unidades, 'screen': screen})
    return render(request, 'add_screen.html', {'unidades': unidades, 'screen': screen})


def list_promotions(request):
    promotions = PromotionsProd.objects.all()
    return render(request, 'list_promotions.html', {'promotions': promotions})


def delete_promotion(request, id):
    if request.method == 'POST':
        return JsonResponse(list(PromotionsProd.objects.filter(id=id).delete()), safe=False)


def delete_screen(request, id):
    return JsonResponse(list(Screen.objects.filter(id=id).delete()), safe=False)
