from .views import CreateCarView, UpdateCarView
from django.urls import path

urlpatterns = [
    path('bulk-create/', CreateCarView.as_view(), name='bulk_create'),
    path('bulk-update/<int:id>/', UpdateCarView.as_view(), name='bulk_update'),
]
