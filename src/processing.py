import json
from pathlib import Path as path

import pandas as pd

def load_data(datapath: path) -> dict:
    with open(datapath) as json_data:
        data_as_dict = json.load(json_data)
        print(
            "Loaded data: ",
            "".rjust(13, "-"),
            *[f"{idx+1}. {k}" for idx, k in enumerate(data_as_dict.keys())],
            sep="\n",
        )
    return data_as_dict


if __name__ == "__main__":
    print("TESTING".center(13, "-"))
    load_data(path("Data/raw/general_information/2022-2023/2022-08-24.json"))
