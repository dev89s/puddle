from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Item

# Create your views here.
def details(request, pk):
  item = get_object_or_404(Item, pk=pk)

  return render(request, 'item/detail.html', {
    'item': item
  })
