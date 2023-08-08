from django.db import models
from django.urls import reverse

class Client(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("reportapp_Client_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("reportapp_Client_update", args=(self.pk,))


class ReportType(models.Model):
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Report Types'

    def __str__(self):
        return str(self.name)


class Input(models.Model):
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=500)
    report_day = models.IntegerField()
    am_email = models.CharField(max_length=500)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Input Data'

    def __str__(self):
        return str(self.client.name)    


class Job(models.Model):
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='draft') #Can be draft, success, failed
    url = models.CharField(max_length=500)
    report_day = models.IntegerField()
    am_email = models.CharField(max_length=500)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=500, blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    run_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Jobs'

    def __str__(self) -> str:
        return self.client.name


class SMTPConfig(models.Model):

    # Fields
    sender_name = models.CharField(max_length=100)
    port = models.IntegerField()
    username = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    server = models.CharField(max_length=100)
    bcc = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    is_enable = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'SMTP Settings'
        
    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("reportapp_SMTPConfig_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("reportapp_SMTPConfig_update", args=(self.pk,))



class AWSConfig(models.Model):

    # Fields
    aws_access_key_id = models.CharField(max_length=100)
    aws_secret_access_key = models.CharField(max_length=200)
    output_path = models.CharField(max_length=200)
    local_path = models.CharField(max_length=200)   
    bucket_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    input_field_path = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    is_enable = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'AWS Settings'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("reportapp_AWSConfig_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("reportapp_AWSConfig_update", args=(self.pk,))
