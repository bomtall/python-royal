import pytest

from demo.plotting_demo import toms_plot

def test_plotting_demo():
    try:
        toms_plot()
    except Exception as e:
        pytest.fail(f"plotting_demo raised an exception: {e}")
