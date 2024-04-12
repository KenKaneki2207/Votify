from django.contrib import admin
from voting.models import Election, vote
# Register your models here.

admin.site.register(Election)
admin.site.register(vote)