from django.db import models

# la definicion de los modelos creados

class Novedad(models.Model):
    novedadSeleccion = (
    ('roja','Roja'),
    ('amarilla', 'Amarilla'),
    ('azul','Azul'),
    ('verde','Verde'),
    )
    usuario = models.CharField(max_length=200) #debería ser  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    sala = models.CharField(max_length=15, choices=novedadSeleccion, default='azul')
    descripcion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
    