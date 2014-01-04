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


from __future__ import unicode_literals, print_function

from urimagic import URI


def test_can_parse_none_uri():
    uri = URI(None)
    assert str(uri) == ""
    assert uri.string is None
    assert uri.scheme is None
    assert uri.hierarchical_part is None
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority is None
    assert uri.path is None
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference is None


def test_can_parse_none_uri_from_none_uri():
    uri = URI(URI(None))
    assert str(uri) == ""
    assert uri.string is None
    assert uri.scheme is None
    assert uri.hierarchical_part is None
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority is None
    assert uri.path is None
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference is None


def test_can_parse_empty_string_uri():
    uri = URI("")
    assert str(uri) == ""
    assert uri.string == ""
    assert uri.scheme is None
    assert uri.hierarchical_part == ""
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority is None
    assert uri.path == ""
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference == ""

def test_can_parse_absolute_path_uri():
    uri = URI("/foo/bar")
    assert str(uri) == "/foo/bar"
    assert uri.string == "/foo/bar"
    assert uri.scheme is None
    assert uri.hierarchical_part == "/foo/bar"
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority is None
    assert uri.path == "/foo/bar"
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference == "/foo/bar"


def test_can_parse_relative_path_uri():
    uri = URI("foo/bar")
    assert str(uri) == "foo/bar"
    assert uri.string == "foo/bar"
    assert uri.scheme is None
    assert uri.hierarchical_part == "foo/bar"
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority is None
    assert uri.path == "foo/bar"
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference == "foo/bar"


def test_can_parse_only_query():
    uri = URI("?foo=bar")
    assert str(uri) == "?foo=bar"
    assert uri.string == "?foo=bar"
    assert uri.scheme is None
    assert uri.hierarchical_part == ""
    assert uri.query == "foo=bar"
    assert dict(uri.query) == {"foo": "bar"}
    assert uri.fragment is None
    assert uri.authority is None
    assert uri.path == ""
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference == "?foo=bar"


def test_can_parse_only_fragment():
    uri = URI("#foo")
    assert str(uri) == "#foo"
    assert uri.string == "#foo"
    assert uri.scheme is None
    assert uri.hierarchical_part == ""
    assert uri.query is None
    assert uri.fragment == "foo"
    assert uri.authority is None
    assert uri.path == ""
    assert uri.user_info is None
    assert uri.host is None
    assert uri.port is None
    assert uri.host_port is None
    assert uri.absolute_path_reference == "#foo"


def test_can_parse_uri_without_scheme():
    uri = URI("//example.com")
    assert str(uri) == "//example.com"
    assert uri.string == "//example.com"
    assert uri.scheme is None
    assert uri.hierarchical_part == "//example.com"
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority == "example.com"
    assert uri.path == ""
    assert uri.user_info is None
    assert uri.host == "example.com"
    assert uri.port is None
    assert uri.host_port == "example.com"
    assert uri.absolute_path_reference == ""


def test_can_parse_simple_uri():
    uri = URI("foo://example.com")
    assert str(uri) == "foo://example.com"
    assert uri.string == "foo://example.com"
    assert uri.scheme == "foo"
    assert uri.hierarchical_part == "//example.com"
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority == "example.com"
    assert uri.path == ""
    assert uri.user_info is None
    assert uri.host == "example.com"
    assert uri.port is None
    assert uri.host_port == "example.com"
    assert uri.absolute_path_reference == ""


def test_can_parse_uri_with_root_path():
    uri = URI("foo://example.com/")
    assert str(uri) == "foo://example.com/"
    assert uri.string == "foo://example.com/"
    assert uri.scheme == "foo"
    assert uri.hierarchical_part == "//example.com/"
    assert uri.query is None
    assert uri.fragment is None
    assert uri.authority == "example.com"
    assert uri.path == "/"
    assert uri.user_info is None
    assert uri.host == "example.com"
    assert uri.port is None
    assert uri.host_port == "example.com"
    assert uri.absolute_path_reference == "/"


def test_can_parse_full_uri():
    uri = URI("foo://bob@somewhere@example.com:8042"
              "/over/there?name=ferret#nose")
    assert str(uri) ==\
        "foo://bob%40somewhere@example.com:8042/over/there?name=ferret#nose"
    assert len(uri) == (len("foo://bob%40somewhere@example.com:8042"
                            "/over/there?name=ferret#nose"))
    assert bool(uri) == True
    assert URI(uri) == \
        "foo://bob%40somewhere@example.com:8042/over/there?name=ferret#nose"
    assert uri.string == \
        "foo://bob%40somewhere@example.com:8042/over/there?name=ferret#nose"
    assert uri.scheme == "foo"
    assert uri.hierarchical_part == \
        "//bob%40somewhere@example.com:8042/over/there"
    assert uri.query == "name=ferret"
    assert dict(uri.query) == {"name": "ferret"}
    assert uri.query["name"] == "ferret"
    assert uri.fragment == "nose"
    assert uri.authority == "bob%40somewhere@example.com:8042"
    assert uri.path == "/over/there"
    assert uri.user_info == "bob@somewhere"
    assert uri.host == "example.com"
    assert uri.port == 8042
    assert uri.host_port == "example.com:8042"
    assert uri.absolute_path_reference == "/over/there?name=ferret#nose"


