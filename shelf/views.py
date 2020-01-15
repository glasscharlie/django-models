from django.views.generic import ListView, DetailView
from .models import Shelf

class HomePageView(ListView):
    template_name = 'home.html'
    model = Shelf
    context_object_name = 'shelf'

class post_DetailView(DetailView):
    template_name = 'detail.html'
    model = Shelf