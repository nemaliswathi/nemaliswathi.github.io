from bs4 import BeautifulSoup
import requests
import numpy as np

# this is the base URL to find hindu boy names
base_url = 'https://www.prokerala.com/kids/baby-names/hindu/boy/'

# checking & reading the base url page
page = requests.get(base_url)
# getting the page source using beautiful soup
soup = BeautifulSoup(page.content, "html.parser")

# checking if multiple pagination exists.
pages = soup.find("ul", class_="pagination")
# If the pagination exists, then it finds that last page number.
last_page = pages.find("a", title="Last Page").text

# list to store all the names
final_names = []

# getting names from each page....
for i in range(1, int(last_page)+1):
    page_url = base_url + 'page-'+str(i)+'.html'
    page_get = requests.get(page_url)
    page_soup = BeautifulSoup(page_get.content, "html.parser")
    page_table = page_soup.find("table", class_="table name-list-wrapper bordered")
    table_body = page_table.find("tbody")
    names_list = table_body.find_all("a")
    for name in names_list:
        final_names.append(name.text.lower())



# save the final list for further use...
np.save('final_list_names.npy', np.array(final_names, dtype=object), allow_pickle=True)
