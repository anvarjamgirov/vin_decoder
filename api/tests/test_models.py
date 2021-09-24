from django.test import TestCase

from api.models import VIN


class VINModelTest(TestCase):

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

    def test_str(self):
        vin: VIN = VIN.objects.get(vin_code="2C4RC1DG3HR711964")
        self.assertEqual("PACIFICA", str(vin))
