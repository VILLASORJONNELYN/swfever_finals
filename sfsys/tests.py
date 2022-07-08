from django.urls import resolve
from django.test import TestCase
from sfsys.views import swfever
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import swinefever 


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'swfever.html')


class ORMtest(TestCase):
	def test_saving_models_retrieve(self):
		user = UserOne()
		user.surname = 'Villasor'
		user.firstname = 'Jonnelyn'
		user.middleInitial ='C'
		user.email = 'jonnelyn.villasor@gsfe.tupcavite.edu.ph'
		user.date = '2022-06-25'
		user.region = 'REGION4A'
		user.save()


		



