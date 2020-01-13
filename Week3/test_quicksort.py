import pytest
import quicksort
import quicksort_assignment

from hypothesis import given, settings, strategies as st


@given(st.lists(st.integers(), min_size=0, max_size=10000))
@settings(max_examples=1000)
def test_quicksort(_input):
    expected = sorted(_input)
    quicksort.quicksort(_input)
    assert _input == expected


@pytest.mark.parametrize("infile,outfile", [
    ("output_dgrcode_20_1000000.txt", "input_dgrcode_20_1000000.txt"),
    ("output_dgrcode_16_100000.txt", "input_dgrcode_16_100000.txt"),
])
def test_num_cmps():
    with open() as output:
        with open() as fp:
            pl = [int(x) for x in fp]
            _orig = pl[:]

            for pivot_func in [
                lambda a: 0,
                lambda a: -1,
                lambda a: sorted([a[0], a[-1], a[(len(a) - 1) // 2]])[1],
            ]:
                assert int(next(output)) == quicksort_assignment.quicksort(pl, pivot_func)
                pl = _orig
                _orig = _orig[:]
