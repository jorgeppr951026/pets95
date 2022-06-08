from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
# Register your models here.

#Añadiendo la opcion importar y exportar a los modelos en el admin
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PetResource(resources.ModelResource):
    class Meta:
        model = Pet

class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

#Personalizando los campos que salen en la interfas administrativa
class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado','fecha_creacion',)
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres', 'apellidos','correo','fecha_creacion',)
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('id','titulo','fecha_creacion')
    resource_class = PostResource

class PetAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = [ 'name','direction','sex','dado_por','categoria',]
    list_display = ('name','direction','sex','dado_por','categoria')
    resource_class = PetResource




class GalleryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['image']
    list_display = ('image','image_tag',)
    resource_class = ImageResource

    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="100px" />'.format(obj.image.url))

    image_tag.short_description = 'Image Preview'
    readonly_fields = ['image_tag']







admin.site.register(Image,GalleryAdmin)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Pet,PetAdmin)
