from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoCreate
from django.http import HttpResponse

#DataFlair
def index(request):
    shelf = Photo.objects.all()
    return render(request, 'photo/library.html', {'shelf': shelf})

def upload(request):
    upload = PhotoCreate()
    if request.method == 'POST':
        upload = PhotoCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'photo/upload_form.html', {'upload_form':upload})

def update_photo(request, photo_id):
    photo_id = int(photo_id)
    try:
        photo_sel = Photo.objects.get(id = photo_id)
    except Photo.DoesNotExist:
        return redirect('index')
    photo_form = PhotoCreate(request.POST or None, instance = photo_sel)
    if photo_form.is_valid():
       photo_form.save()
       return redirect('index')
    return render(request, 'photo/upload_form.html', {'upload_form':photo_form})

def delete_photo(request, photo_id):
    photo_id = int(photo_id)
    try:
        photo_sel = Photo.objects.get(id = photo_id)
    except Photo.DoesNotExist:
        return redirect('index')
    photo_sel.delete()
    return redirect('index')