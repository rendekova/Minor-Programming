import sys
import jokes as tob

def test_no_args():
	sys.argv = ["",]
	l = tob.read_arg()
	assert l == "en"

def test_lang_args_ok():
	sys.argv = ["", "-de"]
	l = tob.read_arg()
	assert l == "de"
	sys.argv = ["", "-fr"]
	l = tob.read_arg()
	assert l == "fr"

def test_args_wrong():
	sys.argv = ["", "-kl"]
	l = tob.read_arg()
	assert l == "en"
	sys.argv = ["", "-de", "-fr"]
	l = tob.read_arg()
	assert l == "de"
	sys.argv = ["", "fr"]
	l = tob.read_arg()
	assert l == "en"

def test_joke_ok():
	j = tob.get_single_joke("de")
	assert type(j) == str

def test_joke_wrong():
	j = tob.get_single_joke("kl")
	assert j == "Bad joke"
