import os
import configparser
from dotenv import load_dotenv
from stackapi import StackAPI

directory = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(f"{directory}/config.ini")

load_dotenv()
API_KEY = str(config.get("stackapi","api_key"))

site = StackAPI("stackoverflow", key=API_KEY)
site.page_size = 5
site.max_pages = 1

def fetch_res(query:str):
    responses = site.fetch("search/excerpts", q=query, filter="!nKzQURF6Y5", sort='votes')
    res_list = []
    for response in responses['items']:
        if response['item_type'] == 'question' or response['item_type'] == 'answer':
            question = {}
            title = f"{response['title']}"
            url = f"https://stackoverflow.com/q/{response['question_id']}"
            question['title'] = title
            question['url'] = url
            res_list.append(question)
        else: 
            pass
    return res_list