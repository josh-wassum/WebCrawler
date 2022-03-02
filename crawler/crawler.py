import urllib.robotparser as urobot
import logging
import getpass
import time
from datetime import datetime
from crawler.validator import Validator
from crawler.crawl import Crawl

class Crawler ():

    def __init__(self):
        self.base_url = ""
        self.validator = Validator()


    def start_crawls(self):

        # Valid url: 'https://ra11yup.linearbsystems.net'
        self.base_url = input("Please type a full URL to crawl: ")
        valid_url = self.validator.does_url_exist(self.base_url)
        while valid_url == False:
            base_url = input("Invalid URL, please try again: ")
            valid_url = self.validator.does_url_exist(self.base_url)
            

        d = datetime.today()
        epoch_time = time.mktime(d.timetuple())
        logging.basicConfig(filename=f'logs/crawl-{getpass.getuser()}.{epoch_time}.log', level=logging.DEBUG )
        rp = urobot.RobotFileParser()
        rp.set_url(self.base_url + "/robots.txt")
        rp.read()
        robots = self.base_url + '/robots.txt'
        f = open('res/crawl-entry-point.txt', 'w')
        f.close()
        has_robots = self.validator.does_url_exist(robots)
        initial_crawl = Crawl(self.base_url, has_robots, rp)
        initial_crawl.get_all_url()
        # file_entry_point_crawl()
