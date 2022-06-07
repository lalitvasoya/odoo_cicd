

class TestFlaskRoute:

    def test_status_success(self, client):
        response = client.get('/status')
        assert response.json['status'] == 'Flask with CICD ****************"})'
        assert response.status == '200 OK'

    def test_factorial_success(self, client):
        response = client.get('/fact', query_string={'no': 5})
        assert response.json['fact'] == 120
        assert response.status == '200 OK'

    def test_factorial_second_success(self, client):
        response = client.get('/fact', query_string={'no': 6})
        assert response.json['fact'] == 720
        assert response.status == '200 OK'

    def test_factorial_third_success(self, client):
        response = client.get('/fact', query_string={'no': 6})
        assert response.json['fact'] == 720
        assert response.status == '200 OK'

    def test_factorial_fourth_success(self, client):
        response = client.get('/fact', query_string={'no': 6})
        assert response.json['fact'] == 720
        assert response.status == '200 OK'
