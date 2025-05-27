from bs4 import BeautifulSoup

with open("website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, "html.parser")
print("Website-Scrape Report")
print(f"Title: {soup.title.string}")
print(f"Heading-one text: {soup.find(name='h1').getText()}")
print("Text inside heading-threes with class 'heading':")
for h3 in soup.select("h3.heading"):
    print("\t" + h3.getText())
print("Linked webpages:")
for a in soup.select("a"):
    print("\t" + a.get("href"))