from django.urls import path
from rocky import views
app_name='rocky'


urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
]
