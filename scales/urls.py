from django.urls import path
from . import views


urlpatterns = [
    path('scales/', views.ScaleCreateListView.as_view(), name='scale-list-view'),
    path('scales/<int:pk>/', views.ScaleRetrieveUpdateDestroy.as_view(), name='scale-detail-view')
]
