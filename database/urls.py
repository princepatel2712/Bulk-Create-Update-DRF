from .views import CarGenericView
from django.urls import path


urlpatterns = [
    path('car/', CarGenericView.as_view(), name='car')
]