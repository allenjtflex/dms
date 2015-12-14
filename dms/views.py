from django.shortcuts import render


def index(request):
	title = "Index Home"
	return render(request, 'index.html', locals())