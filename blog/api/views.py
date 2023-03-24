from rest_framework.viewsets import ModelViewSet
from blog.models import Blog
from blog.api.serializers import BlogSerializer

class BlogApiViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

