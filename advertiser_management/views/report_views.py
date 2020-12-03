from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.utils import timezone, dateparse

from advertiser_management.models import Ad
from advertiser_management.serializers import AdSerializer, AdCTRSerializer, AdEstimationSerializer


class GetTimeMixin:
    def get_time(self):
        current_time = timezone.now()
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')

        if isinstance(start_time, str):
            start_time = dateparse.parse_datetime(start_time) or current_time

        if isinstance(end_time, str):
            end_time = dateparse.parse_datetime(end_time) or current_time

        return start_time, end_time


class ReportViewSet(ReadOnlyModelViewSet, GetTimeMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    @action(detail=False, description='shows ctr')
    def get_ctr(self, _):
        start_time, end_time = self.get_time()
        queryset = Ad.get_total_ctr(start_time, end_time)
        serializer = AdCTRSerializer(queryset, many=True)
        return Response(
            serializer.data
        )

    @action(detail=False, description='shows estimation')
    def get_duration(self, _):
        queryset = self.get_queryset()
        serializer = AdEstimationSerializer(queryset, many=True)
        return Response(
            serializer.data
        )

    @action(detail=False, description='shows total clicks views')
    def get_total_info(self, request):
        start_time, end_time = self.get_time()
        delta = int(request.query_params.get('delta'))
        ads = Ad.get_total_clicks_views(start_time, end_time, delta)
        return Response(
            ads.values()
        )
