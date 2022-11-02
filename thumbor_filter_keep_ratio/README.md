# Thumbor filter keep aspect ratio

This is a filter for Thumbor that resizes the image while allowing it to be less than the
provided request height and width, but always keeping the aspect ratio.

## Installation

```sh
pip install thumbor_filter_keep_ratio
```

To use the filter, it should be enabled in Thumbor configuration, for example:

```
# thumbor.conf

FILTERS=['thumbor.filters.brightness','thumbor.filters.blur','thumbor_filter_keep_ratio']
```

## Usage

Add `filters:keep_ratio()` to the URL, for example:

```
http://localhost:8888/unsafe/1024x1024/smart/filters:brightness(-5):keep_ratio()/https://example.com/image.jpg
```

## Development

To install the package locally:

```sh
pip install -e ./
```

To build the package:

```sh
# Create source distribution
python setup.py sdist
```

It's expected to get the import error `ImportError: No module named thumbor.filters`. Ignore it, the dist should be built.

To publish the package:

```sh
# Install twine
pip install twine

# Publish the package
twine upload dist/*
```
