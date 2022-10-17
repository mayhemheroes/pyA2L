#!/usr/bin/python3
import atheris
import sys
import io
from contextlib import contextmanager

with atheris.instrument_imports():
    import pya2l.a2l_listener
    import pya2l.parserlib


# Disable stdout
@contextmanager
def nostdout():
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr


fuzz_iter = 0
@atheris.instrument_func
def TestOneInput(data):
    global fuzz_iter
    fuzz_iter += 1

    parser = pya2l.parserlib.ParserWrapper("a2l", "alignmentByte", pya2l.a2l_listener.A2LListener,
                                           useDatabase=False, debug=False)
    try:
        with nostdout():
            parser.parseFromString(str(data))
    except AttributeError as e:
        # This is a valid exception, but it's too pervasive to raise all the time
        if fuzz_iter > 1000:
            raise e
    return 0


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
