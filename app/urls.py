from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cards/', views.card_list),
    path('cards/<str:pk>', views.card_detail),
    path('users/', views.UserList.as_view()),
    path('users/<str:pk>', views.UserDetail.as_view()),
    path('category/<str:pk>', views.category_detail),
    path('categories/', views.CategoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
