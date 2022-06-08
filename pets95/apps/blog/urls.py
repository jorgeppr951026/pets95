from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home' ),
    path('todas_las_mascotas/', todas_las_mascotas,name='todas_las_mascotas' ),
    path('gatos/', gatos,name='gatos' ),
    path('perros/', perros,name='perros' ),
    path('<int:id>/',detailPet ,name='detailPet' ),
    path('post/<int:id>/',detailPost ,name='detailPost' ),
    path('sobre_nosotros/', sobreNosotros, name='sobre_nosotros'),
]