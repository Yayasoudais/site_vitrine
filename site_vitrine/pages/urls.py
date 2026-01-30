from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('services/',views.services, name='services'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('contact/', views.contact, name='contact'),
    
    # URLs dynamique
    
    path('article/<int:id>',views.article_detail, name = 'article_detail'),
    path('category/<str:category>',views.category_products, name= 'category_products'), 
    path('user/<str:username>',views.user_profile, name= 'user_profile'),
         
]