import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://app.rockgympro.com/b/widget/"

params = {
    "a" : "fcfeed",
    "widget_guid" : "980235b6ef094cd38a1356a41a60ef2c",
    "mode" : "e",
    "start" : "1785045600",
    "end": "1788674400",
}

def convert_response_to_json(raw_response):

    json_response = raw_response.json()

    return json_response

def parse_event(event: dict):

    title_soup = BeautifulSoup(event["title"], "html.parser").get_text()
    start_soup = BeautifulSoup(event["start"], "html.parser").get_text()
    end_soup   = BeautifulSoup(event["end"], "html.parser").get_text()

    start_time = datetime.fromisoformat(start_soup)
    end_time   = datetime.fromisoformat(end_soup)

    cleaned_map = {
        "title" : title_soup,
        "start" : start_time,
        "end"   : end_time,
    }

    return cleaned_map

def convert_json_to_dataframe(json_response: dict):

    event_list = []

    for event in json_response: 
        cleaned_event = parse_event(event=event)
        event_list.append(cleaned_event)

    df = pd.DataFrame(event_list)

    return df

if __name__ == "__main__":

    response = requests.get(url=url, params=params, timeout=10)
    json_response = convert_response_to_json(response)
    result = convert_json_to_dataframe(json_response=json_response)

    print(result)