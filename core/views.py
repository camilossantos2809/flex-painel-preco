from django.shortcuts import render
from django.contrib import messages
from .models import Screen, PromotionsProd, Produtos, Unidades


def index(request):
    screens = Screen.objects.all()
    return render(request, 'index.html', {'screens': screens})


def screen_promotion(request, screen):
    screen = Screen.objects.filter(cod=screen).get()
    promotions = PromotionsProd.objects \
        .filter(screen=screen, prod__prun__unid=screen.unid.cod)
    return render(request, 'promotion.html', {'promotions': promotions, 'screen': screen})


def add_promotion(request):
    if request.method == 'POST' and request.FILES['image']:
        prod_promo = PromotionsProd()
        prod_promo.image = request.FILES['image']
        prod_promo.prod = Produtos.objects.filter(
            cod=request.POST['produto']).get()
        prod_promo.screen = Screen.objects.get(cod=request.POST['screen'])
        prod_promo.save()
        messages.success(
            request, f'Novo produto {prod_promo.prod.cod} adicionado')
        return render(request, 'add_promotion.html')
    return render(request, 'add_promotion.html')


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
