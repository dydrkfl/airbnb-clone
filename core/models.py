from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """ Time Stamped Model """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # abstract 는 db에 저장되는 것이 아니라 우리가 사용하기 위해 쓰는 data
