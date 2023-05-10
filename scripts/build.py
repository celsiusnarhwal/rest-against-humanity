import subprocess
from typing import ClassVar

import tomlkit as toml
from path import Path
from pydantic import BaseModel, Field, parse_obj_as, validator
from tomlkit import TOMLDocument


class Version(BaseModel):
    name: str
    title: str = None
    aliases: list[str] = Field(default_factory=list)
    default: bool = False

    # noinspection PyMethodParameters
    @validator("title", always=True)
    def set_title(cls, v, values):
        return v or values["name"]


class Mike(BaseModel):
    versions_path: ClassVar[Path] = Path.getcwd() / "docs" / "versions"
    branch: str
    push: bool

    def deploy(self, version: str):
        cmd = ["mike", "deploy", "-b", self.branch, version]
        self._execute(cmd, version)

    def retitle(self, version: str, title: str):
        cmd = ["mike", "retitle", "-b", self.branch, version, title]
        self._execute(cmd, version)

    def alias(self, version: str, alias: str):
        cmd = ["mike", "alias", "-b", self.branch, version, alias]
        self._execute(cmd, version)

    def set_default(self, version: str):
        cmd = ["mike", "set-default", "-b", self.branch, version]
        self._execute(cmd, version)

    def _execute(self, cmd: list, version: str):
        with self.versions_path / version:
            if self.push:
                cmd.append("--push")

            print(f"Executing: {' '.join(cmd)}")

            subprocess.run(cmd + ["--allow-empty"])

    @classmethod
    def get_versions(cls) -> TOMLDocument:
        versions = toml.load((cls.versions_path / "versions.toml").open())
        return parse_obj_as(list[Version], versions["version"])


def build(branch: str, push: bool):
    mike = Mike(branch=branch, push=push)

    for version in mike.get_versions():
        mike.deploy(version.name)

        if version.title:
            mike.retitle(version.name, version.title)

        for alias in version.aliases:
            mike.alias(version.name, alias)

        if version.default:
            mike.set_default(version.name)
