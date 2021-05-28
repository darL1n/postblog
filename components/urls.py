from django.urls import path
from . import views


urlpatterns = [
    path('', views.cal_date, name='cal_date'),
    path('<int:year>/<str:month>/', views.cal_date, name='cal_date')

]
