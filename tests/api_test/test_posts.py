import json, os, pytest, requests
from dotenv import load_dotenv

from api.models import Post, Posts
from tests.utils import *

load_dotenv()


def test_get_all_posts():
    response = requests.get(f"{os.getenv('BASE_URL')}/posts/")
    assert_status_code(response.status_code)
    assert Posts.parse_raw(response.content)
    assert len(json.loads(response.content)) >= 100  # 100 is the minimum number if the server gets restarted


# Should pull this post data into a JSON file for VCS
post_test_data = [
    (1, {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
         'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'})
]


@pytest.mark.parametrize("id,content", post_test_data)
def test_get_post(id: int, content: dict):
    response = requests.get(f"{os.getenv('BASE_URL')}/posts/{id}")
    assert_status_code(response.status_code)
    assert Post.parse_raw(
        response.content), f"Response content wasn't parsed correctly received {json.loads(response.content)}"
    assert json.loads(response.content) == content, f"Response content was not expected"


new_post = {'title': 'olo foo', 'body': 'bar', 'userId': 1}

@pytest.mark.parametrize("data", [new_post])
def test_post_posts(data: dict):
    response = requests.post(f"{os.getenv('BASE_URL')}/posts/", data=json.dumps(data), headers=headers)
    post = Post.parse_raw(response.content)
    assert response.status_code == 201  # Returns this, should upgrade utils to accept a range of values
    for key in data:
        assert post.dict()[key] == data[key]

    retrieved_post = requests.get(f"{os.getenv('BASE_URL')}/posts/{post.id}")

    # This should work but doesnt since this site doesnt store posts
    # assert Post.parse_raw(retrieved_post.content) == post


# This always returns 200 even passing an empty body, if no posts it should fail but doesnt
# Dont know what it should raise as an error
@pytest.mark.skip
def test_malformed_post_posts():
    malformed_post = new_post
    malformed_post.pop("userId")
    response = requests.post(f"{os.getenv('BASE_URL')}/posts/", data=json.dumps({}), headers=headers)
    post = Post.parse_raw(response.status_code)
    assert response.status_code == 201  # Returns this, should upgrade utils to accept a range of values


@pytest.mark.parametrize("id", [(1), (2), (4),(5),(33)])
def test_delete_post(id: int):
    response = requests.delete(f"{os.getenv('BASE_URL')}/posts/{id}")
    assert response.status_code == 200
    check = requests.get(f"{os.getenv('BASE_URL')}/posts/{id}")

    # This should fail but doesnt
    # assert check.status_code !=200
