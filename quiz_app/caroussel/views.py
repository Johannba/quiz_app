from django.shortcuts import render, redirect
from .models import CarouselImage
from .forms import CarouselImageForm

def carousel(request):
    images = CarouselImage.objects.all()
    return render(request, 'caroussel/carousel.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = CarouselImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carousel')
    else:
        form = CarouselImageForm()
    return render(request, 'caroussel/carousel/upload_image.html', {'form': form})
