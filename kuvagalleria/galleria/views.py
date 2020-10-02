from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm
# from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    images = Image.objects.filter(private=False)
    context = {'images': images}
    return render(request, 'galleria/frontpage.html', context)

def imagepage(request, pk):
    image = get_object_or_404(Image, pk=pk)
    context = {'image': image}
    return render(request, 'galleria/image_page.html', context)


def profilepage(request, user):
    username = str(request.user).lower()
    images = []
    if username != user.lower() or user.lower() == 'AnonymousUser'.lower():
        return redirect('/')
    images = Image.objects.filter(user=request.user)
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            print('form is valid')
            image = form.save(commit=False)
            image.user = request.user
            image.save()

        else: 
            print('form is not valid')

    context = {'images': images, 'form': form}

    return render(request, 'galleria/profile_page.html', context)
