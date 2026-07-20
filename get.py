import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://app.rockgympro.com/b/widget/"

params = {
    "a" : "fcfeed",
    "widget_guid" : "980235b6ef094cd38a1356a41a60ef2c",
    "start" : "1782626400",
    "end": "1786255200",
}

def convert_response_to_json(raw_response):

    json_response = raw_response.json()

    return json_response

def parse_event(event: dict):

    title_soup = BeautifulSoup(event["title"], "html.parser").get_text()
    start_time = datetime.fromisoformat(event["start"])
    end_time   = datetime.fromisoformat(event["end"])

    cleaned_map = {
        "title" : title_soup,
        "start" : start_time,
        "end"   : end_time,
    }

    return cleaned_map

def cleaned_event_list(json_response: dict):

    event_list = []

    for event in json_response: 
        cleaned_event = parse_event(event=event)
        event_list.append(cleaned_event)

    return event_list

if __name__ == "__main__":

    response = requests.get(url=url, params=params, timeout=10)
    json_response = convert_response_to_json(response)
    all_events = cleaned_event_list(json_response)
    print(all_events)