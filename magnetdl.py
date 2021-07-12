import cloudscraper
from bs4 import BeautifulSoup


class Magnetdl():
    def __init__(self, key):
        self.key = key
        cat = self.key[0]
        self.url = f"https://www.magnetdl.com/{cat}/{self.key}/"

        self.main_functions()

    def main_functions(self):
        self.scrap_parce()
        self.find_in_content()
        self.get_info()


    def scrap_parce(self):
        scraper = cloudscraper.create_scraper()
        content = scraper.get(self.url).text
        self.bs = BeautifulSoup(content, "lxml")


    def find_in_content(self):
        self.magnet = self.bs.findAll(class_="m")
        self.title = self.bs.findAll(class_="n")
        self.size = self.bs.findAll("tr")


    def get_info(self):
        size_info = []
        title_info = []
        magenet_info = []

        for s in self.size:
            try:
                size_info.append(s.text.split("Movie")[1][1:-2])
            except:
                pass

        for info in self.title:
            title_info.append(info.a["title"])

        for link in self.magnet:
            magenet_info.append(link.a["href"])

        return title_info, magenet_info, size_info


def get(key):
    json = []
    mg = Magnetdl(key)
    title, magnet, size = mg.get_info()

    try:    
        for i in range(len(title)):
            json.append({"title": title[i],"size": size[i],
            "magenet": magnet[i]})
    except:
        pass

    return json
