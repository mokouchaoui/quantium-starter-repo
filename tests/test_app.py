import pytest
from dash import Dash
from app import app  # Import the Dash app instance

@pytest.fixture
def test_client(dash_duo):
    return dash_duo.start_server(app)

def test_header_is_present(test_client):
    """Check if the header is present"""
    test_client.wait_for_element("h1", timeout=5)
    assert test_client.find_element("h1").text == "Pink Morsels Sales Analysis"

def test_visualisation_is_present(test_client):
    """Check if the graph visualization is present"""
    test_client.wait_for_element("#sales-line-chart", timeout=5)
    assert test_client.find_element("#sales-line-chart").is_displayed()

def test_region_picker_is_present(test_client):
    """Check if the region selector (radio button) is present"""
    test_client.wait_for_element("#region-selector", timeout=5)
    assert test_client.find_element("#region-selector").is_displayed()
