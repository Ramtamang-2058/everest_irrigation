from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from everest_broker.models import ReceivedData
from .serializers import LatestReceivedDataSerializer


class LatestReceivedDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        latest_entry = ReceivedData.objects.last()
        if latest_entry:
            serializer = LatestReceivedDataSerializer(latest_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No data available'}, status=status.HTTP_404_NOT_FOUND)
