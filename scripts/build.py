import os
import subprocess

from path import Path


def build(branch: str, push: bool):
    with Path.getcwd() / "docs" / "versions":
        for version_dir in Path.getcwd().listdir():
            if not (version := version_dir.stem).startswith("."):
                subprocess.run(
                    f"mike deploy -b {branch} - F{version}/mkdocs.yml {version} {'--push' if push else ''}".split(),
                    env=os.environ,
                )
