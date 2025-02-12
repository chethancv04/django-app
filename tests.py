import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import YourModel
from .serializers import YourModelSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_model_instance(db):
    return YourModel.objects.create(
        field1='Chethan',
        field2='Yogitha',
        # Add other fields as required
    )

@pytest.mark.django_db
class TestYourModelAPI:
    
    def test_create_instance(self, api_client):
        url = reverse('yourmodel-list')
        data = {
            'field1': 'Chethan',
            'field2': 'Yogitha',
            # Add other fields as required
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert YourModel.objects.count() == 1
    
    def test_get_instance(self, api_client, create_model_instance):
        url = reverse('yourmodel-detail', args=[create_model_instance.id])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        serializer = YourModelSerializer(create_model_instance)
        assert response.data == serializer.data

    def test_update_instance(self, api_client, create_model_instance):
        url = reverse('yourmodel-detail', args=[create_model_instance.id])
        data = {
            'field1': 'Updated Chethan',
            'field2': 'Updated Yogitha',
            # Add other fields as required
        }
        response = api_client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        create_model_instance.refresh_from_db()
        assert create_model_instance.field1 == 'Updated Chethan'
    
    def test_delete_instance(self, api_client, create_model_instance):
        url = reverse('yourmodel-detail', args=[create_model_instance.id])
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert YourModel.objects.count() == 0
