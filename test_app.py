import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Valida que la ruta raíz responda exitosamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"operando de forma segura" in response.data  # Buscamos esta frase sin acentos

def test_health_endpoint(client):
    """Valida el endpoint de salud del sistema"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"UP" in response.data

def test_metrics_endpoint(client):
    """Valida la disponibilidad de métricas para Prometheus"""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"app_uptime_seconds" in response.data

def test_api_suma(client):
    """Valida la lógica matemática del endpoint de suma"""
    response = client.get('/api/v1/suma/10/15')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["resultado"] == 25