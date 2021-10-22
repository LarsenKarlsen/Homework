from setuptools import setup
setup(
    name = 'rss-reader',
    version='0.1',
    packages=['rss-reader'],
    entry_points = {
        'console_scripts':['rss-reader=rss-reader.__main__:main']
    }
)