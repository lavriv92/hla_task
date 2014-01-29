from django.test import TestCase


class PublicTest(TestCase):

    def int_test(self):
        self.assertEquals(1 + 1, 2)
