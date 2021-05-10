import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete):
        url = "https://jrpizzamamadjangogri.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizza_dict = [pizzaModel['fields'] for pizzaModel in data]
            print("data_received")
            if on_complete:
                on_complete(pizza_dict)

        req = UrlRequest(url, on_success=data_received)
