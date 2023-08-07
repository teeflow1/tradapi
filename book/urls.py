from django.urls import path
from book.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name = 'home')
     
]
