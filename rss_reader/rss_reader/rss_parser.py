# https://news.yahoo.com/rss
# https://news.yahoo.com/rss/science
from datetime import date, datetime
import requests
import json
import re
from unidecode import unidecode
from bs4 import BeautifulSoup
from fpdf import FPDF
from rss_reader.logs import get_rss_log, parse_log, feed_log, exec_time, time_converter # import decorators responsible for logs output
from os import link, path,remove


class RssParser:
    """
    Main part of programm
    Class witch response for get rss, manipulate rss feed in human readable format

    takes arguments from RSS reader class
    decorators above methods used for --verbose flag
    """
    def __init__(self,**kwargs):
        self.verbose = kwargs['verbose'] # verbose arg from RssReader class (RRC)
        self.limit = kwargs['limit'] # limit arg from
        self.local_storage_path = path.join(path.dirname(__file__), 'local_storage.json') # path to dir with rss_reader.py
        self.feed = None # for news
        self.local_data = None
        self.filter_date = kwargs['filter_date']
        self.sourse = kwargs['sourse']

    @exec_time
    def main(self):
        """
        Main functionality method. Takes rss feed from URL or from
        local storage and convert it to readable fromat.
        """
        try:
            self._make_local_storage()
        except Exception as e:
            print('Cant create local storage file')
        try:
            self.local_data = self._read_local_storage()
        except Exception as e:
            print('Cant read news feed from local storage')
        if self.filter_date:
            try:
                self.feed = self._local_feed(sourse=self.sourse, filter_date=self.filter_date) # get local_feed
                self.channel = ''
            except Exception as e:
                print(f'Cant parse news from local storage.\n\n{e}\n')
        else:
            try:
                self.raw = self._get_rss(self.sourse) # connect to source URL, get XML content and returne SOUP obj
                self.channel = self._get_channel() # RSS feed name
            except Exception:
                print(f'Some trouble with connection to {self.sourse}')
            try:
                self.feed = self._parse() # list of dicts with rss news (items) after parsing
                self._save_feed(self.sourse)
            except Exception as e:
                print(e)
                print(f'Cant parse feed from {self.sourse}. Make sure its RSS format')

    def _local_feed(self,sourse = None, filter_date = None):
        """
        Method. Loads news feed from local storage
        """
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
        return feed

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
            if self.verbose:
                print ('New sourse, add it to local storage')
            new_source_feed = {
                'feed': self.feed,
                'cached': date.today().strftime("%d/%m/%Y")
            }

            self.local_data[source] = new_source_feed
            if self.verbose:
                print('ADD NEW SOURSE TO LOCAL STORAGE')
        
        with open(self.local_storage_path, mode='w') as outputfile:
            json.dump(self.local_data, outputfile)
        
        if self.verbose:
            print('WRITE LOCAL STORAGE SECCESSFUL')

    @get_rss_log 
    def _get_rss(self,url):
        '''
        Takes RSS feed url try to connect
        Return SOUP object with XML content (RSS FEED)
        '''
        resp = requests.get(url) # request to RSS URL
        soup = BeautifulSoup(resp.content, features='lxml', from_encoding='utf-8') # try to convert pure XML to SOUB object (raw data)
        
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

            title = item.title.text
            title = title.replace('<![CDATA[', '')
            title = title.replace(']]>','')
            news_item['title'] =  title# item tag content in <item>
            
            news_item['link'] = item.link.next_sibling # <link> content , dunno why item.link.text return 'empty_string' mb cuz <link\>
            # if descriprion tag exist take it else leave it None
            try:
                description = item.description.text
                description = description.replace('<![CDATA[', '')
                description = description.replace(']]>','')
                news_item['description'] = description
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
        print(f'In feed - {len(self.feed[:limit])} article(s)')
    
    def to_json(self):
        '''
        Method. Convert feed format to JSON.
        '''
        limit = self.limit
        if (limit == None or limit>len(self.feed) or limit < 1): # Mb i need method to setup the limit ?
            limit = len(self.feed)

        feed = json.dumps(self.feed[:limit]) # convert python list of d in JSON
        print(json.dumps(json.load(feed), indent=4, sort_keys=True)) # print etire JSON in console
    
    def to_pdf(self,path=None):
        """
        Method. Turns feed into pdf format.
        """
        limit = self.limit # set up limit
        if (limit == None or limit>len(self.feed) or limit < 1): # checked conditions when user will see ALL feed / MB add limit argument check in RssReader MOdule?
            limit = len(self.feed)
        
        text = ''
        
        if self.channel:
            text += f'{self.channel} \n\n' # channel name
        if len(self.feed)==0: # check if feed no empty
            print('No articles')
        
        for article in self.feed[:limit]:
            text += f"Title: {article['title']}\nDate: {article['pubDate']}\nLink: {article['link']}\n"
            if article['description']:
                text += f"Description: {article['description']}"
            text +=f'\n'
        
        text = unidecode(text) # turns utf-8 into latin-1
        
        pdf = FPDF()

        pdf.add_page() 

        pdf.set_font("Arial", size = 12) 
        pdf.multi_cell(200, 10, txt = text,) 

        if path:
            pdf.output(path)
        else:
            pdf.output('feed.pdf')
    
    def to_html(self):
        """
        Method turns feed into html
        """
        limit = self.limit # set up limit
        if (limit == None or limit>len(self.feed) or limit < 1): # checked conditions when user will see ALL feed / MB add limit argument check in RssReader MOdule?
            limit = len(self.feed)
        
        text = ''
        
        if self.channel:
            text += f'{self.channel} \n\n' # channel name
        if len(self.feed)==0: # check if feed no empty
            print('No articles')
        
        html = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
        """ # text obj for html code
        for article in self.feed[:limit]:
            title_content = f"\t\t\t<h3>{article['title']}<h3>\n"
            date_content = f"\t\t\t<p>PubDate: {article['pubDate']}</p>\n"
            link_content = f"\t\t\t<a href='{article['link']}'>Source</a>\n"
            descr_content = f"\t\t\t"
            
            article_content = '\t\t<div>\n'
            article_content += title_content + date_content + link_content + descr_content + '</div>\n'
            html += article_content
        html +='    </body>\n</html>'

        with open('./feed.html', 'w') as doc:
            doc.write(html)



        
# # for test only
# kwargs = {
#     'sourse': 'https://news.yahoo.com/rss',#'https://news.yahoo.com/rss/science',#'https://news.yahoo.com/rss/science',#'https://news.yahoo.com/rss/science','https://www.onliner.by/feed'
#     'filter_date': None,
#     'limit': None,
#     'verbose': False,
# }
# parser = RssParser(**kwargs)
# parser.to_html()

