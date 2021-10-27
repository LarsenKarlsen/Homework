# https://news.yahoo.com/rss
import argparse
from rss_reader.rss_parser import RssParser

class RSSReader:
    """
    Class responsible for CLI part:
    Parse console for arguments, takes them to the RSSParser
    """

    def __init__(self):
        self.app = self._create_app() # main functionality
        self.version = '1.4'
        args = self.app.parse_args() # take arguments from console input and procced to next steps
         
        # mb this part i need to change
        if args.version == True: # just prints app version
            print(self.version)
        else: # else normal flow 
            parser = RssParser(**vars(args))
            parser.main()

            if args.pdf == True: # if there is pdf flag, run RSSParser metod .to_pdf
                parser.to_pdf()
            elif args.html == True: # if there is html flag, run RSSParser metod .to_html
                parser.to_html()
            elif args.json == True: # if there is json flag, run RSSParser metod .to_json
                parser.to_json()
            else:
                try:
                    parser.print_feed()
                except:
                    print('Something wrong. Cant parse feed in human readable format')
            



    def _create_app(self):
        app = argparse.ArgumentParser(description='Pure Python command-line RSS reader.') # initialyze argparse class
        app.add_argument('sourse',nargs="?", default=None, help='RSS URL') # takes source URL of RSS
        app.add_argument('--version',dest='version', help='Print app version') # takes version flag
        app.add_argument('--json',dest='json', help='Return feed in JSON format',action='store_true') # json flag
        app.add_argument('--verbose',dest='verbose', help='Outputs verbose status messages',action='store_true') # verbose mode flag
        app.add_argument('--limit',dest='limit', help='Limit news topics if this parameter provided', type=int) # rss feed length limit
        app.add_argument('--date',dest='filter_date', default=None, help='Takes a date in `YearMonthDay` format, and filter local feed') # filter local feed
        app.add_argument('--to_pdf',dest='pdf', default=False, help='Saving news feed in pdf format',action='store_true') # feed into pdf file
        app.add_argument('--to_html', dest='html', default=False, help='Saving news feed in html format',action='store_true') # feed into html file
    
        return app