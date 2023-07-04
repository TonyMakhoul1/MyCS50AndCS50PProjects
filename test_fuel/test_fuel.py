from fuel import convert, gauge
import pytest

def test_one():
    assert convert("2/4") == 50 and gauge(50) == "50%"