import requests
import logging


def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    logging.info(response)
