import pytest

from finance_classes import Asset

@pytest.fixture
def test_asset():
    return Asset("KNEB")

def test_basic_data_by_ticker(test_asset):
    basic_data = test_asset.show_basic_data(self.test_asset)
    self.assertEqual("12345", basic_data)