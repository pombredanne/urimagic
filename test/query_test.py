#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import unicode_literals

try:
    from collections import OrderedDict
except ImportError:
    from .util.ordereddict import OrderedDict

from urimagic import Query


def test_can_parse_none_query():
    query = Query(None)
    assert str(query) == ""
    assert query.string is None
    assert dict(query) == {}
    try:
        assert query["bacon"] == "yummy"
    except KeyError:
        assert True
    else:
        assert False


def test_can_parse_empty_query():
    query = Query("")
    assert str(query) == ""
    assert query.string == ""
    assert dict(query) == {}
    try:
        assert query["bacon"] == "yummy"
    except KeyError:
        assert True
    else:
        assert False


def test_can_parse_key_only_query():
    query = Query("foo")
    assert str(query) == "foo"
    assert query.string == "foo"
    assert dict(query) == {"foo": None}
    assert query["foo"] is None


def test_can_parse_key_value_query():
    query = Query("foo=bar")
    assert str(query) == "foo=bar"
    assert query.string == "foo=bar"
    assert dict(query) == {"foo": "bar"}
    assert query["foo"] == "bar"


def test_can_parse_multi_key_value_query():
    query = Query("foo=bar&spam=eggs")
    assert str(query) == "foo=bar&spam=eggs"
    assert query.string == "foo=bar&spam=eggs"
    assert dict(query) == {"foo": "bar", "spam": "eggs"}
    assert query["foo"] == "bar"
    assert query["spam"] == "eggs"


def test_can_parse_mixed_query():
    query = Query("foo&spam=eggs")
    assert str(query) == "foo&spam=eggs"
    assert query.string == "foo&spam=eggs"
    assert dict(query) == {"foo": None, "spam": "eggs"}
    assert query["foo"] is None
    assert query["spam"] == "eggs"
    try:
        assert query["bacon"] == "yummy"
    except KeyError:
        assert True
    else:
        assert False


def test_can_query_encode_dict():
    data = OrderedDict([("foo", "bar"), ("baz", None), ("big number", 712)])
    encoded = Query.encode(data)
    assert encoded == "foo=bar&baz&big%20number=712"


def test_can_query_encode_list():
    data = ["red", "orange", "yellow", "green", 97, False]
    encoded = Query.encode(data)
    assert encoded == "red&orange&yellow&green&97&False"


def test_query_equality():
    query1 = Query("foo=bar&spam=eggs")
    query2 = Query("foo=bar&spam=eggs")
    assert query1 == query2


def test_query_inequality():
    query1 = Query("foo=bar&spam=eggs")
    query2 = Query("foo=bar&spam=bacon")
    assert query1 != query2


def test_query_equality_when_none():
    query = Query(None)
    none = None
    assert query == none


def test_query_is_hashable():
    query = Query("foo=bar&spam=eggs")
    hashed = hash(query)
    assert hashed
