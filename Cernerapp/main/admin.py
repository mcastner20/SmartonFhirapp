from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Information, Conditions, Demographics, Disaster, Hazards, Hazard_continued, Hazard_probability
# Register your models here.
admin.site.register(Information)
admin.site.register(Conditions)
admin.site.register(Demographics)
admin.site.register(Disaster)
admin.site.register(Hazards)
admin.site.register(Hazard_continued)
admin.site.register(Hazard_probability)