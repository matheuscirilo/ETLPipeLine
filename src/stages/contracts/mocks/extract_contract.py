from src.stages.contracts.extract_contract import ExtractContract
from datetime import date

extract_contract_mock = ExtractContract(
    raw_information_content= [
        {'name': 'Zanini, Giuseppe', 'link': 'https://web.archive.org/we17b/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'}, 
        {'name': 'Zanini-Viola, Giuseppe', 'link': 'https:/ae/web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597'}, 
        {'name': 'Zanotti, Giampietro', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631'}, 
        {'name': 'Zao Wo''u-Ki', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427'}, 
        {'name': ', Zas-Zie', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ2.htm'}, 
        {'name': 'Zie-Zor:/', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ3.htm'}, 
        {'name': '<strong>next<brrk/>page</strong>', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ4.htm'}
    ],
    extraction_date=date.today()
)
