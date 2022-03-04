# Overview

This is a web crawler using Beautiful Soup and the Requests libraries in python. The crawler takes user input and validates whether or not the url is a valid url. If it is it then crawls the initial page and creates a entry_point list within a txt file. We then call a file_crawl object that allows us to loop through and crawl all items found within this entry_point file and log them using a log file and within the entry point file. Using some simple logic we are able to ensure that each item added to the crawl_entry point file is unique and does not already exist within the file. 

Eventually this application will also include a web based component to allow a user to run the crawl from the web and view a graph of the data. Currently we can only crawl the urls found on the initial url provided, however eventually I will add functionality to allow a user to crawl an entire site. Lastly the crawler automatically checks for a robots.txt file, however in the future I would to make it so that the user can specify whether or not they want to check for a robots.txt file.

This application is a moderately complex web crawler demonstrating my ability to use python to gather large amounts of data. The main purpose of this program was to learn more about the various capabilities within python when it comes to data mining. Additionally I find the ability to crawl large webpages to be a fund project and something I have a desire to learn more about.

[Software Demo Video](https://youtu.be/bQNID4FuB4M)

# Development Environment

This program was developed using Visual Studio Code and GitHub.

Languages and Libraries used: 
* [python](https://www.python.org/)
* [urllib](https://docs.python.org/3/library/urllib.html)
* [logging](https://docs.python.org/3/howto/logging.html)
* [getpass](https://docs.python.org/3/library/getpass.html)
* [time](https://docs.python.org/3/library/time.html)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [requests](https://pypi.org/project/requests/)
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Useful Websites

* [Stack Overflow](https://stackoverflow.com/)
* [BeautifulSoup docs](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [urlib docs](https://docs.python.org/3/library/urllib.html)
* [requests docs](https://pypi.org/project/requests/)

# Future Work

* Implement full site crawl functionality.
* Allow user to choose to check for robots.txt.
* Create web app for user interface and data visualization.