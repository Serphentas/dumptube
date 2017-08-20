# dumptube

This tool will download all videos of the given YouTube channels using the best possible quality for each video.

It also stores metadata from both channels and videos inside a local database with parent-children relationships.

## Requirements

* python 3
* pytube
* google-api-python-client
* sqlalchemy

## Usage

Set your [Google API key](https://console.developers.google.com/apis/credentials) in an envvar:

    export YT_API_KEY=yourapikey

List the names of the channels you wish to download inside `targets`, one per line. For instance:

    youlost
    thegame

Then, install and run:

    pyvenv venv
    . venv/bin/activate
    pip install .
    python dumptube

By default, videos are stored in `/dumps`. You may specify the directory in which videos should be saved using the `-d` keyword:

    python dumptube -d /tmp

You can also see what has been stored in the database (`db.sqlite`) like so:

    python dumptube -s

## Contributing

See [here](CONTRIBUTING.md)

## License

No idea yet, use as if [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/3.0)
