from shelf.views import HomePageView, post_DetailView
from django.urls import path

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', post_DetailView.as_view(), name='detail')
]