import pytest

from iteretor_tutorial.itertools_examples import *

@pytest.fixture
def sequences():
    return ["agctctt", "tggtgta", "gcttagt", "aaaagtctgt", "cccta"]

@pytest.fixture
def lines():
    return ["# header1", "# header2", "# header3", "0", "10", "20"]


@pytest.fixture
def ages():
    return [10, 15, 17, 19, 12]


def test_map(sequences):
    assert list(map_example(sequences))==list(map(len, sequences))

def test_filter(sequences):
    assert list(filter_example(sequences))==list(filter(lambda s: len(s)>5, sequences))

def test_longest(sequences):
    lens = [2, 2, 2, 4, 3]
    for seq, l in zip(sequences, lens):
        assert longest_repeat(seq) == l

def test_max_value():
    def func(x, y):
        return x**2-2*y+y**2+1
    assert max_of_function(func) == max(func(x, y) for x, y in product(range(100), repeat=2))

def test_location_from_steps(ages):
    assert list(location_from_steps(ages, start=3)) == list(accumulate(ages, initial=3))

def test_comment(lines):
    assert list(read_numbers(lines)) == list(int(line) for line in dropwhile(lambda line: line.startswith("#"), lines))
