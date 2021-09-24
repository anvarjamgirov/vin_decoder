from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import VIN
from api.serializers import VINDecodeResponseSerializer


class VINDecoderAPIViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        VIN.objects.create(
            vin_code="2C4RC1DG3HR711964",
            make="CHRYSLER",
            model="PACIFICA",
            year="2017",
            manufacturer="CHRYSLER",
            engine="V6, 3.6L; DOHC; 24V; SEFI; FFV",
            trim="TOURING",
            transmission="AUTOMATIC",
        )

    def test_vin_decoder_get(self):
        vin: VIN = VIN.objects.get(vin_code="2C4RC1DG3HR711964")
        url = reverse('vin-decoder')

        response_1 = self.client.get(url, {'vin_code': "2C4RC1DG3HR711964"})
        response_2 = self.client.get(url, {'vin_code': 123456})
        response_3 = self.client.get(url)

        serializer = VINDecodeResponseSerializer(instance=vin)

        self.assertEqual(status.HTTP_200_OK, response_1.status_code)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response_2.status_code)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response_3.status_code)

        self.assertEqual(response_1.data, serializer.data)
