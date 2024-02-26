import json
from django.http import JsonResponse
from .models import Tweezer



def add_tweezer(request, id):
    try:
        tweezer = Tweezer.objects.get(id=id)
        tweezer.count += 1
        tweezer.save()
        return JsonResponse({'count': tweezer.count})
    except Tweezer.DoesNotExist:
        return JsonResponse({'error': 'Tweezer not found'}, status=404)

def subtract_tweezer(request, id):
    try:
        tweezer = Tweezer.objects.get(id=id)
        tweezer.count -= 1
        tweezer.save()
        return JsonResponse({'count': tweezer.count})
    except Tweezer.DoesNotExist:
        return JsonResponse({'error': 'Tweezer not found'}, status=404)


def create_tweezer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            modelname = data.get('modelname')
            color = data.get('color')
            count = data.get('count')

            if modelname is not None and color is not None and count is not None:
                tweezer = Tweezer.objects.create(modelname=modelname, color=color, count=count)
                return JsonResponse({ 'message': 'Tweezer created successfully', 'tweezer_id': tweezer.id})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid JSON data. Model name, color, and count are required.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


def update_tweezer(request, tweezer_id):
    tweezer = Tweezer.objects.filter(id=tweezer_id).first()
    if not tweezer:
        return JsonResponse({'success': False, 'message': 'Tweezer does not exist'})

    if request.method == 'POST':
        data = json.loads(request.body)
        modelname = data.get('modelname')
        color = data.get('color')
        count = data.get('count')

        if modelname and color and count:
            tweezer.modelname = modelname
            tweezer.color = color
            tweezer.count = count
            tweezer.save()
            return JsonResponse({'success': True, 'message': 'Tweezer updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data. Model name, color, and count are required.'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


def delete_tweezer(request, tweezer_id):
    tweezer = Tweezer.objects.filter(id=tweezer_id).first()
    if not tweezer:
        return JsonResponse({'success': False, 'message': 'Tweezer does not exist'})

    tweezer.delete()
    return JsonResponse({'success': True, 'message': 'Tweezer deleted successfully'})
from django.http import JsonResponse
from .models import Tweezer

def get_tweezers(request):
    # Retrieve all instances of the Tweezer model
    tweezers = Tweezer.objects.all()

    # Serialize the queryset to JSON
    serialized_tweezers = [
        {
            'modelname': tweezer.modelname,
            'color': tweezer.color,
            'count': tweezer.count,
        }
        for tweezer in tweezers
    ]

    # Return JSON response
    return JsonResponse(serialized_tweezers, safe=False)
