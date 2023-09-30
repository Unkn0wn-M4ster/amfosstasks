import requests
from bs4 import BeautifulSoup
import csv
import discord
from datetime import datetime

def scrape_livescore():
    ESPN_URL = 'https://www.espncricinfo.com/live-cricket-score'
    result = requests.get(ESPN_URL)
    doc = BeautifulSoup(result.text, 'html.parser')

    tags = doc.find_all(class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo") 
    tags1 = doc.find_all(class_='ds-text-compact-xs ds-mr-0.5') ##Gives the over and things 
    tags2 = doc.find_all(class_="ds-text-tight-xs ds-truncate ds-text-typo-mid3")
    tag2_1 = doc.find(class_="ds-text-compact-xs ds-mr-0.5")
    tag3 = doc.find_all('strong')  ##Score Value
    tag3_1 = doc.find_all('span')
    titletag=doc.find(class_="ds-inline-flex ds-items-start ds-leading-none !ds-inline")
    T1=doc.find_all(class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')    
    T2=doc.find(class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
    if tags and tags1 and tags2:
        tag = tags[0]
        tag1 = tags1[0]
        tag2 = tags2[0]
        print
        if tag3 and tag3_1:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = (
                f"{ T1[0].text,'VS',T1[1].text,titletag['title']}{tags1[1].text} {tag2.text}\n: {tag3[0].text}To {tag3[1].text}\n{tag.text}\n{tag3_1[1].text}{tag1.text}\n")
            append_to_csv(timestamp, data)
            return data
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = f"{tag['title']} {tag2_1.text}\n{tag.text}\n{tag1.text}"
            append_to_csv(timestamp, data)
            return data
    else:
        return "No live score information found."

def append_to_csv(timestamp, data):
    with open('livescore.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, data])

a=scrape_livescore()
print(a)