import semver
import tomlkit as toml

version = toml.load(open("pyproject.toml"))["tool"]["poetry"]["version"]
version = semver.parse_version_info(version)

print(f"DOCS_VERSION={version.major}.{version.major}")
