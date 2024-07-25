
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from django.contrib import messages
# Create your views here.

# - homepage
def home(request):

   return render(request, 'index.html')

#-Login
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})


#- Logout
def logoutUser(request):
    logout(request)
    return redirect('home')


#- Register
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)

                messages.success(request, "User registration was successful!")

                return redirect('login')

    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)


#- Login
@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


#- View photos
@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


#- Edit description
def update_description(request, photo_id):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description:
                photo = Photo.objects.get(pk=photo_id)
                photo.description = description
                photo.save()
                return redirect('gallery')  


#- Add photo
@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)


#- Delete photo
@login_required(login_url='login')
def deletePhoto(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    if photo.category.user == request.user:
        photo.delete()
        return redirect('gallery')
    else:
        return redirect('gallery')

#- Delete category
@login_required(login_url='my_login')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        Photo.objects.filter(category=category).delete()
        
        category.delete()
        
        
    return redirect('gallery')
    
    

