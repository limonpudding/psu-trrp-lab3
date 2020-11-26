from zeep import Client, Settings
from params import Params


def soap_request(params: Params):
    headerArr = {}
    settings = Settings(strict=False, xml_huge_tree=True, extra_http_headers=headerArr)
    client = Client('http://localhost:8080/psu-trrp-lab3/calculate?wsdl',
                    settings=settings)

    requestData = params.get_request_body()
    return client.service.calculate(**requestData)
