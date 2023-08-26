from rest_framework import viewsets, permissions
from .serializers import ProfileSerilizer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerilizer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
