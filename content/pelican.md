Title: Make a static website with Pelican 
author: Francisco Valladolid
tags: python, blog, static, website
lang: en
category: blog
slug: pelican
Date: 2018-03-19
email: ficovh@gmail.com

## What is Pelican?
According to the website, Pelican is a static website generator written in Python programming language.
Pelican parse documents in Markdown, reStructuredText and AsciiDoc file formats.

## Features

* Articles (e.g., blog posts) and pages (e.g., “About”, “Projects”, “Contact”)
* Comments, via an external service (Disqus). If you prefer to have more control over your comment data, self-hosted comments are another option. Check out the Pelican Plugins repository for more details.
* Theming support (themes are created using Jinja2 templates)
* Publication of articles in multiple languages
* Atom/RSS feeds
* Code syntax highlighting
* Import from WordPress, Dotclear, or RSS feeds
* Integration with external tools: Twitter, Google Analytics, etc. (optional)
* Fast rebuild times thanks to content caching and selective output writing

## Requeriments.

* Python 2.7.x or 3.3+
* pip (package manager from python)

```
  For this article, we are using python 3.6
```

## Installing Pelican.
```shell
$ sudo pip install pelican
```

## Installing markdown support (if you intend use it.)
```shell
$ sudo pip install markdown
```

## QuickStart

### Create a project.
```shell
  $ mkdir myblog
  $ pelican-quickstart

  > Where do you want to create your new web site? [.]
  > What will be the title of this web site? My personal Blog
  > Who will be the author of this web site? Author Name
  > What will be the default language of this web site? [Spanish] EN
  > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
  > What is your URL prefix? (see above example; no trailing slash) >   http://blog.example.com
  > Do you want to enable article pagination? (Y/n) y
  > How many articles per page do you want? [10]
  > What is your time zone? [Europe/Paris] Mexico/General
  > Do you want to generate a Fabfile/Makefile to automate generation and    publishing? (Y/n) n
  > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) n
  Done. Your new project is available at /home/ficovh/pelican-projects/myblog
```
### Create the first article.

```
  Title: My First posts
  Date: 2017-11-09 18:24
  Category: Articles

  This is my first post in the Pelican Static website generator.
```

The previous example was written in Markdown file format, save it as:

```
 ~/pelican-projects/myblog/content/first-post.md
```

### Generate the site and Launching the preview.

```
    $ pelican -o output content
      Done: Processed 1 article, 0 drafts, 0 pages and 0 hidden pages in 0.27 seconds.
    $ cd ~/pelican-projects/myblog/output
    $ python -m http.server
      Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)
```

### Settings.

The *pelicanconf.py* file contain the general settings for the website, feel
free to modify and add new variables.

The [pelican-themes](https://github.com/getpelican/pelican-themes) in Github contain several themes for pelican, you can use a specific template by using
the variable **THEME** as follow in the *pelicanconf.py* file

```
  THEME='pelican-bootstrap3'
```

### Conclusions

Pelican is a simple and powerful static website generator, very fast and stable.
Personally, I'm using pelican for more than two years ago.
Enjoy your new blog.
