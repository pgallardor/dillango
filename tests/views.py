from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64
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
    img = open("khajiit.png", "wb")
    decoded = base64.b64decode(img64)
    img.write(decoded)

    return JsonResponse({'success': 'true'})
