# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
import scraperwiki
import lxml.html
import re
import time
shopurl = "http://iledebeaute.ru/shop/fragrance/page"
index = 1
for x in range(1, 50, 1):
    print x
    html = scraperwiki.scrape(shopurl + str(x))
    time.sleep(.2)
    root = lxml.html.fromstring(html)
    brand = root.cssselect('brand')
    pn = root.cssselect('pn')
    price = root.cssselect('p_price')
    articul = root.cssselect('articul')
     for i in range(1,len(brand),1):
        print brand + " " + pn + " " + price + " " + articul
        scraperwiki.sqlite.save(unique_keys=["pk"], data={
                'pk': index,
                'brand': brand[i],
                'pn': pn[i],
                'price': price[i],
                'articul': articul[i]
            })
        index += 1
        #print name[i].text.encode('utf8')
       # print address[i].text.encode('utf8')
       # print phone[i].text.encode('utf8')

    
