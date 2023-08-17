## tests.py
import unittest
from django.test import Client
from .models import User, Community, Discussion, Comment


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_user(self):
        response = self.client.post('/api/users/', {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertIsInstance(users, list)

    def test_create_community(self):
        response = self.client.post('/api/communities/', {
            'name': 'Test Community',
            'description': 'This is a test community'
        })
        self.assertEqual(response.status_code, 201)
        community = Community.objects.get(name='Test Community')
        self.assertEqual(community.description, 'This is a test community')

    def test_get_communities(self):
        response = self.client.get('/api/communities/')
        self.assertEqual(response.status_code, 200)
        communities = response.json()
        self.assertIsInstance(communities, list)

    def test_create_discussion(self):
        community = Community.objects.create(name='Test Community', description='This is a test community')
        response = self.client.post('/api/discussions/', {
            'community_id': community.id,
            'title': 'Test Discussion',
            'content': 'This is a test discussion'
        })
        self.assertEqual(response.status_code, 201)
        discussion = Discussion.objects.get(title='Test Discussion')
        self.assertEqual(discussion.content, 'This is a test discussion')

    def test_get_discussions(self):
        response = self.client.get('/api/discussions/')
        self.assertEqual(response.status_code, 200)
        discussions = response.json()
        self.assertIsInstance(discussions, list)

    def test_create_comment(self):
        discussion = Discussion.objects.create(community_id=1, title='Test Discussion', content='This is a test discussion')
        response = self.client.post('/api/comments/', {
            'discussion_id': discussion.id,
            'user_id': 1,
            'content': 'This is a test comment'
        })
        self.assertEqual(response.status_code, 201)
        comment = Comment.objects.get(content='This is a test comment')
        self.assertEqual(comment.user_id, 1)

    def test_get_comments(self):
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, 200)
        comments = response.json()
        self.assertIsInstance(comments, list)


if __name__ == '__main__':
    unittest.main()
