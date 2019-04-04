from bs4 import BeautifulSoup
from flask import Flask
import requests
import json
import re

app = Flask(__name__)

@app.route("/")
def getIcons():
    page = requests.get('')
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup.find_all(href=re.compile("html")))
    icons = soup.find_all("i", {"class": "bbva-icon"})
    return 'demo'



if __name__ == "__main__":
    app.run()