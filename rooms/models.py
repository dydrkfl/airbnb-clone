from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
# 순서는 django -> third party -> myapp


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """
    name = models.CharField(max_length=80)
    # name = models.CharField(max_length=100)

    class Meta:
        abstract: True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Object Definition """
    class Meta:
        verbose_name = "Room Type"
        # ordering = ['name']


class Amenity(AbstractItem):
    """ Amenity Object Definition """
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Model Definition """
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ Houserule Model Definition """
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    # Room으로 쓰면 파이썬의 읽는 방식에 의해 에러발생. foreignkey는 "" 형식을 사용가능

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE)
    # room과 user를 connect / many to one relation : many rooms -> user
    # on_delete의 옵션은 다음의 사이트에서 확인 https://brunch.co.kr/@ddangdol/5
    room_type = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
