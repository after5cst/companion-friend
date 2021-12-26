from __future__ import annotations
import dataclasses
import pathlib
import yaml


@dataclasses.dataclass(frozen=True)
class ButtonAttributes:
    bgcolor: str
    color: str
    text: str
    size: int

    def save(self, path: pathlib.Path):
        with open(path, "w") as fp:
            fp.write(yaml.dump(dataclasses.asdict(self)))  # type: ignore

    @staticmethod
    def load(path: pathlib.Path) -> ButtonAttributes:
        with open(path) as fp:
            data: dict[str, str | int] = yaml.safe_load(fp)  # type: ignore
            return ButtonAttributes(
                bgcolor=str(data["bgcolor"]),
                color=str(data["color"]),
                text=str(data["text"]),
                size=int(data["size"]),
            )


@dataclasses.dataclass
class Button:
    attr: ButtonAttributes
    page: int
    bank: int
