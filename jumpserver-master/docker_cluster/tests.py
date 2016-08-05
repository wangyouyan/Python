from django.test import TestCase

# Create your tests here.
import pykube
import operator


api = pykube.HTTPClient(pykube.KubeConfig.from_service_account())