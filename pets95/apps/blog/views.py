from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from pets.settings.base import *
from datetime import datetime
# Create your views here.

def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.exclude(id = 1).order_by('-fecha_creacion','-id')
    actual_date = datetime.today()
   

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(contenido__icontains = queryset)|
            Q(bibliografia__icontains = queryset)
        ).distinct().exclude(id = 1)

  
    posts = paginar(request,posts,3)

    return render(request, 'home.html', {'posts':posts, 'actual_date':actual_date})


def detailPost(request,id):
    detail_post = get_object_or_404(Post,id = id)
    return render(request, 'post.html',{'detail_post':detail_post})



def sobreNosotros(request):
    detail_post = get_object_or_404(Post ,id = 1)
    contacts = Autor.objects.all()
    context = {
        'detail_post':detail_post,
        'contacts' : contacts,
    }
    return render(request, 'sobre_nosotros.html',context)



def todas_las_mascotas(request):
    pets = Pet.objects.all()

    queryset = request.GET.get('buscar')
    if queryset:
        pets = buscar(queryset, 'Todas')
    pets = paginar(request,pets)
    return render(request, 'todas_las_mascotas.html', {'pets':pets})


def gatos(request):
    pets = Pet.objects.filter(
        categoria = Categoria.objects.get(nombre__iexact = 'Gatos')
    )
    queryset = request.GET.get('buscar')
    if queryset:
        pets = buscar(queryset, 'Gatos')
    pets = paginar(request,pets)
    return render(request, 'gatos.html', {'pets':pets})


def perros(request):
    pets = Pet.objects.filter(
        categoria = Categoria.objects.get(nombre__iexact = 'Perros')
    )
    queryset = request.GET.get('buscar')
    if queryset:
        pets = buscar(queryset, 'Perros')
    pets = paginar(request,pets)
    return render(request, 'perros.html', {'pets':pets})




def detailPet(request,id):
    pet = get_object_or_404(Pet,id = id)
    return render(request, 'pet.html',{'pet':pet})



def buscar(queryset , categoria_buscar ):
    if categoria_buscar == 'Todas':
        return Pet.objects.filter(
            Q(name__icontains = queryset)|
            Q(direction__icontains = queryset)|
            Q(sex__icontains = queryset)
        ).distinct()
    return  Pet.objects.filter(
            Q(name__icontains = queryset)|
            Q(direction__icontains = queryset)|
            Q(sex__icontains = queryset),
            categoria = Categoria.objects.get(nombre__iexact = categoria_buscar)
        ).distinct()
    
    
def paginar(request,posts, pages = 6):
    paginator = Paginator(posts, pages)
    page =request.GET.get('page')
    return paginator.get_page(page)



