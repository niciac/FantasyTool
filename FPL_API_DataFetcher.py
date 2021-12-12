# Based on the notebook tutorial
# Written as script to run all command line

import requests
import pandas as pd
import numpy as np
from datetime import date
from pathlib import Path as path


# API url
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

# Use requests to get request from API
request = requests.get(url)
json = request.json()

elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])

x = date.today()
day, month, year = x.day, x.month, x.year

dated_filename = f'{year}-{month}-{day}.csv'
if path(f"./Data/{dated_filename}").exists():
    raise IOError("File already exists")
else:
    elements_df.to_csv(path(f"./Data/{dated_filename}"))