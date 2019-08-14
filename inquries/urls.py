from django.urls import path
from .views import make_inquiry
urlpatterns = [
    path('makeinquiry/', make_inquiry, name='makeinquiry'),

]
