from django.urls import path
from django.contrib.auth import views as authViews
from . import views
from .views import LinkDelete

urlpatterns = [

    path('', views.LinkView.as_view(), name='safe_open'),
    path('user/', authViews.LoginView.as_view(template_name='site_link/index.html'), name='index'),
    path('delete/<int:pk>/',LinkDelete.as_view(), name='delete')
]
