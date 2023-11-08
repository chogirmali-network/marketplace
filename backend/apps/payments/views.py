from django.views.generic import TemplateView
from djstripe.models import Product
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def stripe_view(request):
    print("salom")
    return HttpResponse("Text")
