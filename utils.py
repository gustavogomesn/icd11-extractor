import requests
import json

class FetchCID():

    def __change_uri(self, endpoint):
        #ATENÇÃO - API rodando via imagem Docker na porta 8080
        return endpoint.replace('id.who.int', 'localhost:8080')

    def get_data(self, endpoint):
        uri = endpoint
        
        headers = {
                    'Accept-Language': 'pt',
                    'API-Version': 'v2'
            }
        
        try:
            r = requests.get(uri, headers=headers, verify=False)
        except requests.exceptions.MissingSchema:
            return json.loads('{"error": "missing schema"}')
        return json.loads(r.text)

    def get_description(self, endpoint):
        data = {}
        #Verificando se o valor da URI não é NaN
        if endpoint == endpoint:
            data = self.get_data(self.__change_uri(endpoint))
        try:
            return data['definition']['@value']
        except KeyError:
            return float("NaN")