from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def single_json(request):
    print(request.body)
    return JsonResponse({'field': 'content'})


def json_list(request):
    return JsonResponse([
        {'field': 'content1'},
        {'field': 'content2'}
    ], safe=False)


@csrf_exempt
def receive_file(request):
    img64 = request.POST.get('media')
    # img = open("sanik_arrived.png", "wb")
    print(str.encode(img64, 'base-64'))
    # img.write()
    return JsonResponse({'success': 'true'})
