from django.http import JsonResponse
from .models import Lashes
import json





from django.http import JsonResponse


from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Lashes

def add_lashes(request, id):
    try:
        lashes = Lashes.objects.get(id=id)
        lashes.count += 1
        lashes.save()
        return JsonResponse({'count': lashes.count})
    except Lashes.DoesNotExist:
        return JsonResponse({'error': 'Lashes not found'}, status=404)

def subtract_lashes(request, id):
    try:
        lashes = Lashes.objects.get(id=id)
        lashes.count -= 1
        lashes.save()
        return JsonResponse({'count': lashes.count})
    except Lashes.DoesNotExist:
        return JsonResponse({'error': 'Lashes not found'}, status=404)





def create_lashes(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        modelname = data.get('modelname')
        length = data.get('length')
        width = data.get('width')
        count = data.get('count')

        if modelname and length and width and count:
            lashes = Lashes.objects.create(modelname=modelname, length=length, width=width, count=count)
            return JsonResponse({'success': True, 'message': 'Lashes created successfully', 'lashes_id': lashes.id})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data. Model name, length, width, and count are required.'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


def update_lashes(request, lashes_id):
    lashes = Lashes.objects.filter(id=lashes_id).first()
    if not lashes:
        return JsonResponse({'success': False, 'message': 'Lashes does not exist'})

    if request.method == 'POST':
        data = json.loads(request.body)
        modelname = data.get('modelname')
        length = data.get('length')
        width = data.get('width')
        count = data.get('count')

        if modelname and length and width and count:
            lashes.modelname = modelname
            lashes.length = length
            lashes.width = width
            lashes.count = count
            lashes.save()
            return JsonResponse({'success': True, 'message': 'Lashes updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data. Model name, length, width, and count are required.'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


def delete_lashes(request, lashes_id):
    lashes = Lashes.objects.filter(id=lashes_id).first()
    if not lashes:
        return JsonResponse({'success': False, 'message': 'Lashes does not exist'})

    lashes.delete()
    return JsonResponse({'success': True, 'message': 'Lashes deleted successfully'})
from django.http import JsonResponse
from .models import Lashes

def get_lashes(request):
    # Retrieve all instances of the Lashes model
    lashes = Lashes.objects.all()

    # Serialize the queryset to JSON
    serialized_lashes = [
        {
            'modelname': lash.modelname,
            'length': lash.length,
            'width': lash.width,
            'count': lash.count,
        }
        for lash in lashes
    ]

    # Return JSON response
    return JsonResponse(serialized_lashes, safe=False)
