from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tests.models import Ficha, Paciente
import base64
# Create your views here.


@csrf_exempt
def single_json(request):
    stringed = request.body.decode('utf-8')
    measures = {}
    list = []
    for item in stringed.split('&'):
        list += [item.split('=')]

    for tup in list:
        if tup[0] in measures:
            measures[tup[0]].append(tup[1])
        elif tup[0] != '':
            measures[tup[0]] = [tup[1]]

    print(measures)
    f = open('../temps.txt', 'w+')
    for k, v in measures.items():
        f.write("%s : " % k)
        for t in v:
            f.write("%s " % t)
        f.write('\n')
    f.close
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
