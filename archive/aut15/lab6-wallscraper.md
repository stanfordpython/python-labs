# Python Week 6

## Congratulations!
You've made it through week 6! Midterms are almost over (*cough* CS107 *cough*), and we've more or less finished discussing the syntax of the Python language. At this point, you know most of the important stuff about the language itself. Therefore, we'll spend most of the rest of the time in class going over useful builtin- or third-party modules that are omnipresent in the Python ecosystem. However, as far as the language itself goes, you have all become skilled in the art of the Python language.

## Feedback
Before you begin the lab, please take a moment to give us feedback on how we're doing.

[Click Me! I'm a Typeform =D](https://stanfordpython.typeform.com/to/kehII6)

## Overview
Generally, these labs have focused on exploring nuances of the Python language - whether the syntax, semantics, or style of thinking. However, since we've know almost wrapped up talking about the language, labs will become a period of time for you to build something awesome.

In particular, today you will write a program that automatically downloads the top wallpaper from reddit every night to your local computer, and optionally sets it as your desktop background. So cool!

## Getting Set Up
### Summary
Before we begin, we need to get our development environments properly working. Because requests is a third-party library, we first need to install it using `pip3`. Let's create a new virtual environment so that all of our installations for this project will live in one isolated place.

### Creating a virtual environment
```Bash
sredmond:~$ cd to/your/python/folder
sredmond:~$ pyvenv wallscraper
sredmond:~$ source wallscraper/bin/activate
(wallscraper) sredmond:~$
```
The process of activating the virtual environment should cause a `(wallscraper)` text to be prepended to your normal command line prompt.

To ensure that your virtual environment is properly set up, run `which python` and you should see a path to an executable inside the wallscraper folder.
```Bash
(wallscraper) sredmond:~$ which python
/Users/sredmond/more/folders/wallscraper/bin/python
```
If you see something drastically different, please let us know, and we'll try our best to troubleshoot.

### Installing `requests`
While Python's standard library has a lot of functionality included, we sometimes prefer to work with third-party modules. For this project, we're going to use `requests`, a fantastic web client for Python written by Kenneth Reitz.

While your virtual environment is activated, run `pip3 install requests`
```Bash
(wallscraper) sredmond:~ pip3 install requests
Collecting requests
    # Miscellaneous stuff here
Installing collected packages: requests
Successfully installed requests-2.8.1
```
If the `requests` library fails to install, flag one of us down.

To ensure that you've successfully installed requests, enter an interactive session and run `import requests`
```Python3
$ python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>>
```
If you get back the interactive prompt `>>>`, everything is installed correctly. If, on the other hand, you see
```Python3
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'requests'
```
then something has gone wrong - please let one of us know.

## Wallscraper
### Fetching Data from the Internet
The internet is full of many awesome things: [cat videos](https://www.youtube.com/v/2XID_W4neJo), [the most awesome people](https://www.facebook.com/), and most importantly, [reddit](https://www.reddit.com/r/python).

Take a (brief) look at [reddit.com/r/wallpapers](https://www.reddit.com/r/wallpapers) - there is so much happening on the page. Images are being loaded, buttons ask you to click them, ads on the side demand your attention - it can be hard to find the data. Take a look at [reddit.com/r/wallpapers.json](https://www.reddit.com/r/wallpapers.json) (note the suffix `.json`). By adding this suffix to the query, we get back a rich data structure representing, in this case, posts on /r/wallpapers. 

In order to fetch data from the internet, we will use the `requests` module.

The following is sample code showing how one could use the `requests` module.
```Python3
>>> import requests
>>> response = requests.get('http://stanfordpython.com')
>>> print(response)
<Response [200]>
>>> print(type(response))
<class 'requests.models.Response'>
```

The `get` function defined by the `requests` module returns a custom response object that encapsulates the response returned by the server. (There are similar `post`, `put`, and `delete` functions defined by `requests`). 

This response object supports a lot of attribute references:
```
>>> response.<tab>
response.apparent_encoding      response.history                response.raise_for_status
response.close                  response.is_permanent_redirect  response.raw
response.connection             response.is_redirect            response.reason
response.content                response.iter_content           response.request
response.cookies                response.iter_lines             response.status_code
response.elapsed                response.json                   response.text
response.encoding               response.links                  response.url
response.headers                response.ok
```

In particular, I want to call a few to your attention:
```Python3
# returns the raw server response, as a string
response.content

# returns an iterator over the server response - useful if the server responds with a lot of data.
response.iter_content()

# If and only if the content represents JSON-encoded data, return the data decoded into a Python dictionary
response.json()

# Returns true if and only if there were no errors in client-server communication. 
response.ok

# Raises an exception if the status is bad, otherwise does nothing
response.raise_for_status()
```

More information on the `requests` library can be found [here](http://docs.python-requests.org/en/latest/)

### Query Subreddit Data
In this section, your task is to write a function `query` that accepts as an argument a subreddit to query (e.g. `'wallpapers'` or `'funny+gifs'`), and returns the JSON server response from reddit as a Python dictionary. You can add any additional positional or keyword arguments as you see fit.

Place this, and any function helpers you create, into a file called `query.py`.

Your function must handle all of the following scenarios:
* There is no internet connection
* The user supplies a string that doesn't represent a valid subreddit
* The requests module, in particular the `get` function, throws any exception from `requests.exceptions` (hint: look through [the source code](https://github.com/kennethreitz/requests/blob/master/requests/exceptions.py) to find the base exception class for the `requests` package.) 
* reddit responds with a status that is not `ok`

In all of these situations, your query function should print out an informative error message.

To test this function, write a few lines of code in a new file called `wallscraper.py` that call the `query` function (from the `query` module) with some reasonable subreddit name as an argument. You should inspect the response to make sure it seems reasonable. Try writing a quick Python script to check how many posts in the response data had a score over 1000.

#### Note: Rate Limits
It's possible that Reddit will impose a rate limit on us, because we're making too many requests to its server. If this is the case, Reddit will respond with a <Response [429]>, which specifically means: *429 Client Error: Too Many Requests.* If this is the case, add `headers={'User-Agent', <sunet_id>}` as a keyword argument to `requests.get`. For instance, I would call it as `requests.get('http://www.website.com', headers={'User-Agent': 'sredmond'})`. This should get around the rate-limit problem.

### Building a Post Class
For this task, you will need to build a `Post` class in a file called `post.py`.

### Reddit's `Post` data
Posts on Reddit maintain a ton of information. The lowest-level 'post' object in Reddit's response might look something like this:
```
raw_data = {
    'approved_by': None,
    'archived': False,
    'author': 'PCGamingOnly',
    'author_flair_css_class': None,
    'author_flair_text': None,
    'banned_by': None,
    'clicked': False,
    'created': 1445995723.0,
    'created_utc': 1445966923.0,
    'distinguished': None,
    'domain': 'i.imgur.com',
    'downs': 0,
    'edited': False,
    'from': None,
    'from_id': None,
    'from_kind': None,
    'gilded': 0,
    'hidden': False,
    'hide_score': False,
    'id': '3qg0if',
    'is_self': False,
    'likes': None,
    'link_flair_css_class': None,
    'link_flair_text': None,
    'locked': False,
    'media': None,
    'media_embed': {},
    'mod_reports': [],
    'name': 't3_3qg0if',
    'num_comments': 70,
    'num_reports': None,
    'over_18': False,
    'permalink': '/r/wallpapers/comments/3qg0if/mech_warfare/',
    'post_hint': 'image',
    'preview': {
        'images': [{
            'id': 'ZA9jxkAd45imyNW4s6PEorsRlPtVH8zEWIBjEIdJ88Q',
            'resolutions': [{
                'height': 57,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=108&amp;s=16ac24af4afd139bf84f33100eda8bda',
                'width': 108
            }, {
                'height': 115,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=216&amp;s=a30d7b1f0f6784d6c2b8dab7caf50a3d',
                'width': 216
            }, {
                'height': 171,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=320&amp;s=7818ce338c9c8879cbc55663ec019ccf',
                'width': 320
            }, {
                'height': 342,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=640&amp;s=d9eef59835602cf532c5d3a2c110beba',
                'width': 640
            }, {
                'height': 514,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=960&amp;s=60842aab7762157bdb9f0c9464de3bd6',
                'width': 960
            }, {
                'height': 578,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=1080&amp;s=f224b74cbdc83a4443ecb7a0a59549a5',
                'width': 1080
            }],
            'source': {
                'height': 1028,
                'url': 'https://i.redditmedia.com/HbU_9KxTAr5SPILCZsqenqFjTDYg4t596tjMwNYP5pM.jpg?s=c77e81f97fd941efda8f89537f336036',
                'width': 1920
            },
            'variants': {}
        }]
    },
    'quarantine': False,
    'removal_reason': None,
    'report_reasons': None,
    'saved': False,
    'score': 1652,
    'secure_media': None,
    'secure_media_embed': {},
    'selftext': '',
    'selftext_html': None,
    'stickied': False,
    'subreddit': 'wallpapers',
    'subreddit_id': 't5_2qhw4',
    'suggested_sort': None,
    'thumbnail': 'http://b.thumbs.redditmedia.com/jHlcSzXK-MH4vxuAf7L3KbWPz2_M8UwHFxB1viWLJlE.jpg',
    'title': 'Mech Warfare',
    'ups': 1652,
    'url': 'http://i.imgur.com/1O9JfRC.jpg',
    'user_reports': [],
    'visited': False
}
```
Clearly, this is way too many attributes to deal with, so we'll define a `Post` class variable called `attributes` which stores a set of strings representing attribute names that we want to maintain. For example, the bare bones the `Post` class could start as

```
class Post:
    attributes = {'author', 'created', 'domain', 'downs', 'id', 'is_self', 'num_comments', 'over_18', 'score', 'selftext', 'subreddit', 'title', 'ups', 'url'}
```

Write an `__init__(self, info)` method that takes a dictionary as an argument. Create a dictionary instance variable named `self.info` that stores the key-value pairs from the argument info using the class variable `Post.attributes` as a filter.

In essence, we're filtering out the uninteresting attributes. For example,

```Python3
post = Post(raw_data):
print(post.info)
{
    'author': 'PCGamingOnly',
    'created': 1445995723.0,
    'domain': 'i.imgur.com',
    'downs': 0,
    'id': '3qg0if',
    'is_self': False,
    'num_comments': 70,
    'over_18': False,
    'score': 1652,
    'selftext': '',
    'subreddit': 'wallpapers',
    'title': 'Mech Warfare',
    'ups': 1652,
    'url': 'http://i.imgur.com/1O9JfRC.jpg',
}
```

Implement the magic method `__str__(self)` that returns a string representing a human-readable form of a post. (This will allow us to print out post objects to the console). We suggest printing the posts in the following format: `"{title} ({score}): {url}"` (e.g. `print(post)` using the above object could yield: `Mech Warfare (1652): http://i.imgur.com/1O9JfRC.jp`). 

What should you print out if one of these attributes are undefined?

Write a method `is_image(self)` which returns true if and only if `is_self` is False, `selftext` is empty,  `over_18` is False, and either `domain` ends in `imgur.com` (because we love imgur) or `url` ends in `.jpg`, `.jpeg`, or `.png`.

## Load Response Data into Post Objects
The first part of this task had you acquire lots of information from the internet. The second task had you build a Post object where this data can live. In this part of the project, you will need to convert the response data from `query` into an array of `Post` objects (you should have around 25, maybe 26 or 27).

Write a method called `convert_response_data(response_data)` in `wallscraper.py` which accepts a dictionary (as returned by `query`) and returns an array of `Post` objects formed from the `response_data`. If the data is bad - i.e. keys are missing, information is not structured as you suspect, etc. - your program should not crash. Rather, it should gracefully handle the errors and proceed accordingly.

At this point, rewrite your old code to determine the number of posts with a score greater than 1000.

## Download an Image Post
Ultimately, our goal is to download wallpapers. Write a method called `download_to(self, file_pointer)` in the `Post` class that, if `self` is an image, will `requests.get` the `url` of the post, and write the returned content to the open file pointer passed to the function using `.write(data)`. It may be useful to use the `.iter_content()` method of `Response` objects, which returns an iterator representing a data stream of image data from the server to you.

To test this method, get a single `Post` object that you know is an image, and download it to a file using
```Python3
post = some_image_post_object
with open('test_filename', 'wb') as f:
    post.download_to(f)
```
The `'wb'` option passed to open specifies that the file should be opened for `(w)riting` and in `(b)inary` mode, where newlines aren't handled separately. Generally, when reading or writing binary data like images or sound files, it's a good idea to use the `'b'` option.

If you have successfully downloaded a photo, congratulations! That's pretty dang impressive for one lab day.

## Bulk downloads

As a final step, write a function `bulk_download(posts)` in `wallscraper.py` that accepts a list of `Post` objects and downloads all of them to local storage. Note that you will need to come up with some way of naming your files uniquely. Feel free to add extra constraints to the decision regarding which files you download (perhaps you only download images from imgur.com, or only wallpapers with a score over 500, or only gilded posts).

## Extensions
Some of these are easy, some of these are very hard.

### Command Line Utility
We saw in class that command-line arguments can be passed to Python scripts, and these arguments will be available through `sys.argv`. Modify your program so that it can be invoked with a single command-line argument representing the subreddit to scrape data from. So, `$ python wallscraper.py wallpaper` would download all the top wallpapers of the day, and `$ python wallscraper.py fffffffuuuuuuuuuuuu` would download all the top rage comics.

### Configure your computer so that this script runs every hour/day/month
Both OS X and Linux have ways to schedule a program to run every so often (Windows is harder). If you decide to do this option, talk with us. It's one of the coolest extensions, because you get awesome wallpapers over time, but it's also one of the hardest to get right. If you want to read up on your own, look up `launchd` and `cron`.

### Programmatically set the highest-scoring wallpaper as your desktop wallpaper
Both OS X and Linux have command-line tools to programmatically set your desktop background to be a specified file path (again, Windows is harder). In combination with the previous extension, you could have an automatically shifting desktop background of the internet's top trending wallpapers!

### Automatic size detection
Is there a way you can detect the size of an image before you write it to local storage? If not, is there a way you can determine the size after you've saved the image? Use the third-party`pillow` [library](https://python-pillow.github.io/) for any special image processing. Then sort the downloaded images into folders based on their aspect ratio, and furthermore by their absolute size.

### Support for Pagination
We currently scrape only one page of Reddit data at a time. In the response data, there are pagination tokens `before` and `after` than can be used to scroll through pages and pages of reddit. Use these pagination tokens to search through arbitrarily many pages of a subreddit.

### Wallpaper deduplication
If we ever encounter the same wallpaper twice, we'll process the data twice, download it twice, etc. Implement a system that will eliminate image download duplication. You have freedom to implement this however you want.
