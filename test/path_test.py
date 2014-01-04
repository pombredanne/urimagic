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

from urimagic import Path


def test_can_parse_none_path():
    path = Path(None)
    assert str(path) == ""
    assert path.string is None


def test_can_parse_empty_path():
    path = Path("")
    assert str(path) == ""
    assert path.string == ""


def test_can_parse_absolute_path():
    path = Path("/foo/bar")
    assert str(path) == "/foo/bar"
    assert path.string == "/foo/bar"


def test_can_parse_relative_path():
    path = Path("foo/bar")
    assert str(path) == "foo/bar"
    assert path.string == "foo/bar"


def test_can_parse_path_with_encoded_slash():
    path = Path("/foo/bar%2Fbaz")
    assert str(path) == "/foo/bar%2Fbaz"
    assert path.string == "/foo/bar%2Fbaz"


def test_path_equality():
    path1 = Path("/foo/bar")
    path2 = Path("/foo/bar")
    assert path1 == path2


def test_path_inequality():
    path1 = Path("/foo/bar")
    path2 = Path("/foo/bar/baz")
    assert path1 != path2


def test_path_equality_when_none():
    path = Path(None)
    none = None
    assert path == none


def test_path_is_hashable():
    path = Path("/foo/bar")
    hashed = hash(path)
    assert hashed


def test_path_has_no_segments_when_none():
    path = Path(None)
    segments = list(path.segments)
    assert segments == []


def test_path_is_iterable_as_segments():
    path = Path("/foo/bar")
    segments = list(path)
    assert segments == ["", "foo", "bar"]


def test_can_remove_dot_segments_pattern_1():
    path_in = Path("/a/b/c/./../../g")
    path_out = path_in.remove_dot_segments()
    assert path_out == "/a/g"


def test_can_remove_dot_segments_pattern_2():
    path_in = Path("mid/content=5/../6")
    path_out = path_in.remove_dot_segments()
    assert path_out == "mid/6"


def test_can_remove_dot_segments_when_single_dot():
    path_in = Path(".")
    path_out = path_in.remove_dot_segments()
    assert path_out == ""


def test_can_remove_dot_segments_when_double_dot():
    path_in = Path("..")
    path_out = path_in.remove_dot_segments()
    assert path_out == ""


def test_can_remove_dot_segments_when_starts_with_single_dot():
    path_in = Path("./a")
    path_out = path_in.remove_dot_segments()
    assert path_out == "a"


def test_can_remove_dot_segments_when_starts_with_double_dot():
    path_in = Path("../a")
    path_out = path_in.remove_dot_segments()
    assert path_out == "a"


def test_can_add_trailing_slash_to_path():
    path = Path("/foo/bar")
    path = path.with_trailing_slash()
    assert path.string == "/foo/bar/"


def test_wont_add_trailing_slash_to_path_that_already_has_one():
    path = Path("/foo/bar/")
    path = path.with_trailing_slash()
    assert path.string == "/foo/bar/"


def test_wont_add_trailing_slash_to_root_path():
    path = Path("/")
    path = path.with_trailing_slash()
    assert path.string == "/"


def test_can_add_trailing_slash_to_empty_path():
    path = Path("")
    path = path.with_trailing_slash()
    assert path.string == "/"


def test_cant_add_trailing_slash_to_none_path():
    path = Path(None)
    path = path.with_trailing_slash()
    assert path.string is None


def test_can_remove_trailing_slash_from_path():
    path = Path("/foo/bar/")
    path = path.without_trailing_slash()
    assert path.string == "/foo/bar"


def test_wont_remove_trailing_slash_if_none_exists():
    path = Path("/foo/bar")
    path = path.without_trailing_slash()
    assert path.string == "/foo/bar"


def test_will_remove_root_path_slash():
    path = Path("/")
    path = path.without_trailing_slash()
    assert path.string == ""


def test_cannot_remove_trailing_slash_from_empty_string():
    path = Path("")
    path = path.without_trailing_slash()
    assert path.string == ""


def test_cant_remove_trailing_slash_from_none_path():
    path = Path(None)
    path = path.without_trailing_slash()
    assert path.string is None
