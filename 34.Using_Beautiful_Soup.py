import bs4
import requests
"""headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0'}
request = requests.get("https://www.amazon.co.uk/Automate-Boring-Stuff-Python-Programming/dp/1593275994", headers=headers)
request.raise_for_status()"""

res = requests.get('https://www.bbc.co.uk/news/uk-england-london-53288489')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')#pass the response to BS and chose the html parser
print(soup.select('html#responsive-news.orb-js.id-svg.ctm.ff.flex.orb-more-loaded.se-no-touch.grunticon body#asset-type-sty.device--group4.device--wide.no-touch div.direction div#orb-modules div#site-container div#page.configurable.story div div.container div.container--primary-and-secondary-columns.column-clearfix div.column--primary div.story-body h1.story-body__h1'))
elements = soup.select('html#responsive-news.orb-js.id-svg.ctm.ff.flex.orb-more-loaded.se-no-touch.grunticon body#asset-type-sty.device--group4.device--wide.no-touch div.direction div#orb-modules div#site-container div#page.configurable.story div div.container div.container--primary-and-secondary-columns.column-clearfix div.column--primary div.story-body h1.story-body__h1')

print(elements[0].text)