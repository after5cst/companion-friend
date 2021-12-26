import dataclasses
from comfriend.streamdeck import ButtonAttributes

import pathlib


def test_can_save_and_load_button_attributes(tmpdir: pathlib.Path):
    expected = ButtonAttributes(bgcolor="#111111", color="#222222", text="text", size=1)
    fname = tmpdir / "data.json"

    expected.save(fname)
    observed = ButtonAttributes.load(fname)
    assert observed == expected
