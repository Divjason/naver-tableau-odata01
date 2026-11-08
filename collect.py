import os
import re
import requests
import xml.etree.ElementTree as ET

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

URL = "https://naverapihub.apigw.ntruss.com/search/v1/blog"

headers = {
  "X-NCP-APIGW-API-KEY-ID": os.getenv("X-NCP-APIGW-API-KEY-ID"),
  "X-NCP-APIGW-API-KEY": os.getenv("X-NCP-APIGW-API-KEY")
}

params = {
  "query": "에버랜드",
  "display": 100,
  "start": 1,
  "sort": "date",
  "format": "xml"
}

response = requests.get(
  URL,
  headers=headers,
  params=params,
  timeout=20
)

path = Path("data/naver_blog.xml")
path.write_bytes(response.content)

root = ET.fromstring(response.content)
items = root.findall("./channel/item")

for item in items[:3] :
  print({
    "title": item.findtext("title"),
    "bloggername": item.findtext("bloggername"),
    "postdate": item.findtext("postdate")
  })
