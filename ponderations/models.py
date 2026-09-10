from django.db import models

from delegations.models import BaseModel

class Device(BaseModel):
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.PROTECT,
        related_name="ponderations",
    )
    name = models.CharField(max_length=120)
    serial_number = models.CharField(max_length=80, unique=True)
