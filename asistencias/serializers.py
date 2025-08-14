from rest_framework import serializers
from .models import Usuario, Joven, Evento, Asistencia

# ----------------------------
# 1. UsuarioSerializer
# ----------------------------
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'contraseña': {'write_only': True}  # No mostrar contraseña en respuestas
        }

# ----------------------------
# 2. JovenSerializer
# ----------------------------
class JovenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joven
        fields = '__all__'

# ----------------------------
# 3. EventoSerializer
# ----------------------------
class EventoSerializer(serializers.ModelSerializer):
    creado_por = UsuarioSerializer(read_only=True)

    class Meta:
        model = Evento
        fields = '__all__'

# ----------------------------
# 4. AsistenciaSerializer
# ----------------------------
class AsistenciaSerializer(serializers.ModelSerializer):
    joven = JovenSerializer(read_only=True)
    evento = EventoSerializer(read_only=True)
    registrado_por = UsuarioSerializer(read_only=True)

    joven_id = serializers.PrimaryKeyRelatedField(
        queryset=Joven.objects.all(), source='joven', write_only=True
    )
    evento_id = serializers.PrimaryKeyRelatedField(
        queryset=Evento.objects.all(), source='evento', write_only=True
    )
    registrado_por_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), source='registrado_por', write_only=True
    )

    class Meta:
        model = Asistencia
        fields = [
            'id', 'joven', 'evento', 'registrado_por', 'fecha_hora',
            'tipo', 'ubicacion', 'joven_id', 'evento_id', 'registrado_por_id'
        ]
