# Rss-reader
A simple commandline app for reading RSS feeds
# Installation
## Manual
```bash
  $ git clone REPONAME
  $ cd rss-reader/dist
  $ pip install rss_reader-1.4.tar.gz
```
# Usage

usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

The RSS news stored in a local storage while reading. 

Please describe it in a separate section of README.md or in the documentation.
Cached news stored in JSON format(local_storage.json)
{
    "https://news.yahoo.com/rss":{"feed": [{"title": "North Korean soldier in blue generates buzz on social media", "link": "https://news.yahoo.com/north-korean-soldier-blue-generate-121844697.html", "description": null, "pubDate": "20211012"},"cached": "12/10/2021"}}
}
feed - list of news objects in format {"title":str,"link": str,"description":, "pubDate":}
cached - date in d/m/Y when feed was updated 
}

optional argument `--date` take a date in `%Y%m%d` format.
For example: `--date 20191020`
Here date means actual *publishing date* e.g. pubDate not the date when you fetched the news.

The cashed news can be read with it. The new from the specified day will be printed out.
If the news are not found return an error.
