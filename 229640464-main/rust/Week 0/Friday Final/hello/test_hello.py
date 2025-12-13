import io
import sys
import hello


def test_ask():
    # console input must be name
    a = "Victor"
    with io.StringIO(a) as handle:
        stdin = sys.stdin
        sys.stdin = handle
        n = hello.ask_name()
        sys.stdin = stdin
    assert n == a


def test_say():
    # console output must contain name
    a = "Jaqueline"
    with io.StringIO() as handle:
        sys.stdout = handle
        hello.say_hello(a)
        assert a in handle.getvalue()
