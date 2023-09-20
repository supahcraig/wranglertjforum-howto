# wranglertjforum-howto
Scrapes how-to sub-forum to pull links &amp; descriptions to build a how-to index page on www.wranglertjforum.com

## Version 1:

links were manually collected & categorized, then formatted into BBCode to be inserted into the forum index page.   

---

## Version 2:  

Links will be scraped using BeautifulSoup, and then looked up against the existing categorization.   This will allow for the link in the assembled index page to use the same capitalization as the thread title.   V1 uses a hygiened version of the link itself as the title, which removes special characters, and does things like change "TJ" to "tj" which is annoying and I can do better.
