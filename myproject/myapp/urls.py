from django.urls import path
from .views import DataListCreateAPIView, RegisterAPIView, LoginAPIView, LogoutAPIView, Requisicao, RequisicaoCommit, RequisicaoUpdatePost
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("data/", Requisicao),
    path("data/delete", Requisicao),
    path("data/update", Requisicao),
    path("data/update/post", RequisicaoUpdatePost),
    path("data/update/c1", RequisicaoCommit),
    path("data/update/c2", Requisicao),
    path("data/update/c3", Requisicao),
    path('api/data/', DataListCreateAPIView.as_view(), name='data-list-create'),
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),

    #path('api/createuser', RegisterAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
