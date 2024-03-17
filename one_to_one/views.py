from django.shortcuts import render
from django.http import HttpResponse
from  .models import Place, Restaurant

# def inicio(request):
#   place1 = Place(name='Gironcity', address="Gironcity carrera menorcito ptte")
#   place1.save()

#   restaurate1 = Restaurant(place=place1, employess = 3)
#   restaurate1.save()

#   restaurante = Restaurant.objects.get(place_id=9)
#   print(restaurante.place.address)

#   return HttpResponse('Hola')


def update(request, id, name):
    actualizar = Place.objects.get(id = id)
    actualizar.name = name
    actualizar.save()
    return HttpResponse('Se actualizo de Gironcity a Giron')

# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)


# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,

#         on_delete=models.CASCADE,
       
#         primary_key=True,
#     )
#     employess=models.IntegerField(default=1)


