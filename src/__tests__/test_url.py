#!/usr/bin/env python3

from unittest import TestCase

from playlist_id import PlaylistID
from url import URL

URL.HISTORY_BASE = "base"


class TestPlainHistory(TestCase):
    def test_success(self) -> None:
        self.assertEqual(URL.plain_history(PlaylistID("foo")), "base/plain/foo")


class TestPlain(TestCase):
    def test_success(self) -> None:
        self.assertEqual(URL.plain(PlaylistID("foo")), "/playlists/plain/foo")


class TestPretty(TestCase):
    def test_success(self) -> None:
        self.assertEqual(URL.pretty("a b"), "/playlists/pretty/a%20b.md")


class TestCumulative(TestCase):
    def test_success(self) -> None:
        self.assertEqual(URL.cumulative("a b"), "/playlists/cumulative/a%20b.md")
