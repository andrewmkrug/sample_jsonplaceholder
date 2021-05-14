import logging

import pytest
from pydantic import ValidationError

from api.models import *

class ModelTests:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def test_post_model(self):
        with pytest.raises(ValidationError) as e:
            post = Post()
        assert len(e.value.args[0]) == 4, f"{len(e.value.args[0])} were found, expected 4 Validation Errors"
        self.log.info(e)


    def test_posts_model(self):
        with pytest.raises(ValidationError) as e:
            posts = Posts()  # Needs at least one Post to work, might not be valid if spinning up new env has 0 in it
        assert len(e.value.args[0]) == 1, f"{len(e.value.args[0])} were found, expected 1 Validation Error"


    def test_comment_model(self):
        with pytest.raises(ValidationError) as e:
            comment = Comment()
        assert len(e.value.args[0]) == 5, f"{len(e.value.args[0])} were found, expected 5 Validation Errors"


    def test_comments_model(self):
        with pytest.raises(ValidationError) as e:
            comments = Comments()  # Needs at least one Post to work, might not be valid if spinning up new env has 0 in it
        assert len(e.value.args[0]) == 1, f"{len(e.value.args[0])} were found, expected 1 Validation Error"
