from django.db import models

# la definicion de los modelos creados

    
class Comentario(models.Model):
    comentario = models.CharField(max_length=40) #comentario = models.ForeignKey(Novedad, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)