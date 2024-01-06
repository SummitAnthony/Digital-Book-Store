from . import views
from django.urls import include, path



app_name = 'game'
urlpatterns = [
    #/welcome/
    #/game/
    path('', views.IndexClassView.as_view(), name="index"),
    #/game/1
    path('<int:pk>/', views.GameDetail.as_view(), name="detail"),
    path('item/', views.item, name="item"),
    path('user/', views.user, name="user"),  

    #add items 
    path('add', views.CreateItem.as_view(), name = 'create_item'),
    #edit items
    path('update/<int:id>', views.update_item, name='update_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]