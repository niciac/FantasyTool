# Based on the notebook examples
# Written as script to run in command line

from datetime import date
import json
import logging
from pathlib import Path as path
import requests

import config_reader
from config_reader import get_urls, settings

# settings = config_reader.load_settings()

# Authenticated Access
def API_authentication(
    login_email: str = config_reader.get_login_info(settings)["login_email"],
    password: str = config_reader.get_login_info(settings)["password"],
    fpl_manager_id: str = settings["url_completion_values"][
    "fpl_manager_id"]):

    session = requests.session()

    url = "https://users.premierleague.com/accounts/login/"
    payload = {
        "password": password,
        "login": login_email,
        "redirect_uri": "https://fantasy.premierleague.com/a/login",
        "app": "plfpl-web",
    }

    session.post(url, data=payload)

    response = session.get(
        f"https://fantasy.premierleague.com/drf/my-team/{fpl_manager_id}"
    )

    print(type(response))

    return response

def user_input():
    data = input("Enter choices, separated by spaces:\n")
    print(*data.split(" "))


urls = get_urls(settings)


# get API data withour authentication
def API_request_without_authentication(urls:dict=urls):
    # Use requests to get request from API
    url = urls['main_endpoint_url']['link'] + urls['general_information_endpoint_path']['link']
    request = requests.get(url)
    data_nested_dict = request.json()
    return data_nested_dict

# save downloaded data to json format
def save_dated_json_file(data_nested_dict:dict):
    x = date.today()
    day, month, year = x.day, x.month, x.year
    json_output_file_path = path(
        "Data",
        "raw",
        "general_information",
        "2022-2023",
        f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}.json",
    )
    print(str(json_output_file_path))

    if json_output_file_path.exists():
        raise IOError("File already exists")
    else:
        output_file = open(json_output_file_path, "w")
        json.dump(data_nested_dict, output_file, indent=4)

        output_file.close()

if __name__ == "__main__":
    raw_data = API_request_without_authentication()
    save_dated_json_file(raw_data)

# information about endpoints found in the below article
# https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19
