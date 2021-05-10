import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://jrpizzamamadjangogri.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizza_dict = [pizzaModel['fields'] for pizzaModel in data]
            print("data_received")
            if on_complete:
                on_complete(pizza_dict)

        def data_error(req, error):
            print("data_error")
            if on_error:
                on_error(error.args[0])

        def data_failure(req, result):
            print("data_failure")
            if on_error:
                on_error("Erreur serveur : " + str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
