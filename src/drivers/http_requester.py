import requests
from typing import Dict
from .interfaces.http_requester import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):

    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    # faz o get da url especificada no __init__ e retorna um dicionário com status e o html
    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url)

        #cria um dicionário com as repostas desejadas
        return{
            "status_code": response.status_code,
            "html": response.text
        }