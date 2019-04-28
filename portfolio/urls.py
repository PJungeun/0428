from django.contrib import admin
from django.urls import path
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', portfolio.views.home, name='home'),
    path('person/<int:person_id>/', portfolio.views.detail, name='detail'),
    path('person/new/', portfolio.views.person_new, name='new'),
    path('<int:person_id>/edit/', portfolio.views.person_edit, name='edit'),
    path('<int:person_id>/delete/', portfolio.views.person_delete, name='delete'),
]
