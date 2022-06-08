import os
import uuid

from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from pets.settings.base import BASE_DIR

# Create your models here.
 
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoria activada/Categoria no activada',default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


    def __str__(self):
        return self.nombre



class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos del Autor', max_length=255, null=False, blank=False)
    image = models.ImageField('Imagen', upload_to='static/contacts/', height_field=None, width_field=None, max_length=None,blank=True,null=True)
    facebook = models.URLField('Facebook',null=True, blank=True)
    instagram = models.URLField('Instagram',null=True, blank=True)
    twitter = models.URLField('Twitter',null=True, blank=True)
    watsap = models.CharField('Watsap',null=True, blank=True, max_length=11)
    correo = models.EmailField('Correo Electónico', null=True , blank=True)
    reference = models.TextField('Referencia',null=True , blank=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    image = models.ImageField('Imagen', upload_to='static/posts/', height_field=None, width_field=None, max_length=None,  blank=True, null=True)
    contenido = RichTextField()
    bibliografia = models.TextField('Referencias Bibliográficas', blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo


class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=90, blank=True, null=True)
    sterilization = models.BooleanField('Esterilizdo/No Esterilizado',default=True)
    estado = models.BooleanField('Garantiza esterilización/No garantiza esterilización', default=True)
    direction = models.CharField('Dirección', max_length=255)
    sex = models.CharField('Sexo',choices =(('Hembra', "Hembra"),('Macho', 'Macho')), max_length=50, null=True, blank=True)
    image_url = models.URLField('Imagen url', max_length=500, blank=True, null=True)
    image = models.ImageField('Imagen', upload_to='static/pets/', height_field=None, width_field=None, max_length=None, blank=True , null = True)
    dado_por = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    description = RichTextField('Descripcion' , blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)



    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField('Imagen', upload_to='static/galery/', height_field=None, width_field=None, max_length=None, blank=True , null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __str__(self):
        return f'{self.image}'
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('image_detail', kwargs={'pk': self.pk})



@receiver(models.signals.post_delete, sender=Pet)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.image.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Pet)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass




@receiver(models.signals.post_delete, sender=Autor)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.image.delete(save=False)
    except:
        pass

@receiver(models.signals.pre_save, sender=Autor)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass