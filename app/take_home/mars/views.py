from api_clients.nasa_client import MarsImageLinkList, nasa_client
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics
from rest_framework.response import Response
from take_home.mars.serializers import RetrieveMarsPhotosSerializer


@extend_schema(tags=["Mars Rover"])
class MarsPhotosGenericAPIView(generics.GenericAPIView):
    throttle_classes = []
    serializer_class = RetrieveMarsPhotosSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="camera",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Select camera by name",
                required=True,
            ),
            OpenApiParameter(
                name="earth_date",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="Retrieve mars photo by earth date",
                required=True,
            ),
            OpenApiParameter(
                name="page_number",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="Select page number",
                required=False,
            ),
        ],
        responses={"200": MarsImageLinkList},
    )
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        response = nasa_client.get_mars_photos(**serializer.data)
        return Response(response.model_dump())
