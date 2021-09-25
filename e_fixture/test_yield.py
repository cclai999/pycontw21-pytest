import pytest


@pytest.fixture
def set_up_pre_and_post_conditions():
    print("Pre condition")
    yield # this will be executed our test
    print("Post condition")


def test(set_up_pre_and_post_conditions):
    print("Body of test")