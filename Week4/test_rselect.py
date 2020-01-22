from hypothesis import given, settings, strategies as st
from rselect import rselect
from statistics import median


@given(st.lists(st.integers(), min_size=1001, max_size=1001))
@settings(max_examples=10)
def test_rselect(_input):
    assert rselect(_input, 501) == median(_input)
