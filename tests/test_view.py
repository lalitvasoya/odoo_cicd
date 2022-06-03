

class TestFlaskRoute:

    def test_status_success(self, client):
        response = client.get('/status')
        assert response.json['status'] == 'Flask testing!'
        assert response.status == '200 OK'

    def test_factorial_success(self, client):
        response = client.get('/fact', query_string={'no': 5})
        assert response.json['fact'] == 1220
        assert response.status == '200 OK'
