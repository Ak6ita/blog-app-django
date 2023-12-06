from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.conf import settings
from rest_framework.response import Response

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_openai_key(request):
    return Response({'key': settings.OPENAI_SECRET_KEY}, status=200)