# About Boston Python

Content and configuration for <https://shireenrao.github.io>, build with [Pelican](https://blog.getpelican.com/) and hosted on [GitHub Pages](https://pages.github.com/).

## Building the site locally

Prerequisites:
- Create a virtual environment with Python 3.7
- Install requirements.txt

```
pelican -lr
```

`pelican -lr` generates the html in the output directory and starts a local web server where you can go browse the site at <http://localhost:8000/>. You need to execute this command from the root of the project.


## Pages 
This site is setup to only display pages. All markdown content is located under content/pages. All pages are setup to show up as navigation links. A typical page metadata in the header needs to be as follows:

```
Title: Contact Us
URL: contact.html
save_as: contact.html
slug: contact
```

In case a page is needed which is not needed in the navigation section, just add a `status: hidden` metadata tag in the header of the markdown file.



