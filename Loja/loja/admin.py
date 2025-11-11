from django.contrib import admin
from .models import * #imporata nossos models
admin.site.register(Categoria)
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    empty_value_display = 'Vazio'
    search_fields = ('Produto',)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)