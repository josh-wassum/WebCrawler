# def file_entry_point_crawl(self):
#         with open('crawl-entry-point.txt') as fh:
#             urls = fh.readlines()

#         for url in urls:
#             url = url.strip()
#             rp = urobot.RobotFileParser()
#             rp.set_url(url + "/robots.txt")
#             rp.read()
#             robots = url + '/robots.txt'
#             has_robots = does_url_exist(robots)
#             get_all_url(url, has_robots, rp)