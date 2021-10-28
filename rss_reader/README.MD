# Rss-reader
A simple commandline app for reading RSS feeds
# Installation

```bash
  $ git clone REPONAME
  $ cd rss-reader
  $ pip install .
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

### Local storage
News are stored in JSON file local_strage.json in rss_reader dir.
structure:
'RSS feed URL' : {'feed':[{news feed files}], 'cashed':'date of last update'}

when you run programm its looks in root dir for local_starage.json, if it exists then programm loads it into feed,
if not it creates empty local storage file, and self.feed = {empty dict}.