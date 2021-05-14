import json, os, pytest, requests
from dotenv import load_dotenv
from naughty_string_validator import *

from api.models import Comments, Comment
from tests.utils import *

load_dotenv()


@pytest.mark.parametrize("id,expected_count", [(1,5), (2,5)])
def test_get_comments_for_post(id: int, expected_count: int):
    response = requests.get(f"{os.getenv('BASE_URL')}/comments?postId={id}")
    assert_status_code(response.status_code)
    assert Comments.parse_raw(response.content)
    assert len(json.loads(response.content)) == expected_count # Suboptimal since it is static server

@pytest.mark.parametrize("data", [{"postId": 1, "name": "olo", "email": "test@test.com", "body": "test body"}])
def test_post_comment(data: dict):
    response = requests.post(f"{os.getenv('BASE_URL')}/posts/", data=json.dumps(data), headers=headers)
    comment = Comment.parse_raw(response.content)
    assert response.status_code == 201  # Returns this, should upgrade utils to accept a range of values
    for key in data:
        assert comment.dict()[key] == data[key]


@pytest.mark.parametrize("id", [(1), (2)])
def test_comments_for_post_to_post_comments(id:int):
    comments_filter_by_post = requests.get(f"{os.getenv('BASE_URL')}/comments?postId={id}")
    posts_comments = requests.get(f"{os.getenv('BASE_URL')}/posts/{id}/comments")

    assert_status_code(comments_filter_by_post.status_code)
    assert_status_code(posts_comments.status_code)
    assert json.loads(comments_filter_by_post.content) == json.loads(posts_comments.content)
# Would write in a test to see if the comments allow for malformed comments

l = get_naughty_string_list()

@pytest.fixture(params=l)
def fixture(f):
    return f
@pytest.fixture(params=l)
def test_naught_strings_in_comments(comment: str):
    data = {"postId": 1, "name": "olo", "email": "test@test.com", "body": comment}
    response = requests.post(f"{os.getenv('BASE_URL')}/posts/", data=json.dumps(data), headers=headers)
    comment = Comment.parse_raw(response.content)
    assert response.status_code == 201  # Returns this, should upgrade utils to accept a range of values
    for key in data:
        assert comment.dict()[key] == data[key]