# -*- coding: utf-8 -*-
import requests
import time
import pprint
from bs4 import BeautifulSoup

#url = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2020&value(semekikn)=1&value(kougicd)={}&value(crclumcd)=01011800002019"
#url = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2020&value(semekikn)=1&value(kougicd)=25273&value(crclumcd)=01011800002019N"
base_url = "https://tora-net.sti.chubu.ac.jp/syllabusv3/slbssbdr.do?value(risyunen)=2020&value(semekikn)=1&value(kougicd)={}&value(crclumcd)=01011800002019N"

def scraper(url):
    html = requests.get(url)
    shot = BeautifulSoup(html.text, "html.parser")

    html_data = shot.find_all(class_="kougi")

    datas = {}

    datas = {"jp-title": html_data[0].prettify().split("\n")[1].strip(),
             "en-title": html_data[1].prettify().split("\n")[1].strip(),
             "id": html_data[2].prettify().split("\n")[1].strip(),
             "teacher": html_data[3].prettify().split("\n")[3].strip().replace("\u3000", " "),
             "tani": html_data[4].prettify().split("\n")[1].strip(),
             "gakunen": html_data[5].prettify().split("\n")[1].strip(),
             "ziki": html_data[7].prettify().split("\n")[3].replace("\u3000", " "),
             "details": html_data[8].prettify().split("\n")[1].strip(),
             "skil": html_data[9].prettify().split("\n")[1].strip().replace("\u3000", " ")}

    datas["ziki"] =  datas["ziki"].replace(datas["teacher"], "").strip().replace("：", "")
    
    return datas


lists = []
url_id = 25273

for i in range(5):
    url = base_url.format(int(url_id + i))
    print(url)
    
    data = scraper(url)
    lists.append(data)
    time.sleep(2)

pprint.pprint(lists)

