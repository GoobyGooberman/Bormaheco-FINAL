from django.test import TestCase
from .models import Equipment
# Create your tests here.
class EquipmentTest(TestCase):
    def TestEquipment(self):
        brand = Equipment.details.get()
        name = Equipment.details.get()
        cost = Equipment.details.get()
        date = Equipment.details.get()
        details = Equipment.details.get()
        type = Equipment.details.get()
