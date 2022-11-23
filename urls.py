from django.urls import path
from . import views

urlpatterns = [
    path('', views.mains, name='mains'),
    path('insert', views.insert, name='insert'),
    path('redirects', views.redirects, name='redirects'),
    path('<int:id>', views.personId, name='id'),
    path('delete', views.deleteId, name='deleteId'),
    path('update/<int:id>', views.update, name='update'),
    path('personId/<int:id>', views.personId, name='personId'),
]