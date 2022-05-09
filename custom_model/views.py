from django.shortcuts import render

from django.http import HttpResponse

from .models import Nft

# Create your views here.

def index(request):
    """ Render the custom_model page """

    return HttpResponse("Hello World!")

def nft_by_id(request, nft_id):
    nft = Nft.objects.get(pk=nft_id)
    return render(request, 'nft_details.html', {'nft':nft})