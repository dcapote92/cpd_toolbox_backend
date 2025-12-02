from django.contrib import admin
from django.urls import path
from models.views import ModelCreateListView, ModelRetrieveUpdateDestroy
from sections.views import SectionCreateListView, SectionRetrieveUpdateDestroy
from scales.views import ScaleCreateListView, ScaleRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('models/', ModelCreateListView.as_view(), name='model-list-view'),
    path('models/<int:pk>/', ModelRetrieveUpdateDestroy.as_view(), name='model-detail-view'),

    path('sections/', SectionCreateListView.as_view(), name='section-list-view'),
    path('sections/<int:pk>/', SectionRetrieveUpdateDestroy.as_view(), name='section-detail-view'),

    path('scales/', ScaleCreateListView.as_view(), name='scale-list-view'),
    path('scales/<int:pk>/', ScaleRetrieveUpdateDestroy.as_view(), name='scale-detail-view'),
]
