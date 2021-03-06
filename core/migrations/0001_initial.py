# Generated by Django 2.1.3 on 2018-11-07 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('cod', models.IntegerField(db_column='prod_codigo', primary_key=True, serialize=False)),
                ('extra3_barras', models.CharField(db_column='prod_extra3', max_length=50)),
                ('cod_caixa', models.CharField(db_column='prod_codcaixa', max_length=14)),
                ('cod_barra', models.CharField(db_column='prod_codbarras', max_length=13)),
                ('descricao', models.CharField(db_column='prod_descricao', max_length=40)),
                ('descricao_comp', models.CharField(db_column='prod_complemento', max_length=40)),
                ('descricao_pdv', models.CharField(db_column='prod_descrpdvs', max_length=40)),
                ('grupo_nome', models.CharField(db_column='prod_grup_nome', max_length=40)),
                ('dpto_cod', models.CharField(db_column='prod_dpto_codigo', max_length=3)),
                ('emb', models.CharField(db_column='prod_emb', max_length=2)),
                ('emb_qtd', models.IntegerField(db_column='prod_qemb')),
                ('pesavel', models.CharField(db_column='prod_balanca', max_length=1)),
                ('peso', models.DecimalField(db_column='prod_peso', decimal_places=5, max_digits=15)),
                ('peso_liq', models.DecimalField(db_column='prod_pesoliq', decimal_places=5, max_digits=15)),
                ('data_alt', models.DateField(db_column='prod_dataalt')),
                ('data_cad', models.DateField(db_column='prod_datacad')),
                ('ncm', models.CharField(db_column='prod_codigoncm', max_length=10)),
                ('cod_preco', models.IntegerField(db_column='prod_codpreco')),
                ('marca', models.CharField(db_column='prod_marca', max_length=30)),
                ('trib_cod', models.CharField(db_column='prod_trib_codigo', max_length=15)),
                ('status', models.CharField(db_column='prod_status', max_length=1)),
                ('controla_est', models.CharField(db_column='prod_contrest', max_length=1)),
                ('ativo_un', models.CharField(db_column='prod_ativounidades', max_length=2000)),
                ('bloqueado_un', models.CharField(db_column='prod_bloqueadounidades', max_length=2000)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'public"."produtos',
                'ordering': ['cod'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('cod', models.CharField(db_column='unid_codigo', editable=False, help_text='Código da unidade/filial.', max_length=3, primary_key=True, serialize=False)),
                ('reduzido', models.CharField(db_column='unid_reduzido', help_text='Descrição resumida da unidade.', max_length=5)),
                ('nome', models.CharField(db_column='unid_nome', max_length=10)),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
                'db_table': 'public"."unidades',
                'ordering': ['cod'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PromotionsProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('show_promotion', models.BooleanField(default=False)),
                ('show_list', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'promotions_prod',
                'ordering': ('screen', 'prod'),
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=30, unique=True)),
                ('background_list', models.FileField(upload_to='background/')),
                ('background', models.FileField(upload_to='background/')),
                ('seconds_promotion', models.IntegerField(help_text='Quantia de segundos que cada promoção será mantida na tela')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Unidades')),
            ],
            options={
                'db_table': 'screen',
            },
        ),
        migrations.CreateModel(
            name='Produn',
            fields=[
                ('prod', models.ForeignKey(db_column='prun_prod_codigo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='prun', serialize=False, to='core.Produtos')),
                ('preco', models.DecimalField(db_column='prun_prpdv', decimal_places=5, max_digits=10)),
            ],
            options={
                'verbose_name': 'Produn',
                'verbose_name_plural': 'Produn',
                'db_table': 'public"."produn',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='promotionsprod',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Produtos'),
        ),
        migrations.AddField(
            model_name='promotionsprod',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='core.Screen'),
        ),
    ]
