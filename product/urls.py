from django.urls import path
from . import views

urlpatterns = [
    # path('categoriesList/', views.CategoryListAPIView.as_view()),
    path('categoriesList/', views.CategoryViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('categoriesList/<int:id>/', views.CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    # path('<int:id>/', views.CategoryDetailAPIView.as_view()),
    # path('productsList/', views.ProductListAPIView.as_view()),
    path('productsList/', views.ProductViewSet.as_view({
        'get':'list', 
        'post':'create'
    })),
    path('productsList/<int:id>/', views.ProductViewSet.as_view({
        'get':'retrieve', 
        'put':'update',
        'delete': 'destroy'
    })),
    # path('<int:id>/', views.ProductDetailAPIView.as_view()),
    # path('reviewList/', views.ReviewListAPIIView.as_view()),
    path('reviewList/', views.ReviewViewSet.as_view({
        'get':'list', 
        'post':'create'
    })),
    path('reviewList/<int:id>/', views.ReviewViewSet.as_view({
        'get':'retrieve', 
        'put':'update',
        'delete': 'destroy'
    })),
#     path('<int:id>/', views.ReviewDetailAPIView.as_view())
]
