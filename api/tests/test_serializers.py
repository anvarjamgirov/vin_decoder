from django.test import TestCase
from rest_framework.exceptions import ValidationError

from api.models import VIN
from api.serializers import VINDecodeRequestSerializer, VINDecodeResponseSerializer


class VINDecodeRequestSerializerTest(TestCase):

    def test_input_data(self):

        serializer = VINDecodeRequestSerializer(data={})

        self.assertRaises(ValidationError, serializer.is_valid, raise_exception=True)


class VINDecodeResponseSerializerTest(TestCase):
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

    def test_output_data(self):
        vin: VIN = VIN.objects.get(vin_code="2C4RC1DG3HR711964")

        serializer_1 = VINDecodeResponseSerializer(vin)
        serializer_2 = VINDecodeResponseSerializer()

        self.assertEqual(serializer_1.data.get('make'), vin.make)
        self.assertEqual('', serializer_2.data.get('make'))
