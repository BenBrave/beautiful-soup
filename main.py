from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news") #get new from website
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
soup.find(name="a", rel="nofollow").decompose() # remove advertising content
article_tag = soup.find_all(name="a", class_="titlelink") #get article
article_upvote = soup.find_all(name="span", class_="score") # get vote
titles = []
links = []
scores = []
for article in article_tag: #split article into title list and link list
    titles.append(article.string)
    links.append(article.get("href"))

for score in article_upvote: #split vote into list
    scores.append(score.text)

score_int = []
for score in scores: #turn vote from string to integer
    score = score.split()
    score_int.append(int(score[0]))

new_list =[]
for i in range(0,len(score_int)): #combine vote link and title into one list
    new_list.append({"title": titles[i],"link": links[i], "score": score_int[i]})

max_item = max(score_int)
print(new_list[score_int.index(max_item)])






















# with open("index.html", "r") as file:
#     data = file.read()
#     print(type(data))
#
# soup = BeautifulSoup(data, "html.parser")
# print(soup.p.string)
# print(soup.find_all(name="a"))
# # all_anchor_tags = soup.find_all(name="a")
# #
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.string)
# other = soup.find(name="h3", class_="other")
# print(other.get('class'))
# company_url = soup.select("a")
# print(company_url)
