from rest_framework import viewsets, permissions
from .models import Video, User, Follow, Like, Earning
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-created_at')
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        video = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, video=video)
        return Response({'status': 'liked'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        target_user = self.get_object()
        Follow.objects.get_or_create(follower=request.user, following=target_user)
        return Response({'status': 'followed'})

class EarningViewSet(viewsets.ModelViewSet):
    queryset = Earning.objects.all()
    serializer_class = EarningSerializer
