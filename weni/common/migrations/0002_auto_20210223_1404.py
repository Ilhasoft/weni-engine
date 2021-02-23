# Generated by Django 2.2.17 on 2021-02-23 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('type_service_flows', 'Flows service'), ('type_service_inteligence', 'Inteligence Service'), ('type_service_chat', 'Chat Service')], default='type_service_chat', max_length=50, verbose_name='service type'),
        ),
    ]