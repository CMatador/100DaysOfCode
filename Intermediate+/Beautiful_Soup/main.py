from bs4 import BeautifulSoup
import requests

# with open('website.html', encoding='utf8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# anchors = soup.find_all(name='a')

# for tag in anchors:
#     print(tag.get('href'))

# heading = soup.find(id='name')
# print(heading.getText())

# compmany_url = soup.select(selector='.heading')
# print(compmany_url)

response = requests.get(url='https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')

article_texts = []
article_links = []

for article in articles:
    anchor_tag = article.find(name='a')
    text = anchor_tag.getText()
    article_texts.append(text)
    link = anchor_tag.get('href')
    article_links.append(link)

article_votes = [int(score.getText().split()[0])
                 for score in soup.find_all(class_='score')]

i = article_votes.index(max(article_votes))

print(article_texts[i])
print(article_links[i])
print(article_votes[i])
