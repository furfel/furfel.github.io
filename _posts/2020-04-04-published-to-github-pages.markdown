---
layout: post
title: Published the site to GitHub Pages
date: 04-04-2020
---
Today, I managed to push the first version of the webiste to GitHub Pages.
At first the content was duplicated so I had to remove `markdown: kramdown`
from `_config.yml`. Apparently, GitHub always injects its own preprocessor.

I also fixed the dates in posts and `<title>`. Because the `title` in
`jekyll-seo-tag` is kind of bad - a long string of description inside it
doesn't look right.
