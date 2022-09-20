from django.contrib import admin

from home.models import Fruits

# Register your models here.
from .models import *

admin.site.register(Fruits)