from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.get_books),
    path('create/', views.create_book),
    path('<str:book_id>/', views.get_book_by_id),
    path('delete/<str:book_id>/', views.remove_book)

]
