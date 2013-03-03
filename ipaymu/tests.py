from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from ipaymu.forms import IpaymuForm
from ipaymu.models import IpaymuSessionID
from ipaymu.utils import save_session, verify_session, IpaymuParamsBuilder


class IpaymuTest(TestCase):

    fixtures = ['ipaymu/fixtures/sessionID.json',]
    
    def setUp(self):
        self.c = Client()
        self.good_sessid = 'ad05fd717b3bb836519df7c430f0db0801d347b34ea28e4f15bc6213b9f95772ff882808442e1a5275715f2895f3db8adbd95105147e9f0856c4c5ad7de24bab'
        self.junk_sessid = 'this-sesssion-not-exists-in-database'

    def test_forms(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_urls(self):

        # Test canceled page
        resp = self.c.get(reverse('ipaymu_cancel_url'))
        self.assertEqual(resp.status_code, 200)

        # Test return page
        resp = self.c.get(reverse('ipaymu_return_url'))
        self.assertEqual(resp.status_code, 200)

        # Test process url - GET
        resp = self.c.get(reverse('ipaymu_process_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, 'Invalid request.')

        # Test process url - POST
        # No data posted, will return invalid field.
        resp = self.c.post(reverse('ipaymu_process_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('valid' in resp.content)

        # Test process url - POST
        # With valid data, will redirected to Ipaymu
        # resp = self.c.post(reverse('ipaymu_process_url'), {
        #         'product': 'test product',
        #         'quantity': 1,
        #         'price': 5000,
        #         'comments': 'this is comments',
        #     })
        # self.assertEqual(resp.status_code, 302)

        # Test notify url - GET
        resp = self.c.get(reverse('ipaymu_notify_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, '')

        # Test notify url - POST
        resp = self.c.post(reverse('ipaymu_notify_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, '')

    def test_functions(self):

        # Test verify_session
        verified = verify_session(self.good_sessid)
        self.assertEqual(verified, True)

        verified = verify_session(self.junk_sessid)
        self.assertEqual(verified, False) 

        # Test save_session
        save_session(self.junk_sessid)
        try:
            sess = IpaymuSessionID.objects.get(sessid=self.junk_sessid)
        except IpaymuSessionID.DoesNotExist:
            raise
        else:
            self.assertEqual(sess.sessid, self.junk_sessid)
