from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Screen, PromotionsProd, Produtos, Unidades


def index(request):
    screens = Screen.objects.all()
    return render(request, 'index.html', {'screens': screens})


def screen_promotion(request, screen):
    screen = Screen.objects.filter(cod=screen).get()
    promotions = PromotionsProd.objects \
        .filter(screen=screen, prod__prun__unid=screen.unid.cod)
    return render(request, 'promotion.html', {'promotions': promotions, 'screen': screen})


def add_promotion(request, id=None):
    prod_promo = None
    if id:
        prod_promo = PromotionsProd.objects.get(id=id)

    if request.method == 'POST' and request.FILES['image']:
        if not id:
            prod_promo = PromotionsProd()
        prod_promo.image = request.FILES['image']
        prod_promo.prod = Produtos.objects.filter(
            cod=request.POST['produto']).get()
        prod_promo.screen = Screen.objects.get(cod=request.POST['screen'])
        prod_promo.save()
        messages.success(
            request, f'Produto {prod_promo.prod.cod} gravado')
        return render(request, 'add_promotion.html', {'promo': prod_promo})
    return render(request, 'add_promotion.html', {'promo': prod_promo})


def list_products(request):
    products_list = Produtos.objects.values(
        'cod',  'cod_barra', 'descricao', 'descricao_comp', 'marca', 'dpto_cod',
        'grupo_nome'
    ).all()
    paginator = Paginator(products_list, 25)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return JsonResponse(list(products), safe=False)


def add_screen(request):
    unidades = Unidades.objects.all()
    if request.method == 'POST' and request.FILES['image']:
        screen = Screen()
        screen.unid = Unidades.objects.filter(cod=request.POST['unid']).get()
        screen.descricao = request.POST['desc']
        screen.minutes_reload_page = request.POST['reload-page']
        screen.seconds_promotion = request.POST['time-promotion']
        screen.background = request.FILES['image']
        screen.save()
        messages.success(request, f"Nova configuração de tela adicionada")
    return render(request, 'add_screen.html', {'unidades': unidades})


def list_promotions(request):
    promotions = PromotionsProd.objects.all()
    return render(request, 'list_promotions.html', {'promotions': promotions})
