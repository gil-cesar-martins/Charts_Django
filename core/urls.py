from django.urls import path
from .views import IndexView, DataJSONView

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('charts/', DataJSONView.as_view(), name='charts'),
]
