## v0.0.4 (2023-12-19)

[GitHub release](https://github.com/Automate-Everything-Company/logo_bg_vanisher/releases/tag/v0.0.4)

The code released in v0.0.4 handles iPhone's .HEIC format.
The library saves the pictures ONLY as .png.

### What's Changed

* No error is raised when the user wants to work with the .HEIC format.

## v0.0.3 (2023-12-15)

[GitHub release](https://github.com/Automate-Everything-Company/logo_bg_vanisher/releases/tag/v0.0.3)

Remove version from dependencies

## v0.0.2 (2023-12-10)

[GitHub release](https://github.com/Automate-Everything-Company/logo_bg_vanisher/releases/tag/v0.0.2)

The code released in v0.0.2 changed the folder path input parameter and is NOT functionally identical to that of v0.0.1.

### What's Changed

* Renamed user argument from '--input_path' to '--folder'
* Added user arguments validation
* Added instance attribute validation for all classes

#### New Features

* Add pydantic for type validation in [#15](https://github.com/Automate-Everything-Company/logo_bg_vanisher/pull/15)
* Add tests for CLI testing [#13](https://github.com/Automate-Everything-Company/logo_bg_vanisher/pull/13)

#### Fixes

* Fix faulty `--cropped` to `--crop` argument # todo: fill the pull request link

## v0.0.1 (2023-12-07)

[GitHub release](https://github.com/Automate-Everything-Company/logo_bg_vanisher/releases/tag/v0.0.1)

* First version for test.pypi 