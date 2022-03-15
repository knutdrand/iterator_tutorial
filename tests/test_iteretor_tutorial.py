#!/usr/bin/env python

"""Tests for `iteretor_tutorial` package."""

import pytest
from iteretor_tutorial.list_comprehensions import *

@pytest.fixture
def sequences():
    return ["agctctt", "tggtgta", "gcttagt", "aaaagtctgt", "cccta"]

@pytest.fixture
def ages():
    return [10, 15, 17, 19, 12]

def test_simple(sequences):
    assert simple_loop(sequences) == [len(s) for s in sequences]

def test_double(sequences):
    assert double_loop(sequences) == [[ord(c) for c in s] for s in sequences]

def test_setcomprehension(sequences):
    assert set_comprehension(sequences) == {c for sequence in sequences for c in sequence}

def test_double(sequences):
    assert two_operations(sequences) == [len(s.replace("a", "")) for s in sequences]

def test_sum(sequences):
    assert len_sum(sequences) == sum(len(s) for s in sequences)

def test_filter(sequences):
    assert len_filter(sequences) == [s.count("a") for s in sequences if len(s)>5]

def test_zip(sequences, ages):
    assert age_filter(sequences, ages) == [s.count("a") for s, a in zip(sequences, ages) if a>=15]
