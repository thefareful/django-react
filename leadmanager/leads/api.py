from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# lead viewset
class LeadViewSet(viewsets.ModelViewSet):
    querqset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer