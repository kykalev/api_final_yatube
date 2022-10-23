from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/groups', GroupViewSet)
router_v1.register(
    r'^v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
router_v1.register('v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
]
