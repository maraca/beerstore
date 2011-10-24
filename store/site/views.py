from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader

from store.models import Beer
from store.models import BeerStyle

def index(request):
    """Home page"""
    template = loader.get_template('index.html')
    beers = Beer.objects.all()[:10]
    context = RequestContext(request, {
        'styles': BeerStyle.objects.all(),
        'beers': beers,
        })
    
    return HttpResponse(template.render(context))
