from src.analytics.leverage_efficiency import (
    calculate_de,
    calculate_icr,
    calculate_asset_turnover
)

def test_de_positive():

    row = {
        "company_id": "TCS",
        "borrowings": 100,
        "equity": 200
    }

    assert calculate_de(row) == 0.5


def test_de_negative_equity():

    row = {
        "company_id": "TCS",
        "borrowings": 100,
        "equity": -10
    }

    assert calculate_de(row) is None


def test_icr_zero_interest():

    row = {
        "interest": 0,
        "operating_profit": 100
    }

    assert calculate_icr(row) is None


def test_asset_turnover():

    row = {
        "sales": 1000,
        "total_assets": 500
    }

    assert calculate_asset_turnover(row) == 2.0