import json
import requests

requests.packages.urllib3.disable_warnings() # verify=False [testing only]. Create link to windows cert for prod

api_key = '##### API_KEY ######'
resource_id = '##### Cloud storage bucket ######' 
base_url = '#####  URL  #####'

headers = {
    'accept-encoding': 'gzip',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json',
    'Api-Key': api_key
}

def get_tags():
    data = {}
    response = requests.get(        
        url = base_url + f'/v2/public/resource/{resource_id}/tags/list',
        data = json.dumps(data),
        verify = False,
        headers = headers
    )
    return response.json()    

print(get_tags())
