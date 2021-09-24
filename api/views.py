from django.http import HttpRequest
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.models import VIN
from api.utils.external_vin_decoder import decode


class VINDecodeAPIView(APIView):
    """
    Retrieve a VIN data
    """

    @swagger_auto_schema(
        query_serializer=serializers.VINDecodeRequestSerializer(),
        responses={
            status.HTTP_200_OK: serializers.VINDecodeResponseSerializer(),
            status.HTTP_404_NOT_FOUND: "Not Found",
            status.HTTP_400_BAD_REQUEST: "This field may not be blank."
        },
        operation_description='Use this method to decode VIN by VIN number',
        operation_summary='VIN Decoder'
    )
    def get(self, request: HttpRequest, *args, **kwargs):
        serializer = serializers.VINDecodeRequestSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        vin_code = serializer.validated_data.get('vin_code')

        try:
            vin: VIN = VIN.objects.get(vin_code=vin_code)
        except VIN.DoesNotExist:
            decoded_data: dict = decode(vin_code)
            if decoded_data:
                vin: VIN = VIN.objects.create(
                    vin_code=vin_code,
                    **decoded_data
                )
            else:
                vin = None
        if vin:
            response_serializer = serializers.VINDecodeResponseSerializer(instance=vin)
            return Response(data=response_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
