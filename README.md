CLIVE
=====

[![PyPI Version] (https://img.shields.io/pypi/v/CLIve.svg)](https://pypi.python.org/pypi/CLIve)
[![PyPI](https://img.shields.io/pypi/l/CLIve.svg)](https://pypi.python.org/pypi/CLIve)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/binaryheadache)

When following a Reddit live feed, who wants to have a big ugly webpage open
all the time? Not me, and perhaps not you either.

So I started to write a command line interface that prints messages
as they arrive. It's still a **little** rough as I put this together in a few
hours, so consider it a work in progress. Contributions and suggestions
welcome and encouraged.

If you are wondering why *clive*, it's a  blend of *cli* and *live*.

Requirements
------------

* Python 2.7 or 3.5
* colorama==0.3.7
* html==1.16
* requests==2.9.1
* websocket-client==0.35.0

Installation
------------

    $ pip install clive

Usage
-----

    $ clive wmk50bsm9vt3

Where `wmk50bsm9vt3` is the last part of the live feed URL from Reddit.

License
-------

The MIT License (MIT)
Copyright (c) 2016 Sven Steinbauer

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.


