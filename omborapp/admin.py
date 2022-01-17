from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Ombor, Product, Client

@admin.register(Ombor, Product, Client)


class OmborAdmin(ModelAdmin):
    search_files = ['ism', 'dokon_nomi', 'joylashuv', 'turi']


class ProductAdmin(ModelAdmin):
    search_files = ['nom', 'brend_nomi', 'narx', 'miqdor']


class ClientAdmin(ModelAdmin):
    search_files = ['ism', 'tel', 'dokon_nomi', 'joylashuv']

