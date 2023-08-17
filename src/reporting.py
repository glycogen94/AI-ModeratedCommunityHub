## reporting.py
from django.http import JsonResponse
from .models import User, Report


def report_content(request):
    if request.method == 'POST':
        data = request.POST
        user_id = data.get('user_id')
        content_id = data.get('content_id')
        reason = data.get('reason')
        if not user_id or not content_id or not reason:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        Report.objects.create(user=user, content_id=content_id, reason=reason)
        return JsonResponse({'message': 'Content reported successfully'}, status=201)
    else:
        reports = Report.objects.all()
        return JsonResponse([{
            'id': report.id,
            'content_id': report.content_id,
            'reason': report.reason,
            'status': report.status
        } for report in reports], safe=False)


def resolve_report(request, report_id):
    if request.method == 'PUT':
        data = request.POST
        status = data.get('status')
        if not status:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        try:
            report = Report.objects.get(id=report_id)
        except Report.DoesNotExist:
            return JsonResponse({'error': 'Report not found'}, status=404)
        report.status = status
        report.save()
        return JsonResponse({'message': 'Report resolved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
