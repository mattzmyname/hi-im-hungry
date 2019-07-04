from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from hi_hungry.src import hi_hungry


def search(request):
	return JsonResponse(hi_hungry.main())
