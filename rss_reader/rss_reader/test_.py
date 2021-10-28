import unittest
from .rss_parser import RssParser

class RssParserTestToHTMLMethod(RssParser):
    """Subclas for testing to_html() method"""
    def __init__(self, feed, limit, channel):
        self.feed = feed
        self.limit = limit
        self.channel = channel

class TestParser(unittest.TestCase):
    
    def test_to_html(self):
        feed = [{
            'title': 'TEST TITLE',
            'pubDate': '20211028',
            'link': 'test_link.test',
        },
        {
            'title': 'TEST TITLE #2',
            'pubDate': '20211028',
            'link': 'test_link_2.test',
        },
        ]

        answ = '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
        		<div>
			<h3>TEST TITLE<h3>
			<p>PubDate: 20211028</p>
			<a href='test_link.test'>Source</a>
			</div>
		<div>
			<h3>TEST TITLE #2<h3>
			<p>PubDate: 20211028</p>
			<a href='test_link_2.test'>Source</a>
			</div>
    </body>
</html>'''
        
        limit = None
        channel = 'Test Channel'
        
        parser = RssParserTestToHTMLMethod(feed, limit, channel)
        parser.to_html()

        html_content=''

        with open('./feed.html', 'r') as f:
            html_content = f.read()
        
        self.assertEqual(html_content,answ)
        
if __name__ == '__main__':
    unittest.main()