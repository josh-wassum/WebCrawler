import urllib.robotparser as urobot
import urllib.request
import logging
import requests
from bs4 import BeautifulSoup

class Crawl():
    def __init__ (self, url, has_robots, rp):
        self.url = url
        self.has_robots = has_robots
        self.rp = rp
    def get_all_url(self):

        if self.rp.can_fetch("*",self.url) or not self.has_robots:
            url_list = []

            # Get the input url web page HTML content.
            html_data = urllib.request.urlopen(self.url).read().decode("utf-8")

            # Create an instance of BeautifulSoup with the above HTML data.
            soup = BeautifulSoup(html_data, features='html.parser')

            # Get all HTML a tag on the web page in a list.
            tag_list = soup.find_all('a')

            # Loop the above tag list.
            for tag in tag_list:

                # Get the HTML a tag href attribute value.
                href_value = str(tag.get('href'))
                if not 'http' in href_value:
                    href_value = self.url + "/" + href_value

                if href_value.split('#') not in url_list:
                    url_list.append(href_value)

            # Removing duplicate values from the url list.
            final_url_list = set(url_list)
            
            # Looping through the url list and adding url to crawl entry.
            for url in final_url_list:
                page = requests.head(url)
                f = open('res/crawl-entry-point.txt', 'a+')
                urls = f.readlines()
                if page.status_code < 400 and url not in urls:
                    f.write(f'{url}\n')

                # TEST
                print(url)
                print(page.status_code)
                logging.info('Page status for {} is: {}'.format(url,page.status_code))
            f.close()

        else:
            print("Can't scrape.")

    