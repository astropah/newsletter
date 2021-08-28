
from typing import Union
from pathlib import Path
from datetime import datetime
from warnings import warn
import json


class Section(object):
    def __init__(self, title: str, contents: str, header: Union[None, str] = None)
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        assert type(value) == str
        self._title = value

    @property
    def contents(self) -> str:
        return self._contents

    @contents.setter
    def contents(self, value: str):
        assert type(value) == str
        self._contents = value

    @property
    def header(self) -> str:
        """Override this method to customize how
        you want a header looks, or modify the `_header`
        attribute.
        """
        text = f"# {self.title}"
        if self._header:
            text += f"\n {self._header}"
        return text

    @header.setter
    def header(self, value: Union[None, str]):
        self._header = value

    def build(self) -> str:
        text = f"{self.header} \n {self.contents}"
        return text


def get_current_issue_date() -> str:
    return datetime.now().strftime("%M-%Y")


def unpack_issue_details(issue_details) ->str:
    tex = ""
    for key, value in issue_details.items():
        if key != "potmcredits":
            tex += f"\\newcommand{{\\{key}}}{{{value}}}\n"
        else:
            pass
    return tex


def main():
    issue_json = Path("issue_details.json")
    if not issue_json.exists():
        raise FileNotFoundError("issue_details.json is not found!")
    issue_details = json.loads(issue_json.read())
    full_text = f"{unpack_issue_details(issue_details)}\n"
    for folder in ["editorial", "infocus"]:
        md_files = Path(folder).rglob("*.md")
        if len(md_files) == 0:
            warn(f"{folder} does not contain any markdown files!")
        else:
            contents = "\n".join([file.read() for file in md_files])
            section = Section(folder.capitalize(), contents)
            full_text += f"\n {section.build()}"
    return full_text
