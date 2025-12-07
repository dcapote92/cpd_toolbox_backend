from django.urls import path
from . import views


urlpatterns = [
    path('sections/', views.SectionCreateListView.as_view(), name='section-list-view'),
    path('sections/<int:pk>/', views.SectionRetrieveUpdateDestroy.as_view(), name='section-detail-view')
]
