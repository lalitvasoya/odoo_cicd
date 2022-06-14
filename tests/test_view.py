

class TestFlaskRoute:

    def test_status_success(self, client):
        response = client.get('/status')
        assert response.json['status'] == "CICD"
        assert response.status == '200 OK'

    def test_factorial_5_success(self, client):
        response = client.get('/fact', query_string={'no': 5})
        assert response.json['fact'] == 120
        assert response.status == '200 OK'

    def test_factorial_4_success(self, client):
        response = client.get('/fact', query_string={'no': 4})
        assert response.json['fact'] == 24
        assert response.status == '200 OK'

    def test_factorial_6_success(self, client):
        response = client.get('/fact', query_string={'no': 6})
        assert response.json['fact'] == 72
        assert response.status == '200 OK'
