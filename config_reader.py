"""Reads the required data from the yaml configuration file in path"""

from pathlib import Path as path
import yaml


def get_login_info(config_file_path: path = path("personal_config.yml")) -> dict:
    """Gets the login information from the configuration file"""

    print(yaml.safe_load(str(config_file_path)))
    with open(config_file_path) as config_file:
        config = yaml.safe_load(config_file)
    print(
        config["url"]["main_endpoint_url"]
        + config["url"]["general_information_endpoint_path"]
    )
    print(config["login_info"]["login_email"])
    login_email = config["login_info"]["login_email"]
    password = config["login_info"]["password"]
    return {"login_email": login_email, "password": password}

if __name__ == "__main__":
    get_login_info()