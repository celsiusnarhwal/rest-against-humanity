# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

Nothing yet.

## [2.0.0] - 2023-02-21

This is the first versioned release of REST Against Humanity.

### Added

- REST Against Humanity is now a versioned API. Its versioning scheme will adhere to [Semantic Versioning]
  (https://semver.org/) as closely as possible.
- Pack names and cards are now served from distinct endpoints.
- Cards can now be filtered by color and pick.
- For all additions brought by version 2.0.0, see the [documentation](https://restagainsthumanity.com/docs).

### Changed

- The API's root endpoint is now located at `https://restagainsthumanity.com/api/vX/`, where `X` is the
  major version of the API you wish to access.
  - The previous, unversioned, release of REST Against Humanity has been retroactively dubbed Version 1 and is
    accessible at `https://restagainsthumanity.com/api/v1/`.
  - `https://restagainsthumanity.com/api/` will **always** redirect to Version 1.
- REST Against Humanity's documentation is now located at `https://restagainsthumanity.com/docs/version`, where
  `version` is the version of the documentation you wish to access.
  - The latest version of the documentation is always accessible at `https://restagainsthumanity.com/docs/latest`.
  - `https://restagainsthumanity.com` and `https://restagainsthumanity.com/docs` will **always** redirect to the
    latest version of the documentation.
