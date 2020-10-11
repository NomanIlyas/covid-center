from datetime import datetime
from pytz import utc
from django.core.management.base import BaseCommand
from django.utils import timezone
from frontend import views

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response = views.importCountries()
        print("execute from outside")
        self.stdout.write("Counties data have been imported Now: %s" % response)
def handle():
    response = views.importCountries()
    print("execute from outside")
    # self.stdout.write("Counties data have been imported Now: %s" % response)
print("I am executed..! outside")

