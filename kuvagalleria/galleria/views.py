from django.shortcuts import render

# Create your views here.
def index(request):
    # images = Images.objects.get()
    context = {}
    return render(request, 'galleria/frontpage.html', context)