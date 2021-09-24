from django.test import TestCase
from api.utils import external_vin_decoder


class ExternalVINDecoderTest(TestCase):

    def test_decoder(self):

        self.assertDictEqual({}, external_vin_decoder.decode('11111121212'))
        self.assertDictEqual({}, external_vin_decoder.decode(11111121212))
        self.assertEqual("CHRYSLER", external_vin_decoder.decode("2C4RC1DG3HR711964")['make'])
