from django.urls import path


from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from .views import (
    home,
    ProjectsView,
    ProjectDetailView,
    contacts, about, Shop, ShopDetail, CartView,
    add_to_cart
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<slug>/', ProjectDetailView.as_view(), name="project-detail"),
    path('shop/', Shop.as_view(), name='shop'),
    path('shop/<slug>/', ShopDetail.as_view(), name="shop-detail"),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('cart/', CartView.as_view(), name="cart"),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
