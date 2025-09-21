# Register your models here.
from django.contrib import admin
from .models import Member, Plan, Trainer

admin.site.register(Member)
admin.site.register(Plan)
admin.site.register(Trainer)
