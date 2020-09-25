from django.shortcuts import render, get_object_or_404
from .models import Image
# Create your views here.
def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'galleria/frontpage.html', context)

def imagepage(request, pk):
    image = get_object_or_404(Image, pk=pk)
    context = {'image': image}
    return render(request, 'galleria/image_page.html', context)