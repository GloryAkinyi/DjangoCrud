
from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
]
