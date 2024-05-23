from src.drivers.tests.http_requester import HttpRequesterSpy
from src.drivers.tests.html_collector import HtmlCollectorSpy
from src.stages.extract.extract_html import ExtractHtml
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

def test_extract():

    http_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert 'html' in html_collector.collect_essential_information_attributes

def test_extract_error():

    http_requester = 'issoVaiDarErro'
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    try:
        extract_html.extract()
    except Exception as exception: # pylint: disable=W0718:broad-exception-caught
        assert isinstance(exception, ExtractError)