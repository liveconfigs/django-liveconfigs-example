from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('sync', views.IndexSyncView.as_view()),
    path('async', views.IndexView.as_view()),
]
