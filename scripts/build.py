import subprocess

from path import Path


def build(push: bool):
    with Path.getcwd() / "docs" / "versions":
        for version_dir in Path.getcwd().listdir():
            if not (version := version_dir.stem).startswith("."):
                subprocess.run(
                    f"mike deploy -b vercel -F {version}/mkdocs.yml {version} {'--push' if push else ''}".split()
                )
