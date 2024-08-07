from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view()),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
