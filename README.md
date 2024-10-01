# lppn
| master | dev |
| :----: | :-: |
| [![CI](https://github.com/president-not-sure/lppn/actions/workflows/CI.yaml/badge.svg?branch=master)](https://github.com/president-not-sure/lppn/actions/workflows/CD.yaml) | [![CI](https://github.com/president-not-sure/lppn/actions/workflows/CI.yaml/badge.svg?branch=dev)](https://github.com/president-not-sure/lppn/actions/workflows/CD.yaml) |

lppn, or Latest Python Patch Number, parses the Python FTP download page for the latest Python patch number of a given major and minor version. It can be used as a cli command or imported as a library. This was developped as a way to atomate the download the most recent python of an older but still supported version.

## Install
```shell
python3 -m venv venv
. venv/bin/activate
pip install lppn
```

## Usage (python)
```python
import lppn

major = 3
minor = 12
patch = lppn.get(major, minor)

print(f'{major}.{minor}.{patch}')
```

## Usage (cli)
```shell
$ lppn -h
usage: lppn [-h] [--full-version] major minor

Prints the latest Python patch number of a given major and minor version

positional arguments:
  major               Major Python version e.g. 3
  minor               Minor Python version e.g. 12

options:
  -h, --help          show this help message and exit
  --full-version, -f  Print full version.
```

