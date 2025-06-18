import requests

from modules.load_data import load_key

def animal_api_call(name: str):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': load_key()})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return []

class Animal:
    def __init__(self, data: dict):
        self.data = data
    @property
    def name(self) -> str:
        return self.data.get('name',"")
    @property
    def diet(self) -> str:
        return self.data.get('characteristics',{}).get('diet',"")
    @property
    def type(self) -> str:
        return self.data.get('characteristics',{}).get('type',"")
    @property
    def first_location(self) -> str:
        _ret = self.data.get('locations',[])
        return _ret[0] if _ret else ''