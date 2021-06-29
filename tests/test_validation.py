
from pathlib import Path
from newsletter_tools import parsers

TEST_DIR = Path(__file__).parent

def test_yaml_parser():
    data = parsers.get_yaml_data(TEST_DIR.joinpath("abstracts/lee_1970.yml"))
    assert all([key in data.keys() for key in ["authors", "title", "abstract", "doi", "journal"]])


def test_author_parsing():
    data = parsers.get_yaml_data(TEST_DIR.joinpath("abstracts/herzberg_2021.yml"))
    authors = parsers.extract_authors(data.get("authors"))
    assert authors == ["Herzberg, G. H.", "Hougen, J.", "Watson, J."]
    # now try and extract names
    assert parsers.first_last_names(authors[0]) == "G. H. Herzberg"
