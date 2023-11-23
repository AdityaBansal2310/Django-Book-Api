from django.contrib import admin
from django.urls import path 
from ApiApplication.views import BookApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookApiView.as_view(), name='book-list'),
    path('book/<int:book_id>/', BookApiView.as_view(), name='book-detail'),
]
