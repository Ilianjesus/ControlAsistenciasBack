from django.db import models

class Usuario (models.Model):
    ROLES = [
        ('administador', 'Administrador'),
        ('entrenador', 'Entrenador'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
    

class Joven(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    tipo_sangre = models.CharField(max_length=5)
    alergias = models.TextField(blank=True, null=True)
    grupo = models.CharField(max_length=50, unique=True)
    qr_codigo = models.CharField(max_length=255)
    tutor_nombre = models.CharField(max_length=100)
    tutor_telefono = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Joven"
        verbose_name_plural = "Jovenes"

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_creados')

    def __str__(self):
        return self.nombre
    

class Asistencia(models.Model):
    TIPO_CHOICES = [
        ('escaneado', 'Escaneado'),
        ('manual', 'Manual'),
        ('justificado', 'Justificado'),
    ]

    id = models.AutoField(primary_key=True)
    joven = models.ForeignKey(Joven, on_delete=models.CASCADE, related_name='asistencias')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='asistencias')
    registrado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='asistencias_registradas')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Asistencia de {self.joven.nombre} a {self.evento.nombre}"
    
    