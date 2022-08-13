from django.urls import path
from .views import GetCoinInfo

app_name = "coins"
urlpatterns = [
    path('info/', GetCoinInfo.as_view(), name='coins-list')
]