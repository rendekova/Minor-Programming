import pytest
import faces
from faces import convert 


def test_smiley_emoji():
    assert faces.convert("Hello :)") == "Hello 🙂"

def test_sad_emoji():
    assert faces.convert("Goodbye :(") == "Goodbye 🙁"

def test_wink_emoji():
    assert faces.convert("Hey ;)") == "Hey 😉"

def test_frog_emoji():
    assert faces.convert("Kvak :frog:") == "Kvak 🐸"

def test_no_emojis():
    assert faces.convert("Text") == "Text"

def test_uppercase():
    assert faces.convert(":FROG:") == ":FROG:"

def test_strange_characters():
    assert faces.convert("Huh?!! :( ??") == "Huh?!! 🙁 ??"
    assert faces.convert("#hashtag ** kvak :frog:") == "#hashtag ** kvak 🐸"

def test_half_emojis():
    assert faces.convert(":") == ":"
    assert faces.convert(";") == ";"
    assert faces.convert(":frog") == ":frog"
    assert faces.convert("frog:") == "frog:"
    assert faces.convert("(") == "("


def test_multiple_emojis():
    assert faces.convert("Hello :) Bye :(:frog:") == "Hello 🙂 Bye 🙁🐸"


