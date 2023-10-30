#!/usr/bin/env python

"""Tests for `aiida_tuktuk` package."""

import pytest


from aiida_tuktuk import aiida_tuktuk


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    print("Test passed.")

if __name__ == "__main__":
    test_content()
