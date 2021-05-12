from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    # khởi tạo một post để test
    def setUp(self):
        Post.objects.create(title='myTitle',body='Just a Test')
    # kiểm tra xem hàm str có chạy đúng không
    def test_string_representation(self):
        post=Post(title='My entry title')
        self.assertEqual(str(post),post.title)
    # Kiểm tra xem response có lấy template trong blog
    def test_post_list_view(self):
        response=self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response,'blog/blog.html')
    # Kiểm tra xem chi tiết của Post khi NSD chọn vào blog Id=1
    def test_post_detail_view(self):
        response=self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response,'blog/post.html')

