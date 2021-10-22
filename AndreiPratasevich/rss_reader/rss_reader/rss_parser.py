# https://news.yahoo.com/rss
# https://news.yahoo.com/rss/science
from datetime import date, datetime
import requests
import json
from bs4 import BeautifulSoup
from .logs import get_rss_log, parse_log, feed_log, exec_time, time_converter # import decorators responsible for logs output
from os import path

class RssParser:
    """
    Main part of programm
    Class witch response for get rss, manipulate rss feed in human readable format

    takes arguments from RSS reader class
    decorators above methods used for --verbose flag
    """
    @exec_time
    def __init__(self,**kwargs):
        self.verbose = kwargs['verbose'] # verbose arg from RssReader class (RRC)
        self.limit = kwargs['limit'] # limit arg from
        self.local_storage_path = path.join(path.dirname(__file__), 'local_storage.json') # path to dir with rss_reader.py
        self.feed = None # for news
        self._make_local_storage()
        self.local_data = self._read_local_storage()
        if kwargs['filter_date']:
            self.feed = self._local_feed(sourse=kwargs['sourse'], filter_date=kwargs['filter_date']) # get local_feed
            self.channel = ''
        else:
            self.raw = self._get_rss(kwargs['sourse']) # connect to source URL, get XML content and returne SOUP obj
            self.channel = self._get_channel() # RSS feed name
            self.feed = self._parse() # list of dicts with rss news (items) after parsing
            self._save_feed(kwargs['sourse'])
        
        self.print_feed()


    def _local_feed(self,sourse = None, filter_date = None):
        """
        Method. Loads news feed from local storage
        """
        try:
            if sourse:
                channel = sourse
                feed = self.local_data[sourse]['feed']
            else:
                feed = []
                channel = '\nAll news from:\n'
                for key in self.local_data:
                    channel += f'{key}\n'
                    feed.extend(self.local_data[key]['feed'])
            if filter_date:
                filtered_feed = []
                for index, article in enumerate(feed):
                    if article['pubDate'] == filter_date:
                        filtered_feed.append(feed.pop(index))
                feed = filtered_feed
            print(channel)
            return feed
        except Exception as e:
            print('THERE IS PROBLEM')
            print(e) # TODO more exceptions


    def _make_local_storage(self):
        '''
        Try to find local storage if not create it
        '''
        try:
            #print('Find local storage')
            with open(self.local_storage_path, mode='r'):
                pass
        except:
            print('There is no storage file yet')
            print('Creating local storage file')
            with open(self.local_storage_path, mode='w'):
                pass

    def _read_local_storage(self, p=False):
        """
        Read local storage file
        """
        try:
            with open(self.local_storage_path, mode='r') as json_file:
                data = json.load(json_file)
        except:
            data = {}
        
        return data

    def _save_feed(self, source):
        # try to get sourse from local storage
        try:
            source_feed = self.local_data[source]
            #print('sourse present in a local storage')
            last_new_link = source_feed['feed'][0]['link'] # get freshest link in sourse part of local storage
            
            feed_links = [] # get links in self.feed
            for article in self.feed:
                feed_links.append(article['link'])
            
            #print('Всего новостей в ленте: ',len(feed_links))
            index_last_local_new = feed_links.index(last_new_link)
            # print(index_last_local_new) # find index of last local new in fetchen news feed
            
            if index_last_local_new == 0:
                return
            new_source_feed = self.feed[:index_last_local_new]
            new_source_feed.extend(source_feed)
            
            #print(len(new_source_feed))
            
            self.local_data[source]['feed'] = new_source_feed
            self.local_data[source]['cached'] = date.today().strftime("%d/%m/%Y")

            # print('LOCAL STORAGE UPDATED')
            
        except:
            # add fresh news to local storage
            print ('New sourse, add it to local storage')
            new_source_feed = {
                'feed': self.feed,
                'cached': date.today().strftime("%d/%m/%Y")
            }

            self.local_data[source] = new_source_feed
            print('ADD NEW SOURSE TO LOCAL STORAGE')
        
        with open(self.local_storage_path, mode='w') as outputfile:
            json.dump(self.local_data, outputfile)
        
        print('WRITE LOCAL STORAGE SECCESSFUL')

    @get_rss_log 
    def _get_rss(self,url):
        '''
        Takes RSS feed url try to connect
        Return SOUP object with XML content (RSS FEED)
        '''
        try:
            resp = requests.get(url) # request to RSS URL
        except Exception as e:
            print('Error fetching the URL: ', url) # print error if cant fetch data from RSS FEED
            print(e)
        
        try:
            soup = BeautifulSoup(resp.content, features='lxml', from_encoding='utf-8') # try to convert pure XML to SOUB object (raw data)
        except Exception as e:
            print('Could not parse XML at: ', url)
            print(e)
        
        return soup
    
    @parse_log
    def _parse(self):
        '''
        Method takes SOUP obj with raw data
        and returns list of dicts with rss item tag
        dict_in_self.feed = {
            'title': title tag content
            'link': link to sourse article
            'description': if RSS sourse gave description tag it goes there
            'pubDate': date when article was published
        }
        '''
        items = self.raw.find_all('item') # takes all <item>
        feed = [] # empty list for dict_article
        for item in items: 
            news_item = {} # dict_article
            news_item['title'] = item.title.text # item tag content in <item>
            news_item['link'] = item.link.next_sibling # <link> content , dunno why item.link.text return 'empty_string' mb cuz <link\>
            # if descriprion tag exist take it else leave it None
            try:
                news_item['description'] = item.description.text
            except:
                news_item['description'] = None
            
            news_item['pubDate'] = time_converter(item.pubdate.text) # <pubDate> content
            feed.append(news_item) # add dict to feed list
        
        return feed
    
    def _get_channel(self):
        '''
        Method. Find <channel> name of RSS in raw data
        '''
        return self.raw.find('channel').title.text
    
    @feed_log
    def print_feed(self):
        '''
        Method. Pretty prints self.feed in console

        if limit set up > then 0 and < len(self.feed) print ONLY limit number of feed element
        else prints all feed
        '''
        limit = self.limit # set up limit
        if (limit == None or limit>len(self.feed) or limit < 1): # checked conditions when user will see ALL feed / MB add limit argument check in RssReader MOdule?
            limit = len(self.feed)
        
        if self.channel:
            print(self.channel,'\n') # channel name
        
        if len(self.feed)==0: # check if feed no empty
            print('No articles')
        elif len(self.feed) > 0: # pretty print part ! 
            for article in self.feed[:limit]:
                print('Title: ', article['title'])
                print('Date:  ', article['pubDate'])
                print(f'Link:  ', article['link'],'\n')
                if article['description'] != None:
                    print('Description:', article['description'],'\n')
        print(f'In feed - {len(self.feed)} article(s)')
    
    def to_json(self):
        '''
        Method. Convert feed format to JSON.
        '''
        limit = self.limit
        if (limit == None or limit>len(self.feed) or limit < 1): # Mb i need method to setup the limit ?
            limit = len(self.feed)

        feed = json.dumps(self.feed[:limit]) # convert python list of d in JSON
        print(json.dumps(json.load(feed), indent=4, sort_keys=True)) # print etire JSON in console

# for test only
# kwargs = {
#     'sourse': None,#'https://news.yahoo.com/rss/science',#'https://news.yahoo.com/rss/science',#'https://news.yahoo.com/rss/science','https://news.yahoo.com/rss', 'https://www.onliner.by/feed'
#     'filter_date': '20211013',
#     'limit': None,
#     'verbose': False,
# }
# parser = RssParser(**kwargs)