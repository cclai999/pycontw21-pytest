"""Demonstrate simple fixtures."""

import pytest


@pytest.fixture()
def some_data():
    """Return value for fixture."""
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42


def test_inc_data(some_data):
    """Use fixture return value in a test."""
    inc_data = some_data + 1
    assert inc_data == 43


