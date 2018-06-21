from bs4 import BeautifulSoup
import urllib, random, re, mechanize

#make soup
url = 'https://www.hdwallpapers.in'
response = urllib.urlopen(url)
soup = BeautifulSoup(response, 'lxml')

#find categories
selected_categories = ['nature', 'beach', 'digital_universe', 'planes', 'animals', 'bikes', 'cars', 'dreamy', 'fantasy_girls']
found_categories = soup.find(id='tabs-categories').find_all('a')
found_links = []

for link in found_categories:
    for category in selected_categories:
        if re.match('^/' + category, link['href']):
            found_links.append(link['href'])

#trying this piece of code here to simplify things
#found_links = soup.find(id='tabs-categories').find_all(href=re.compile('|'.join(selected_categories)))

#select random category
random_index = random.randint(0, len(found_links) -1)
selected_category = found_links[random_index]
selected_category_url = url + selected_category

#navigate to selected category
browser = mechanize.Browser()
response = browser.open(selected_category_url)
soup = BeautifulSoup(response, 'lxml')
section_toppage = max(int(link.text) for link in soup.find('div', class_='pagination').find_all('a') if link.text.strip().isdigit())

#debbuging
print found_links
