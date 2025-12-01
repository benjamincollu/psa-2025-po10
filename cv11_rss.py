import xml.etree.ElementTree as ET
import requests

RSS_URL = "https://www.bazos.sk/rss.php?rub=pc"

def getRSS():
    resp = requests.get(RSS_URL)
    print(resp.status_code)
    rss_text = resp.text
    root = ET.fromstring(rss_text)

    out = []
    for channel in root:
        for item in channel:
            title = ""
            link = ""
            description = ""
            for child in item:
                if child.tag == "title":
                    title = child.text
                if child.tag == "link":
                    link = child.text
                if child.tag == "description":
                    description = child.text
                out.append([title, link, description])
    return out
getRSS()