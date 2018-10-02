from django.test import TestCase
from .models import UserAccount

# Create your tests here.
class UserAccountTest(TestCase):
    def TestsetName(self):
        UserAccount.company.create(name = "admin", pswd = "dlsu1234")



    def TestshowName(self):
        admin = UserAccount.company.get(name="admin")
        dlsu = UserAccount.company.get(pswd = "dlsu1234")
        self.assertEqual(admin.speak(), "admin")
        self.assertEqual(admin.pswd(), "dlsu1234")

