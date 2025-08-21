from django.urls import path
from .views import * 

urlpatterns = [
    path('autores', AutoresView.as_view()),
    path('editora', EditoraView.as_view()),
    path('livros', LivrosView.as_view())

]
