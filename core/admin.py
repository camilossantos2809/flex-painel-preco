from django.contrib import admin
from .models import (Produtos, Unidades, Screen, PromotionsProd)


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    pass


@admin.register(PromotionsProd)
class PromotionsProdAdmin(admin.ModelAdmin):
    pass


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('cod', 'cod_barra', 'descricao',
                    'descricao_comp', 'marca', 'dpto_cod', 'ncm')
    list_display_links = ('cod', 'descricao', 'cod_barra')
    search_fields = ('cod', 'descricao', 'descricao_comp',
                     'marca', 'cod_barra', 'ncm', 'dpto_cod')

    def get_readonly_fields(self, request, obj=None):
        # make all fields readonly
        readonly_fields = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        if 'is_submitted' in readonly_fields:
            readonly_fields.remove('is_submitted')
        return readonly_fields


@admin.register(Unidades)
class UnidadesAdmin(admin.ModelAdmin):
    list_display = ('cod', 'nome')

    def get_readonly_fields(self, request, obj=None):
        # make all fields readonly
        readonly_fields = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        if 'is_submitted' in readonly_fields:
            readonly_fields.remove('is_submitted')
        return readonly_fields
