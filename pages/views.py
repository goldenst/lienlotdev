from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import type_choices , year_choices, make_choices

from listings.models import Listing
from sellers.models import Seller

# Create your views here.
def index(request):
  listings = Listing.objects.order_by('-avalible_date').filter(is_published=True)[:3]

  context = {
    'listings': listings,
    'type_choices': type_choices,
    'year_choices': year_choices,
    'make_choices' : make_choices
  }
  return render(request, 'pages/index.html', context)


def about(request):
  # Get sellers
  sellers = Seller.objects.all()

  context = {
    'sellers': sellers
  }
  return render(request, 'pages/about.html', context)