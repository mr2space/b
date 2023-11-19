from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FamilyPhotosForm
from django.contrib.auth.models import User
from .models import Photos


def uploadphoto(request):
    if request.method == 'POST':
        form = FamilyPhotosForm(request.POST, request.FILES)
        if form.is_valid():
            family_photo = form.save()
            # You can do additional actions after saving the form, if needed
            return redirect('/g')  # Redirect to a success page or another page
    else:
        form = FamilyPhotosForm()

    return render(request, 'gallary/upload.html', {'form': form})


@login_required(login_url="/auth")
def showphoto(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user_groups = user.groups.all()
    photos = []
    for u in user_groups:
        p = Photos.objects.all().filter(category = u.name)
        for photo in  p:
            photos.append(photo)
    p = []
    for i in photos:
        p.append(i.photo.url)
    return render(request, 'gallary/g.html', {'photos':p})
    
    
    