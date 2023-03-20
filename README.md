[![Formatting](https://github.com/maerkl24/PySide6-DAW/actions/workflows/formatting.yml/badge.svg)](https://github.com/maerkl24/PySide6-DAW/actions/workflows/formatting.yml)
[![Linting](https://github.com/maerkl24/PySide6-DAW/actions/workflows/linting.yml/badge.svg)](https://github.com/maerkl24/PySide6-DAW/actions/workflows/linting.yml)

# PySide6DAW

Desktop Application Widget (DAW) for PySide6.

## Usage

Text ...

## Development and Contribution

You would like to develop and contribute to this project? Then this chapter is what you were looking for.

### PDM

This project uses [PDM](https://pdm.fming.dev) as Python package and dependency manager. In order to develop on this
project, it is recommended to install PDM. For more information, see: <https://pdm.fming.dev/latest/#installation>

### Install Development Tools

To install the ``PySide6-DAW`` Python package with its dependencies and all development tools, execute the following
command on your terminal:

```shell
pdm install --dev
```

### Execute Development Tools

To execute the development tools, run the following commands on your terminal:

```shell
pdm run isort PySide6_DAW
pdm run black PySide6_DAW
pdm run pylint PySide6_DAW
pdm run mypy PySide6_DAW
```

## TODOs

- [ ] Evaluate making DesktopApplication inheriting from MainWindow
- [ ] Maybe add custom properties for ToolTip
- [ ] Fix linting errors
- [ ] Setup contribution rules
- [ ] Setup PiPy deployment
