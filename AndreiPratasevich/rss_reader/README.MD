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

usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--to_pdf] [--to_html]
                     source

## without installing:
Prints news feed in command line

'''bash
python rss_reader URL_RSS 
'''

For help and additional functionality
'''bash
python rss_reader -h 
'''


The cashed news can be read with it. The new from the specified day will be printed out.
If the news are not found return an error.
