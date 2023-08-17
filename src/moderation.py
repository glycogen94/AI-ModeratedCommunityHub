## moderation.py
from django.http import JsonResponse
from .models import Moderation

def review_moderation(request, moderation_id):
    if request.method == 'PUT':
        data = request.POST
        status = data.get('status')
        if not status:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        try:
            moderation = Moderation.objects.get(id=moderation_id)
        except Moderation.DoesNotExist:
            return JsonResponse({'error': 'Moderation not found'}, status=404)
        moderation.status = status
        moderation.save()
        return JsonResponse({'message': 'Moderation reviewed successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def approve_moderation(request, moderation_id):
    if request.method == 'PUT':
        try:
            moderation = Moderation.objects.get(id=moderation_id)
        except Moderation.DoesNotExist:
            return JsonResponse({'error': 'Moderation not found'}, status=404)
        moderation.approve()
        return JsonResponse({'message': 'Moderation approved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def reject_moderation(request, moderation_id):
    if request.method == 'PUT':
        try:
            moderation = Moderation.objects.get(id=moderation_id)
        except Moderation.DoesNotExist:
            return JsonResponse({'error': 'Moderation not found'}, status=404)
        moderation.reject()
        return JsonResponse({'message': 'Moderation rejected successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
