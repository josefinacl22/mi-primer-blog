from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Albumes(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    artista = models.TextField()
    lanzamiento = models.DateField()
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    genero = models.TextField()
    duracion_album = models.TextField()
    productores = models.TextField()
    canciones = models.TextField()
    reproducciones_diarias = models.TextField()
    reconocimiento = models.TextField()
    premio_grammy = models.TextField(blank=True, null=True)
    observacion = models.TextField()
    resena_personal = models.TextField()
    otro = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
