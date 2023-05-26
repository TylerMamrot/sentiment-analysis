import pytest
from main import app
from routers import predict
from routers.prediction import Prediction, Inference
from fastapi.testclient import TestClient
from mock import patch, Mock

test_app = TestClient(app)


@pytest.fixture
def inference_fixture():
    return {"text":"some inference"}




@patch('routers.p.get_model')
def test_predict(mock_get_model, inference_fixture):
    mock_model = Mock()
    mock_model.predict.return_value = 1
    mock_get_model.return_value = mock_model
    response = test_app.post(url="/predict/", json=inference_fixture)
    assert response.status_code == 200
    assert response.json() == {"prediction": "positive"}
