from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import User, Community, Discussion, Comment
from serializers import UserSerializer, CommunitySerializer, DiscussionSerializer, CommentSerializer

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
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=201)
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_community(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        if not name or not description:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
        community = Community.objects.create(name=name, description=description)
        serializer = CommunitySerializer(community)
        return JsonResponse(serializer.data, status=201)
    else:
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return JsonResponse(serializer.data, safe=False)

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
        serializer = DiscussionSerializer(discussion)
        return JsonResponse(serializer.data, status=201)
    else:
        discussions = Discussion.objects.all()
        serializer = DiscussionSerializer(discussions, many=True)
        return JsonResponse(serializer.data, safe=False)

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
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data, status=201)
    else:
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
