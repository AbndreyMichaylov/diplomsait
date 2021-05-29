from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from PIL import Image
import io
from uuid import uuid4
from .tesseract.src import translate_api

def show_page(request):
    return render(request, 'index.html')

def translate(request):
    filename = request.POST['photo_name']
    requestLang = request.POST['lang']
    res = translate_api.translate_image(str(settings.MEDIA_ROOT), filename, requestLang)
    return JsonResponse({"result" : res})

def save_img(request):
    filename = request.POST['photo_name']
    requestImageBytes = request.FILES['photo'].read()
    image = Image.open(io.BytesIO(requestImageBytes))
    save_root = str(settings.MEDIA_ROOT) + '/' + filename
    image.save(save_root)
    print(save_root)
    return JsonResponse({"image_root" : '../media/' + filename})