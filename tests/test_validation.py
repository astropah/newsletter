
from pathlib import Path
from newsletter_tools import parsers, classes

TEST_DIR = Path(__file__).parent

def test_yaml_parser():
    data = parsers.get_yaml_data(TEST_DIR.joinpath("abstracts/lee_1970.yml"))
    # make sure all the keys are present
    assert all([key in data.keys() for key in ["authors", "title", "abstract", "doi", "journal"]])


def test_abstract_class():
    abstract = classes.AbstractEntry.from_yml(TEST_DIR.joinpath("abstracts/herzberg_2021.yml"))
    # check name parsing
    assert str(abstract.authors[0]) == "G. H. Herzberg"
    # check affiliations
    assert abstract.authors[0].affiliations == [classes.Institution("NRC"),]


# def test_author_parsing():
#     data = parsers.get_yaml_data(TEST_DIR.joinpath("abstracts/herzberg_2021.yml"))
#     authors = parsers.extract_authors(data.get("authors"))
#     assert authors == ["Herzberg, G. H.", "Hougen, J.", "Watson, J."]
#     # now try and extract names
#     assert parsers.first_last_names(authors[0]) == "G. H. Herzberg"
