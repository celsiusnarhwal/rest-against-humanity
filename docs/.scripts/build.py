import subprocess

from path import Path

with Path(__file__).parent.parent / "versions":
    for version_dir in Path.getcwd().listdir():
        if not (version := version_dir.stem).startswith("."):
            subprocess.run(
                f"mike deploy -b vercel -F {version}/mkdocs.yml {version}".split()
            )
