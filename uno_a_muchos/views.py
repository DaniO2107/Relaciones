from django.shortcuts import render
from django.http import HttpResponse
from  .models import Reporter, Article
from datetime import date

def inicio(request):

  reporte = Reporter(name='Jose', last_name ='Ojeda',email="ojedadaniel178@gmail.com", id= '1')
  reporte.save()
  reporte = Reporter.objects.get(id=1)

  # report1 = Article(title='Ella y yo', pub_date=date(2004, 7, 14),reporter=reporte)

  # report2 = Article(title="Yo y Ella", pub_date=date(2004,7,24), reporter=reporte)

  # report1.save()
  # report2.save()
  eliminar = Article.objects.get(id=1)
  eliminar.update()

  



  # restaurate1 = Restaurant(place=place1, employess = 3)
  # restaurate1.save()
  return HttpResponse('WASAAAAA')

