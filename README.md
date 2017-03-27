# **Flickr Scrapy Bot**

### **Description**

**Flickr Scrapy Bot** is a [web scraping](https://en.wikipedia.org/wiki/Web_scraping) build upon [Scrapy](https://scrapy.org), an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

This bot collects images licensed under **CC** using Flickr API.

### **Requirements**

You must already have:

+ python (2.7 or 3.3 or above)
+ [Flickr API KEY](https://www.flickr.com/services/api/misc.api_keys.html)

You need to install scrapy:

```
$ pip install scrapy  
```
It is recommended to [**set a virtual environment**](https://doc.scrapy.org/en/latest/intro/install.html#using-a-virtual-environment-recommended).

### **Usage**

Clone the repo:

```
$ git clone git@github.com:gcamerli/flickr_scrapy_bot.git
```
Change path:

```
$ cd flickr_scrapy_bot
```
Run crawler setting the API key:

```
$ FLICKR_KEY=******* scrapy crawl flickr
```

Collected images are saved into images dir, which will be created if not exists.

### **Credits**

[@orangain](https://github.com/orangain): sushibot

### **GPL License**

This work is licensed under the terms of [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl.html)
