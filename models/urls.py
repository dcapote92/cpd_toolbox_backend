from django.urls import path
from . import views

urlpatterns = [
    path('models/', views.ModelCreateListView.as_view(), name='model-list-view'),
    path('models/<int:pk>/', views.ModelRetrieveUpdateDestroy.as_view(), name='model-detail-view')
]