from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,

        on_delete=models.CASCADE,
       
        primary_key=True,
    )
    employess=models.IntegerField(default=1)


# class Place():
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)


# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,

#         on_delete=models.CASCADE,
       
#         primary_key=True,
#     )
#     employess=models.IntegerField(default=1)
