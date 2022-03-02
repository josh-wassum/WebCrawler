import requests

class Validator():
    
    def does_url_exist(self, url):
        try:
            url_request = requests.head(url)
            if url_request.status_code < 400:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(e)

    