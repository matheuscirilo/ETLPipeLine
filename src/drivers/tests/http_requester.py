from typing import Dict

class HttpRequesterSpy:

    def __init__(self) -> None:
        self.request_from_page_count = 0

    # faz o get da url especificada no __init__ e retorna um dicionário com status e o html
    def request_from_page(self) -> Dict[int, str]:
        self.request_from_page_count += 1
        return{
            "status_code": 200,
            "html": "<h1>TesteSpy</h1>"
        }