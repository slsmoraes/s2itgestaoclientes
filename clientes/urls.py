from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete

urlpatterns = [
    path('list/', persons_list, name="person_list"),                # Lista todas
    path('new/', persons_new, name="person_new"),                   # Incluir
    path('update/<int:id>/', persons_update, name="person_update"), # Alterar
    path('delete/<int:id>/', persons_delete, name="person_delete"), # Excluir

]
