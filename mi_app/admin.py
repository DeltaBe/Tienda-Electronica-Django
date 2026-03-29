from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Dispositivo, Categoria # Importa tus modelos

# Clase opcional para que el admin se vea más pro
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria') # Columnas a mostrar
    search_fields = ('nombre',) # Barra de búsqueda
    list_filter = ('categoria',) # Filtro lateral

# Registra los modelos
admin.site.register(Categoria)
admin.site.register(Dispositivo, DispositivoAdmin)