from rest_framework.routers import DefaultRouter
from blog.api.views import BlogApiViewSet

router_post = DefaultRouter()

router_post.register(prefix='blog', basename='blog', viewset=BlogApiViewSet)
