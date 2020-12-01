from zeep import Client, Settings
from params import Params


def soap_request(url, params: Params):
    headerArr = {}
    settings = Settings(strict=False, xml_huge_tree=True, extra_http_headers=headerArr)
    client = Client(url, settings=settings)

    requestData = params.get_request_body()
    return client.service.calculate(**requestData)
