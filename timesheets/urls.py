from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'entries', views.EntryViewSet, basename='Entry')

urlpatterns = [
    path('', include(router.urls)),
    path('summaries', views.SummaryView.as_view(), name='timesheet-summary')
]
