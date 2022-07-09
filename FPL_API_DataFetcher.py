# Based on the notebook examples
# Written as script to run in command line

from datetime import date
import json
from pathlib import Path as path
import requests

class URL():
    pass

def requires_completion(string:str)->bool:
    
    '''Checks if the configuration string requires a completion 
    from the completion section of the configuration file.'''
    
    for char in string:
        if char == '{':
            opening = True
        elif char == '}':
            closing = True
        else:
            continue
    return opening and closing

def get_urls(config_file_path:path=path('personal_config.yaml')):
    config = ConfigParser()
    config.read(config_file_path)
    
    main_endpoint_url = config.get('URL','MAIN_ENDPOINT_URL')
    general_information_endpoint_path = config.get('URL','GENERAL_INFORMATION_ENDPOINT_PATH')
    fixtures_url_endpoint_path = config.get('URL','FIXTURES_URL_ENDPOINT_PATH')
    player_detailed_data_endpoint_path = config.get('URL','player_detailed_data_endpoint_path')
    element_id = config.get('URL_COMPLETION_VALUES','ELEMENT_ID')

    # requested_url = main_endpoint_url + fixtures_url_endpoint_path.format(event=1)
    # requested_url = list(config.get('URL_COMPLETION_VALUES','list'))
    requested_url = main_endpoint_url + general_information_endpoint_path
    return requested_url

# print(get_urls())


# Authenticated Access
def API_authentication(login_email:str=get_login_info_yaml()['login_email'], password:str=get_login_info_yaml()['password'], fpl_manager_id:str=fpl_manager_id):
    session = requests.session()
    
    url = 'https://users.premierleague.com/accounts/login/'
    payload = {
        'password': password,
        'login': login_email,
        'redirect_uri': 'https://fantasy.premierleague.com/a/login',
        'app': 'plfpl-web'
    }

    session.post(url, data=payload)

    response = session.get(f'https://fantasy.premierleague.com/drf/my-team/{fpl_manager_id}')

    print(type(response))

    return response

# get API data withour authentication
def API_request_without_authentication():
    # Use requests to get request from API
    request = requests.get(get_urls())
    data_nested_dict = request.json()
    return data_nested_dict

# save downloaded data to json format
def save_dated_json_file(data_nested_dict = API_request_without_authentication()):
    x = date.today()
    day, month, year = x.day, x.month, x.year
    json_output_file_path = path('Data','raw','general_information',f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}.json')
    print(str(json_output_file_path))

    if json_output_file_path.exists():
        raise IOError("File already exists")
    else:
        output_file = open(json_output_file_path,'w')
        json.dump(data_nested_dict,output_file, indent=4)
        
        output_file.close()

def user_input():
    data = input('Enter choices, separated by spaces:\n')
    print(*data.split(' '))

# user_input()
# print(get_login_info_ini())

if __name__ == "__main__":
    save_dated_json_file()

# information about endpoints found in the below article
# https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19