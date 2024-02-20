from bs4 import BeautifulSoup
import requests
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# main scraper
def main_scrape(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup



#scrape site 1
def scrape_site1(url):
    soup = main_scrape(url)
    table_body = soup.find("tbody")
    # Find all <tr> tags
    rows = table_body.find_all('tr')
    names = []
    # Loop through each row
    for row in rows:
        # Find the <a> tag with the name
        name_tag = row.find('a')
        name = name_tag.text.lower() if name_tag else 'notfound'

        # # Find the <td> tag with the number
        # number_tag = row.find_all('td')
        # number_tag = number_tag[len(number_tag)-2]
        # number = number_tag.text if number_tag else 'Number not found'
        names.append(name)
    return names



# scrape site 2
def scrape_site2(url):
    soup = main_scrape(url)
    table_body = soup.find_all('font', class_='text2')
    names = []
    for row in table_body:
        name = row.text.lower()
        names.append(name)

    return  names


# scrape site 3

def scrape_site_3(url):
    final_names = []
    for i in range(1, 16):
        soup = main_scrape(url+str(i)+'/?sort=alpha')
        tables = soup.find_all('table', class_='table table-striped table-baby-names clearfix list-names name-list-boy')
        for table in tables:
            names = table.find_all("strong")
            names = [name.text.lower() for name in names]
            final_names.extend(names)
    return final_names


# scrape site 4
def scrape_site_4(url):
    soup = main_scrape(url)
    list_names = soup.find('ol')
    names = list_names.find_all('li')
    names = [name.text.lower() for name in names]
    return names



site_1_url = 'https://forebears.io/india/forenames'
site_2_url = 'https://studentsoftheworld.info/penpals/stats.php?Pays=IND'
site_3_url = 'https://www.mamanatural.com/baby-names/boys/origins/indian-sanskrit-boy-names/page/'
site_4_url = 'https://siachenstudios.com/list/common-indian-names/'


site_1_names = scrape_site1(site_1_url)
site_2_names = scrape_site2(site_2_url)
site_3_names = scrape_site_3(site_3_url)
site_4_names = scrape_site_4(site_4_url)

site_2_names = site_2_names[11:200]


final_common_names = [item for sublist in [site_1_names, site_2_names, site_3_names, site_4_names] for item in sublist]
final_common_names = final_common_names.remove('notfound')

# Join the elements in my_list into one string, separated by space
text = ' '.join(final_common_names)
# Create a WordCloud object with some parameters
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text)

# Display the generated image
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()