from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Community, Discussion, Comment


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username or not email or not password:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        user = User.objects.create(username=username, email=email, password=password)
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }, status=201)
    else:
        users = User.objects.all()
        return JsonResponse([{
            'id': user.id,
            'username': user.username,
            'email': user.email
        } for user in users], safe=False)


@csrf_exempt
def create_community(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        if not name or not description:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        community = Community.objects.create(name=name, description=description)
        return JsonResponse({
            'id': community.id,
            'name': community.name,
            'description': community.description
        }, status=201)
    else:
        communities = Community.objects.all()
        return JsonResponse([{
            'id': community.id,
            'name': community.name,
            'description': community.description
        } for community in communities], safe=False)


@csrf_exempt
def create_discussion(request):
    if request.method == 'POST':
        data = request.POST
        community_id = data.get('community_id')
        title = data.get('title')
        content = data.get('content')
        if not community_id or not title or not content:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        try:
            community = Community.objects.get(id=community_id)
        except Community.DoesNotExist:
            return JsonResponse({'error': 'Community not found'}, status=404)
        discussion = community.create_discussion(title=title, content=content)
        return JsonResponse({
            'id': discussion.id,
            'title': discussion.title,
            'content': discussion.content
        }, status=201)
    else:
        discussions = Discussion.objects.all()
        return JsonResponse([{
            'id': discussion.id,
            'title': discussion.title,
            'content': discussion.content
        } for discussion in discussions], safe=False)


@csrf_exempt
def create_comment(request):
    if request.method == 'POST':
        data = request.POST
        discussion_id = data.get('discussion_id')
        user_id = data.get('user_id')
        content = data.get('content')
        if not discussion_id or not user_id or not content:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        try:
            discussion = Discussion.objects.get(id=discussion_id)
        except Discussion.DoesNotExist:
            return JsonResponse({'error': 'Discussion not found'}, status=404)
        comment = discussion.create_comment(user_id=user_id, content=content)
        return JsonResponse({
            'id': comment.id,
            'user_id': comment.user_id,
            'content': comment.content
        }, status=201)
    else:
        comments = Comment.objects.all()
        return JsonResponse([{
            'id': comment.id,
            'user_id': comment.user_id,
            'content': comment.content
        } for comment in comments], safe=False)
