import pytest

from utils.dicts import get_val


def test_val(fixture_dict):
    assert get_val(fixture_dict, 'name') == 'Kris'
