from django.shortcuts import render

# Create your views here.
def test(request):
	from django.http import HttpResponse
	return HttpResponse('Helllo World')