# https://news.yahoo.com/rss
import argparse
from .rss_parser import RssParser

class RSSReader:
    """
    Class responsible for CLI part:
    Parse console for arguments, takes them to the RSSParser
    """

    def __init__(self):
        self.app = self._create_app() # main functionality
        self.version = '1.3' # version (dont forget to change!)
        args = self.app.parse_args() # take arguments from console input and procced to next steps
         
        # mb this part i need to change
        if args.version == True: # just prints app version
            print(self.version)
        elif args.json == True: # if there is json flag, run RSSParser metod .to_json
            parser = RssParser(**vars(args))
            parser.to_json()
        else: # else normal flow 
            parser = RssParser(**vars(args))



    def _create_app(self):
        app = argparse.ArgumentParser(description='Pure Python command-line RSS reader.') # initialyze argparse class
        app.add_argument('sourse',nargs="?", default=None, help='RSS URL') # takes source URL of RSS
        app.add_argument('--version',dest='version', help='Print app version') # takes version flag
        app.add_argument('--json',dest='json', help='Return feed in JSON format',action='store_true') # json flag
        app.add_argument('--verbose',dest='verbose', help='Outputs verbose status messages',action='store_true') # verbose mode flag
        app.add_argument('--limit',dest='limit', help='Limit news topics if this parameter provided', type=int) # rss feed length limit
        app.add_argument('--date',dest='filter_date', default=None, help='Takes a date in `%Y%m%d` format, and filter local feed') # filter local feed 
    
        return app