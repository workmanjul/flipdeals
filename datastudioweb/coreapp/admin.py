from django.contrib import admin
from .models import Client, ReportType, Input, Job, SMTPConfig, AWSConfig
# Register your models here.


admin.site.register(ReportType)
admin.site.register(SMTPConfig)
admin.site.register(AWSConfig)
admin.site.register(Client)
# admin.site.register(Input)
# admin.site.register(Job)