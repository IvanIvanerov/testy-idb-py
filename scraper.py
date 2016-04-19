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

yelpurl = "http://www.yelp.ca/search?find_desc=gyms&find_loc=Calgary%2C+AB&start="
index = 1

for x in range(0, 300, 10):
    print x
    html = scraperwiki.scrape(yelpurl + str(x))
    time.sleep(.2)
    root = lxml.html.fromstring(html)
    
    name = root.cssselect('a.biz-name')
    address = root.cssselect('address')
    phone = root.cssselect('span.biz-phone')
    cat = root.cssselect('div.price-category')
    
    for i in range(len(name)):
        category = ""
        
        my_cats = cat[i].cssselect('span.category-str-list a')
        for j in range(len(my_cats)):
            category += ", " + my_cats[j].text.encode('utf-8').decode('utf-8').strip()
        
        scraperwiki.sqlite.save(unique_keys=["pk"], data={
                'pk': index,
                'name': name[i].text.encode('utf-8').decode('utf-8').strip(),
                'address': address[i].text.encode('utf-8').decode('utf-8').strip(),
                'phone': phone[i].text.encode('utf-8').decode('utf-8').strip(),
                'category': category,
                'url': name[i].attrib['href'].strip()
            })
        index += 1
        #print name[i].text.encode('utf8')
       # print address[i].text.encode('utf8')
       # print phone[i].text.encode('utf8')

    
