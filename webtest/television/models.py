#https://medium.com/@4yub1k/free-deploy-django-project-to-pythonanywhere-1f3f08a6447f
from django.db import models
import mssql_python

# Create your models here.
class Serie:
    def __init__(self):
        self.idSerie = 0
        self.nombre = ""
        self.imagen = ""
        self.anyo = 0

class ServiceSeries:
    def __init__(self):
        self.connection = mssql_python.connect('Server=sqlpaco3430.database.windows.net;Database=AZURETAJAMAR;Encrypt=yes;UID=adminsql;PWD=Admin123;TrustServerCertificate=yes')

    def getSeries(self):
        cursor = self.connection.cursor()
        sql = "select * from SERIES"
        cursor.execute(sql)
        listaSeries = []
        for row in cursor:
            ser = Serie()
            ser.idSerie = row[0]
            ser.nombre = row[1]
            ser.imagen = row[2]
            ser.anyo = row[3]
            listaSeries.append(ser)
        cursor.close()
        return listaSeries