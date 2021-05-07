from api.models import Post, Posts, Comment
import pytest
from pydantic import ValidationError

def test_post_model():
    with pytest.raises(ValidationError) as e:
        p = Post()
    assert len(e.value.args[0]) == 4, f"{len(e.value.args[0])} were found, expected 4 Validation Errors"


def test_posts_model():
    with pytest.raises(ValidationError) as e:
        p = Posts() # Needs at least one Post to work, might not be valid if spinning up new env has 0 in it 
    assert len(e.value.args[0]) == 1, f"{len(e.value.args[0])} were found, expected 1 Validation Error"

# Hypothesis Testing would be great here to test the properties of the objects 

def test_comment_model():
    with pytest.raises(ValidationError) as e:
        c = Comment() 
    assert len(e.value.args[0]) == 5, f"{len(e.value.args[0])} were found, expected 5 Validation Errors"