import os

import semver
import tomlkit as toml

version = toml.load(open("pyproject.toml").read())["tool"]["poetry"]["version"]
version = semver.parse_version_info(version)

with open(os.getenv("GITHUB_OUTPUT", "w")) as output:
    output.write(f"DOCS_VERSION={version.major}.{version.major}")
