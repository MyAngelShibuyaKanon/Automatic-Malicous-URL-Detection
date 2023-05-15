from googlesearch import search
from urllib.parse import urlparse

url = "https://zetrotranslation.com/novel/while-trying-my-best-to-get-along-with-my-childhood-friend-who-was-head-over-heels-for-me-the-idol-whom-i-saved-that-one-time-in-history-transferred-in-now-my-school-life-is-in-carnage/#google_vignette"
path = urlparse(url).path
newurl = url.replace(path, "/")
domain = "zetrotranslation.com"

def GoogleIndex(domain):
    try:
        for i in search(domain, sleep_interval=3, num_results=3):
            parsed = urlparse(i)
            parseddom = parsed.netloc
            if parseddom == domain:
                return 1
        else:
            return -1
    except:
        return -1

print(GoogleIndex(domain))