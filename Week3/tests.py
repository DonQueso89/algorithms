import quicksort
from hypothesis import given, settings, strategies as st


@given(st.lists(st.integers(), min_size=0, max_size=10000))
@settings(max_examples=1000)
def test_quicksort(_input):
    expected = sorted(_input)
    quicksort.quicksort(_input)
    assert _input == expected
