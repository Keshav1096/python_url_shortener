import string
import random  # define the random module
from mongo import MongoConnection

mongo = MongoConnection()


class Helper:
    def __init__(self, url, host_name):
        self.url = url
        self.host_name = host_name
        pass

    def genShortCode(self):
        S = 10
        ran = "".join(random.choices(string.ascii_lowercase + string.digits, k=S))
        return str(ran)

    def getShortUrl(self):
        shortCode = self.genShortCode()
        urlObj = {
            "shortCode": shortCode,
            "shortUrl": self.host_name + shortCode,
            "longUrl": self.url,
        }

        try:
            mongo.insert(urlObj)
            return urlObj
        except Exception:
            return False


def getLongUrl(short_code):
    result = mongo.find({"shortCode": short_code})
    
    if result is not None:
        try:
            long_url = result["longUrl"]
            return long_url
        except:
            return None
    return result
