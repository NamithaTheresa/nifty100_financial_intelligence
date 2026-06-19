from src.utils.helpers import normalize_ticker, normalize_year

def test_ticker_1():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_2():
    assert normalize_ticker(" infy ") == "INFY"

def test_ticker_3():
    assert normalize_ticker("HdfcBank") == "HDFCBANK"

def test_year_1():
    assert normalize_year("Mar-24") == "2024-03"

def test_year_2():
    assert normalize_year("Mar-23") == "2023-03"

def test_year_3():
    assert normalize_year("Jan-20") == "2020-01"