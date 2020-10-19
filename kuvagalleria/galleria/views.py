from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    return redirect('register/register/')

def login(request):
    return redirect('login/login/')

def index(request):
    sortTerm = request.GET.get('sort', None)
    if sortTerm == None:
        images = Image.objects.filter(private=False)
    else:
        if sortTerm == 'views' or sortTerm == 'rating':
            images = Image.objects.filter(private=False).order_by(sortTerm).reverse()
        elif sortTerm == 'newest':
            images = Image.objects.filter(private=False).order_by('date', 'time').reverse()
        elif sortTerm == 'oldest':
            images = Image.objects.filter(private=False).order_by('date','time')
        else:
            images = Image.objects.filter(private=False).order_by(sortTerm)

    context = {"images": images}
    return render(request, "galleria/frontpage.html", context)

def search(request):
    searchTerm = request.GET.get('search', '')

    print('searchterm', searchTerm)
    if searchTerm == None:
        images = Image.objects.filter(private=False)
    else:
        images = Image.objects.filter(private=False, title__contains=searchTerm)

    context = {"images": images}
    return render(request, "galleria/search_page.html", context)

def imagepage(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if image.private == True:
        print(image.user)
        if image.user != request.user:
            return redirect('/')
    image.views = image.views + 1
    image.save()
    if request.method == "POST":
        if 'delete' in request.POST:
            if user_authorized(request, image.user.username):
                image.delete()
                return redirect('/')
        if 'vote' in request.POST or request.user.lower() == "AnonymousUser".lower():
            if image.user == request.user:
                return redirect("imagepage", image.id)
            image.rating += 1
            image.save()
    context = {"image": image}
    return render(request, "galleria/image_page.html", context)


@login_required
def profilepage(request, user):
    # Check if currently logged in user is the owner
    if not user_authorized(request, user):
        return redirect("/")

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

def user_authorized(request, user):
    username = str(request.user).lower()
    print(username)
    print(user)
    if username != user.lower() or user.lower() == "AnonymousUser".lower():
        print('not authorized')
        return False
    else:
        print('authorized')
        return True