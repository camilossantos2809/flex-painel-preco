from django.db import models


class Produtos(models.Model):
    cod = models.IntegerField(db_column="prod_codigo", primary_key=True)
    extra3_barras = models.CharField(db_column="prod_extra3", max_length=50)
    cod_caixa = models.CharField(db_column="prod_codcaixa", max_length=14)
    cod_barra = models.CharField(db_column="prod_codbarras", max_length=13)
    descricao = models.CharField(db_column="prod_descricao", max_length=40)
    descricao_comp = models.CharField(
        db_column="prod_complemento", max_length=40)
    descricao_pdv = models.CharField(db_column="prod_descrpdvs", max_length=40)
    grupo_nome = models.CharField(db_column="prod_grup_nome", max_length=40)
    dpto_cod = models.CharField(db_column="prod_dpto_codigo", max_length=3)
    emb = models.CharField(db_column="prod_emb", max_length=2)
    emb_qtd = models.IntegerField(db_column="prod_qemb")
    pesavel = models.CharField(db_column="prod_balanca", max_length=1)
    peso = models.DecimalField(
        db_column="prod_peso", max_digits=15, decimal_places=5)
    peso_liq = models.DecimalField(
        db_column="prod_pesoliq", max_digits=15, decimal_places=5)
    data_alt = models.DateField(db_column="prod_dataalt")
    data_cad = models.DateField(db_column="prod_datacad")
    ncm = models.CharField(db_column="prod_codigoncm", max_length=10)
    cod_preco = models.IntegerField(db_column="prod_codpreco")
    marca = models.CharField(db_column="prod_marca", max_length=30)
    trib_cod = models.CharField(db_column="prod_trib_codigo", max_length=15)
    status = models.CharField(db_column="prod_status", max_length=1)
    controla_est = models.CharField(db_column="prod_contrest", max_length=1)
    ativo_un = models.CharField(
        db_column="prod_ativounidades", max_length=2000)
    bloqueado_un = models.CharField(
        db_column="prod_bloqueadounidades", max_length=2000)

    def __str__(self):
        return f"Produtos(cod={self.cod},descricao={self.descricao})"

    class Meta:
        managed = False
        ordering = ["cod"]
        db_table = 'public"."produtos'
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Unidades(models.Model):
    cod = models.CharField(primary_key=True, null=False, editable=False,
                           db_column="unid_codigo", max_length=3,
                           help_text="Código da unidade/filial.")
    reduzido = models.CharField(null=False, editable=True, db_column="unid_reduzido",
                                max_length=5, help_text="Descrição resumida da unidade.")
    nome = models.CharField(null=False, db_column="unid_nome", max_length=10)

    def __str__(self):
        return f"{self.cod} - {self.reduzido}"

    class Meta:
        managed = False
        ordering = ["cod"]
        db_table = 'public"."unidades'
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"


class Produn(models.Model):
    prod = models.ForeignKey(Produtos, db_column="prun_prod_codigo",
                             on_delete=models.DO_NOTHING, related_name='prun', primary_key=True)
    unid = models.ForeignKey(
        Unidades, db_column="prun_unid_codigo", on_delete=models.DO_NOTHING)
    preco = models.DecimalField(
        db_column='prun_prvenda', decimal_places=5, max_digits=10)

    class Meta:
        managed = False
        db_table = 'public"."produn'
        verbose_name = "Produn"
        verbose_name_plural = "Produn"
        unique_together = ('prod', 'unid')


class Screen(models.Model):
    cod = models.AutoField(primary_key=True)
    unid = models.ForeignKey(Unidades, on_delete=models.DO_NOTHING)
    descricao = models.CharField(unique=True, max_length=30, null=False)
    background = models.FileField(upload_to='background/')
    minutes_reload_page = models.IntegerField(
        null=False, help_text="Quantia de minutos para atualização automática da página")
    seconds_promotion = models.IntegerField(
        null=False, help_text="Quantia de segundos que cada promoção será mantida na tela")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cod} - {self.descricao}"

    class Meta:
        db_table = 'screen'


class PromotionsProd(models.Model):
    prod = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
    screen = models.ForeignKey(
        Screen, on_delete=models.CASCADE, related_name='promotions')
    image = models.FileField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'promotions_prod'
