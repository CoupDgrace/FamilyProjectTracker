from django.contrib import admin
from .models import Members
from .models import Tasks
from .models import taskNotes

# Register your models here.
admin.site.register(Members)
admin.site.register(Tasks)
admin.site.register(taskNotes)