def test_uri_representation():
    uri = URI("http://example.com/")
    representation = repr(uri)
    assert representation in ("URI('http://example.com/')",
                              "URI(u'http://example.com/')")


def test_uri_equality():
    uri1 = URI("http://example.com/")
    uri2 = URI("http://example.com/")
    assert uri1 == uri2


def test_uri_inequality():
    uri1 = URI("http://example.com/")
    uri2 = URI("http://example.org/")
    assert uri1 != uri2


def test_uri_equality_when_none():
    uri = URI(None)
    none = None
    assert uri == none


def test_uri_is_hashable():
    uri = URI("http://example.com/")
    hashed = hash(uri)
    assert hashed


def test_uri_to_true():
    uri = URI("http://example.com/")
    assert uri.__bool__()
    assert uri.__nonzero__()


def test_uri_to_false():
    uri = URI("")
    assert not uri.__bool__()
    assert not uri.__nonzero__()


def test_uri_can_be_iterated():
    uri = URI("http://example.com/")
    listed = list(uri)
    assert listed == ['h', 't', 't', 'p', ':', '/', '/', 'e', 'x', 'a', 'm',
                      'p', 'l', 'e', '.', 'c', 'o', 'm', '/']


def _test_references(references):
    base = URI("http://a/b/c/d;p?q")
    for reference, target in references.items():
        print(reference, "->", target)
        uri = base.resolve(reference)
        assert uri == target


def test_can_resolve_normal_uri_references():
    _test_references({
        "g:h"    : "g:h",
        "g"      : "http://a/b/c/g",
        "./g"    : "http://a/b/c/g",
        "g/"     : "http://a/b/c/g/",
        "/g"     : "http://a/g",
        "//g"    : "http://g",
        "?y"     : "http://a/b/c/d;p?y",
        "g?y"    : "http://a/b/c/g?y",
        "#s"     : "http://a/b/c/d;p?q#s",
        "g#s"    : "http://a/b/c/g#s",
        "g?y#s"  : "http://a/b/c/g?y#s",
        ";x"     : "http://a/b/c/;x",
        "g;x"    : "http://a/b/c/g;x",
        "g;x?y#s": "http://a/b/c/g;x?y#s",
        ""       : "http://a/b/c/d;p?q",
        "."      : "http://a/b/c/",
        "./"     : "http://a/b/c/",
        ".."     : "http://a/b/",
        "../"    : "http://a/b/",
        "../g"   : "http://a/b/g",
        "../.."  : "http://a/",
        "../../" : "http://a/",
        "../../g": "http://a/g",
    })


def test_can_resolve_abnormal_uri_references():
    _test_references({
        "../../../g"    :  "http://a/g",
        "../../../../g" :  "http://a/g",
    })


def test_can_resolve_and_remove_dot_segments_correctly():
    _test_references({
        "/./g"          :  "http://a/g",
        "/../g"         :  "http://a/g",
        "g."            :  "http://a/b/c/g.",
        ".g"            :  "http://a/b/c/.g",
        "g.."           :  "http://a/b/c/g..",
        "..g"           :  "http://a/b/c/..g",
    })


def test_can_resolve_nonsensical_dot_segments_correctly():
    _test_references({
        "./../g"        :  "http://a/b/g",
        "./g/."         :  "http://a/b/c/g/",
        "g/./h"         :  "http://a/b/c/g/h",
        "g/../h"        :  "http://a/b/c/h",
        "g;x=1/./y"     :  "http://a/b/c/g;x=1/y",
        "g;x=1/../y"    :  "http://a/b/c/y",
    })


def test_can_resolve_and_handle_queries_and_fragments_correctly():
    _test_references({
        "g?y/./x"       :  "http://a/b/c/g?y/./x",
        "g?y/../x"      :  "http://a/b/c/g?y/../x",
        "g#s/./x"       :  "http://a/b/c/g#s/./x",
        "g#s/../x"      :  "http://a/b/c/g#s/../x",
    })


def test_can_resolve_with_strict_mode():
    base = URI("http://a/b/c/d;p?q")
    uri = base.resolve("http:g", strict=True)
    assert uri == "http:g"


def test_can_resolve_without_strict_mode():
    base = URI("http://a/b/c/d;p?q")
    uri = base.resolve("http:g", strict=False)
    assert uri == "http://a/b/c/g"


def test_can_resolve_from_empty_path():
    base = URI("http://example.com")
    uri = base.resolve("foo")
    assert uri == "http://example.com/foo"


def test_can_resolve_from_empty_uri():
    base = URI("")
    uri = base.resolve("foo")
    assert uri == "foo"


def test_resolving_when_reference_is_none_returns_none():
    base = URI("http://example.com")
    uri = base.resolve(None)
    assert uri is None
