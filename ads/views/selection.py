from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.serializers import SelectionListSerializer, SelectionDetailSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.order_by('-price')
    default_serializer = SelectionDetailSerializer
    serializer_classes = {
        'list': SelectionListSerializer
    }
    default_permission = [AllowAny()]
    permissions = {
        'retrieve': [IsAuthenticated],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)