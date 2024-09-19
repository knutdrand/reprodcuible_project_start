#!/usr/bin/env python

"""Tests for `reprodcuible_project_start` package."""

import pytest

from reprodcuible_project_start.reprodcuible_project_start import count_gc


@pytest.fixture
def seq():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
    return 'acgtcg'

def test_content(seq):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert count_gc(seq) == 4
