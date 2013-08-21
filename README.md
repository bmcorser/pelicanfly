Introduction
============

This is **pelicanfly**, a plugin for [Pelican](http://docs.getpelican.com/) that
lets you type things like `i ♥ :icon-coffee:` in your
[Markdown](http://daringfireball.net/projects/markdown/) documents and have it
come out as little icons in the browser. It provides a minimal extension to
Markdown and a plugin for Pelican.

The Pelican plugin hacks in some static assets to make this work with
Pelican "out of the box". If you just want the Markdown extension, it is
available
[separately](http://bmcorser.github.com/markdown-fontawesome/).

Installation
============

It's not hard, just install via pip:

    :::shell
    (env)$ pip install pelicanfly

Then add to your Pelican settings, under `PLUGINS` as follows:

    :::python
    PLUGINS = [
        # ...
        'pelicanfly',
        # ...
    ]

If you have followed these steps correctly, next time you build your Pelican
blog, pelicanfly will do its magic and convert all the `:icon-heart:` style
tags into proper nice little Font Awesome icons. Job done!
