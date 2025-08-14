from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Usuario, Joven, Evento, Asistencia
from django.urls import reverse
from datetime import date

class AsistenciasAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Crear usuario administrador
        self.admin = Usuario.objects.create(
            nombre="Admin Test",
            email="admin@test.com",
            contraseña="admin123",
            rol="administador"
        )

        # Crear usuario entrenador
        self.entrenador = Usuario.objects.create(
            nombre="Entrenador Test",
            email="entrenador@test.com",
            contraseña="entrenador123",
            rol="entrenador"
        )

        # Crear un joven
        self.joven = Joven.objects.create(
            nombre="Joven Test",
            fecha_nacimiento=date(2010, 1, 1),
            fecha_ingreso=date(2023, 1, 1),
            tipo_sangre="O+",
            alergias="Ninguna",
            grupo="Grupo A",
            qr_codigo="QR12345",
            tutor_nombre="Tutor Test",
            tutor_telefono="1234567890"
        )

        # Crear evento
        self.evento = Evento.objects.create(
            nombre="Entrenamiento Test",
            fecha=date(2025, 8, 15),
            lugar="Cancha Principal",
            descripcion="Entrenamiento semanal",
            creado_por=self.admin
        )

    # ----------------------------
    # Prueba CRUD Usuario
    # ----------------------------
    def test_list_usuarios(self):
        url = reverse('usuario-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ----------------------------
    # Prueba CRUD Joven
    # ----------------------------
    def test_create_joven(self):
        url = reverse('joven-list')
        data = {
            "nombre": "Nuevo Joven",
            "fecha_nacimiento": "2011-05-10",
            "fecha_ingreso": "2025-01-01",
            "tipo_sangre": "A+",
            "alergias": "",
            "grupo": "Grupo B",
            "qr_codigo": "QR67890",
            "tutor_nombre": "Tutor Nuevo",
            "tutor_telefono": "0987654321"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Joven.objects.count(), 2)

    # ----------------------------
    # Prueba CRUD Evento
    # ----------------------------
    def test_list_eventos(self):
        url = reverse('evento-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ----------------------------
    # Prueba CRUD Asistencia
    # ----------------------------
    def test_create_asistencia(self):
        url = reverse('asistencia-list')
        data = {
            "joven_id": self.joven.id,
            "evento_id": self.evento.id,
            "registrado_por_id": self.entrenador.id,
            "tipo": "escaneado",
            "ubicacion": "Cancha Principal"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Asistencia.objects.count(), 1)
