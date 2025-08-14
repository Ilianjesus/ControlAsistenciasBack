#After this file will be updated to include rols and permissions 

from rest_framework import viewsets
from .models import Usuario, Joven, Evento, Asistencia
from .serializers import UsuarioSerializer, JovenSerializer, EventoSerializer, AsistenciaSerializer

# ----------------------------
# 1. UsuarioViewSet
# ----------------------------
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# ----------------------------
# 2. JovenViewSet
# ----------------------------
class JovenViewSet(viewsets.ModelViewSet):
    queryset = Joven.objects.all()
    serializer_class = JovenSerializer

# ----------------------------
# 3. EventoViewSet
# ----------------------------
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# ----------------------------
# 4. AsistenciaViewSet
# ----------------------------
class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
