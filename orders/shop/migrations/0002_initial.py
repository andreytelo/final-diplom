# Generated by Django 4.1.4 on 2023-01-15 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='productparameter',
            name='parameter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='shop.parameter', verbose_name='Параметр'),
        ),
        migrations.AddField(
            model_name='productparameter',
            name='product_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='shop.productinfo', verbose_name='Информация о продукте'),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='shop.shop', verbose_name='Магазин'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='shop.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='shop.productinfo', verbose_name='Информация о продукте'),
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Контакт', to='user_auth.contact', verbose_name='Контакт'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(blank=True, related_name='categories', to='shop.shop', verbose_name='Магазины'),
        ),
        migrations.AddConstraint(
            model_name='productparameter',
            constraint=models.UniqueConstraint(fields=('product_info', 'parameter'), name='unique_product_parameter'),
        ),
        migrations.AddConstraint(
            model_name='productinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop'), name='unique_product_info'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order_id', 'product_info'), name='unique_order_item'),
        ),
    ]
