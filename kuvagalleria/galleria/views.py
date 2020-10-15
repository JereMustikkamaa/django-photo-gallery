from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    images = Image.objects.filter(private=False)
    context = {"images": images}
    return render(request, "galleria/frontpage.html", context)


def imagepage(request, pk):
    image = get_object_or_404(Image, pk=pk)
    context = {"image": image}
    return render(request, "galleria/image_page.html", context)


@login_required
def profilepage(request, user):
    # Check if currently logged in user is the owner
    username = str(request.user).lower()
    if username != user.lower() or user.lower() == "AnonymousUser".lower():
        return redirect("/")

    # # Form
    # imageForm = ImageForm()
    # if request.method == "POST":
    #     imageForm = ImageForm(request.POST, request.FILES)
    #     if imageForm.is_valid():
    #         print("form is valid")
    #         image = imageForm.save(commit=False)
    #         image.user = request.user
    #         image.save()
    #         return redirect("profile", request.user)

    # Get users pictures and subfolders
    images = Image.objects.filter(user=request.user).order_by('subfolder')
    folders = []
    for x in images:
        if x.subfolder not in folders:
            folders.append(x.subfolder)
    print(folders)
    context = {"images": images, "folders": folders}

    return render(request, "galleria/profile_page.html", context)


@login_required
def uploadpage(request):
    imageForm = ImageForm()
    if request.method == "POST":
        imageForm = ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
            print("form is valid")
            image = imageForm.save(commit=False)
            image.user = request.user
            image.save()
            return redirect("profile", request.user)

    context = {"form": imageForm}

    return render(request, "galleria/upload_page.html", context)
