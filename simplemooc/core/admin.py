<<<<<<< HEAD
from django.contrib import admin
from .models import Empresa
# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id_emp', 'cnpj', 'razao', 'fantasia', 'endereco', 'cidade', 'uf', 'cep', 'ativo', 'data_cadastro')
    list_display_links = ('id_emp', 'cnpj', 'razao', 'fantasia', 'endereco', 'cidade', 'uf', 'cep', 'ativo', 'data_cadastro')
    list_filter = ('id_emp', 'cnpj', 'razao', 'fantasia', 'cidade', 'uf', 'ativo')
    search_fields = ('id_emp', 'cnpj', 'razao', 'fantasia', 'cidade', 'uf', 'ativo')

admin.site.register(Empresa, EmpresaAdmin)
=======
from django.contrib import admin

# Register your models here.
>>>>>>> f2e683044aaafdb905a72a34bad0582a9ae5a7ed
