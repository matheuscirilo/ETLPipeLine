# importa a classe que vai ser testada
from .http_requester import HttpRequester

#cria uma classe de teste
def test_request_from_page(requests_mock):
    #executa os métodos dentro da classe utilizado o pytest
    # comando dado na pasta ETLPipeLine -> pytest -s -v src/drivers/http_requester_test.py

    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    response_context = '<h1.OlaMundo</h1>'
    requests_mock.get(url, status_code=200, text=response_context)

    #cria uma instância da classe
    http_requester = HttpRequester()

    request_response = http_requester.request_from_page()
    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == response_context