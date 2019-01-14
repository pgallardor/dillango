from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tests.models import Ficha, Paciente
import base64
# Create your views here.


@csrf_exempt
def single_json(request):
    stringed = str(request.body)
    print('='.split(stringed))

    return JsonResponse({'field': 'content'})


def json_list(request):
    return JsonResponse([
        {'field': 'content1'},
        {'field': 'content2'}
    ], safe=False)


@csrf_exempt
def receive_file(request):
    if request.method == 'POST':
        img64 = request.POST.get('media')
        img = open("khajiit.jpg", "wb")
        decoded = base64.b64decode(img64)
        img.write(decoded)

        return JsonResponse({'success': 'true'})

    return HttpResponse('<h1>Subete algo prro</h1>')


@csrf_exempt
def create_record(request):
    if request.method == 'POST':
        list = request.POST.copy()
        paciente = Paciente.objects.get(rut=list.get('rut'))
        ficha = Ficha(
            rut=paciente,
            imagenes=list.get('imagenes')
        )
        ficha.save()
        print(ficha.id)
        return JsonResponse({'success': 'true'})

    return HttpResponse('<h1>Crear la ficha con POST</h1>')
