import requests
import json

links = ["https://www.interia.pl/", "https://samsungu.udemy.com/organization/home/",
          "https://p2mforum.info/", "www.lola.ddd", "www.odd.idd"]

def create_file_with_links():
    with open("links.json", "w") as file:
        json.dump(links, file)


def check_links_are_working():
    pages_exists = 0
    pages_does_not_exists = 0


    with open("links.json", "r") as file:
        websites = json.load(file)
        for items in websites:
            try:
                if requests.get(items.replace("\"","")).status_code == 200:
                    pages_exists +=1
            except:
                pages_does_not_exists +=1

        print("Pages that exists:", pages_exists)
        print("Pages that does not exists:", pages_does_not_exists)

create_file_with_links()
check_links_are_working()

