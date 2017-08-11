# dumptube

This tool will download all videos of the given YouTube channels using the best possible quality for each video.

## Requirements

* pytube
* google-api-python-client

## Usage

Set your [Google API key](https://console.developers.google.com/apis/credentials) in an envvar:

    export YT_API_KEY=yourapikey

List the names of the channels you wish to download inside `targets`, one per line. For instance:

    youlost
    thegame

## License

No idea yet, use as if CC-BY-NC-SA
