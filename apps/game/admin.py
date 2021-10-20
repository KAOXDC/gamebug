from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Card_Type)
admin.site.register(Card)
admin.site.register(Player)
admin.site.register(Turn)
admin.site.register(Game)
admin.site.register(Registred)
admin.site.register(Board)

