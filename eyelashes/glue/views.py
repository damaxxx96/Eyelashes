from django.http import JsonResponse
from .models import Glue
import json
def add_glue(request, id):
    try:
        glue = Glue.objects.get(id=id)
        glue.count += 1
        glue.save()
        return JsonResponse({'count': glue.count})
    except Glue.DoesNotExist:
        return JsonResponse({'error': 'Glue not found'}, status=404)

def subtract_glue(request, id):
    try:
        glue = Glue.objects.get(id=id)
        glue.count -= 1
        glue.save()
        return JsonResponse({'count': glue.count})
    except Glue.DoesNotExist:
        return JsonResponse({'error': 'Glue not found'}, status=404)




def create_glue(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        modelname = data.get('modelname')
        content = data.get('content')
        count = data.get('count')

        if modelname and content and count:
            glue = Glue.objects.create(modelname=modelname, content=content, count=count)
            return JsonResponse({'success': True, 'message': 'Glue created successfully', 'glue_id': glue.id})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data. Model name, content, and count are required.'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


def update_glue(request, glue_id):
    glue = Glue.objects.filter(id=glue_id).first()
    if not glue:
        return JsonResponse({'success': False, 'message': 'Glue does not exist'})

    if request.method == 'POST':
        data = json.loads(request.body)
        modelname = data.get('modelname')
        content = data.get('content')
        count = data.get('count')

        if modelname and content and count:
            glue.modelname = modelname
            glue.content = content
            glue.count = count
            glue.save()
            return JsonResponse({'success': True, 'message': 'Glue updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data. Model name, content, and count are required.'})
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})


def delete_glue(request, glue_id):
    glue = Glue.objects.filter(id=glue_id).first()
    if not glue:
        return JsonResponse({'success': False, 'message': 'Glue does not exist'})

    glue.delete()
    return JsonResponse({'success': True, 'message': 'Glue deleted successfully'})


def get_glues(request):
    # Retrieve all instances of the Glue model
    glues = Glue.objects.all()

    # Serialize the queryset to JSON
    serialized_glues = [
        {
            'modelname': glue.modelname,
            'content': str(glue.content),
            'count': glue.count,
        }
        for glue in glues
    ]

    # Return JSON response
    return JsonResponse(serialized_glues, safe=False)
