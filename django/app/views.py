from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Event

@csrf_exempt
def receiver(request):
    print(request.POST)
    data = request.POST.dict()
    if data:
        name = data.get('name')
        source = data.get('source')
        description = data.get('description')
        e = Event.objects.create(name=name, source=source, description=description)
        print(f'{e.uuid=}')

    return HttpResponse('200')
