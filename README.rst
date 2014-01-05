.. image:: https://travis-ci.org/nigelsmall/urimagic.png?branch=master   :target: https://travis-ci.org/nigelsmall/urimagic

URIMagic
========

URIMagic is a Python library that provides full implementations of RFC
3986 URIs and RFC 6570 URI Templates.

Percent Encoding & Decoding
---------------------------

.. code-block:: python

    >>> from urimagic import percent_encode, percent_decode
    >>> percent_encode("Mulder & Scully")
    'Mulder%20%26%20Scully'
    >>> percent_decode("Mulder%20%26%20Scully")
    'Mulder & Scully'

Parsing a URI
-------------

.. code-block:: python

    >>> from urimagic import URI
    >>> uri = URI("https://bob@example.com:8080/data/report.html?date=2000-12-25#summary")
    >>> uri.scheme
    'https'
    >>> uri.authority
    Authority('bob@example.com:8080')
    >>> uri.user_info
    'bob'
    >>> uri.host
    'example.com'
    >>> uri.port
    8080
    >>> uri.host_port
    'example.com:8080'
    >>> uri.path
    Path('/data/report.html')
    >>> uri.query
    Query('date=2000-12-25')
    >>> uri.fragment
    'summary'
    >>> uri.hierarchical_part
    '//bob@example.com:8080/data/report.html'
    >>> uri.absolute_path_reference
    '/data/report.html?date=2000-12-25#summary'
    >>> uri.string
    'https://bob@example.com:8080/data/report.html?date=2000-12-25#summary'

Authorities
~~~~~~~~~~~

.. code-block:: python

    >>> from urimagic import Authority
    >>> auth = Authority("bob@example.com:8080")
    >>> auth.user_info
    'bob'
    >>> auth.host
    'example.com'
    >>> auth.port
    8080
    >>> auth.host_port
    'example.com:8080'
    >>> auth.string
    'bob@example.com:8080'

Paths
~~~~~

.. code-block:: python

    >>> from urimagic import Path
    >>> Path("/foo/bar").segments
    ['', 'foo', 'bar']
    >>> Path("/foo/bar").with_trailing_slash()
    Path('/foo/bar/')
    >>> Path("/foo/bar/").without_trailing_slash()
    Path('/foo/bar')
    >>> Path("/foo/bar").string
    '/foo/bar'

Queries
~~~~~~~

.. code-block:: python

    >>> from urimagic import Query
    >>> query = Query("cake=nice&mushrooms=yuk")
    >>> query["cake"]
    'nice'
    >>> query["mushrooms"]
    'yuk'
    >>> query.string
    'cake=nice&mushrooms=yuk'
    >>> Query.encode(["Mulder", "Scully"])
    'Mulder&Scully'
    >>> Query.encode({"Mulder": "believer", "Scully": "sceptic"})
    'Mulder=believer&Scully=sceptic'
    >>> Query.decode("Mulder=believer&Scully=sceptic")
    [('Mulder', 'believer'), ('Scully', 'sceptic')]

Resolving new URIs
------------------

URI Templates
-------------

