"""Testing for the library."""
from src import vue_cinema


def test_get_cinemas():
    """
    Tests the get cinemas.

    There are 91 vue cinemas in the uk so it should return 91.
    """
    cinemas = vue_cinema.get_cinemas()
    assert len(cinemas) == 91


def test_get_cinemas_by_id():
    """
    Tests getting a cinema by id.

    Manchester Printworks has id 10091
    Manchester Quayside has id 10057
    """
    manchester_printworks = vue_cinema.Cinema().from_id(10091)
    assert manchester_printworks.name == "Manchester Printworks"

    manchester_quayside = vue_cinema.Cinema().from_id(10057)
    assert manchester_quayside.name == "Manchester"


def test_cinema_values():
    """Test all the values of the cinema."""
    cinema = vue_cinema.Cinema().from_id(10091)
    assert cinema.id == 10091
    assert cinema.name == "Manchester Printworks"
    assert cinema.search_term == "Manchester Printworks"
    assert cinema.link_name == "manchester-printworks"
