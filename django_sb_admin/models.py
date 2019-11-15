from django.db import models

# Create your models here.

from django.db import models

class Applicants (models.Model):
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    pending = models.BooleanField(default = True)