from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', CRUDViewset)


urlpatterns = [
    # path('post',ProductCRUDAPI.as_view()),
    # path('get',ProductCRUDAPI.as_view()),
    # path('get/<int:product_id>',ProductCRUDAPI.as_view()),
    # path('put/<int:product_id>',ProductCRUDAPI.as_view()),
    # path('patch/<int:product_id>',ProductCRUDAPI.as_view()),    
    # path('delete/<int:product_id>',ProductCRUDAPI.as_view()),
    
    
    # path('products',ProductCRUD),
    # path('products/<int:product_id>',ProductCRUD)
    
    # path('products',CRGeneric.as_view()),
    # path('products/<int:pk>/',UDGeneric.as_view())
    
    path('',include(router.urls))
]

