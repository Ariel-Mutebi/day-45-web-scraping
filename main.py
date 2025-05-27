from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
hacker_news_webpage = response.text

let_him_cook = BeautifulSoup(hacker_news_webpage, "html.parser")

article_anchor_elements = let_him_cook.select(".titleline > a")
article_titles = []
article_links = []

for article_anchor_element in article_anchor_elements:
    article_title = article_anchor_element.getText()
    article_link = article_anchor_element.get("href")
    article_titles.append(article_title)
    article_links.append(article_link)

article_score_elements = let_him_cook.find_all(name="span", class_="score")
article_score_texts = [article_score_element.getText() for article_score_element in article_score_elements]
article_score_numbers = [int(article_score_text[0:-7]) for article_score_text in article_score_texts]

highest_article_score = max(article_score_numbers)
index_of_article_with_highest_score = article_score_numbers.index(highest_article_score)

print("Top story on Hacker News:")
print("\tTitle: " + article_titles[index_of_article_with_highest_score])
print("\tRead at: " + article_links[index_of_article_with_highest_score])