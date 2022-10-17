#!/usr/bin/python3
import atheris
import sys
import io

with atheris.instrument_imports():
    import pya2l.a2l_listener
    import pya2l.parserlib


@atheris.instrument_func
def TestOneInput(data):
    if len(data) < 1:
        return -1

    fdp = atheris.FuzzedDataProvider(data)
    parser = pya2l.parserlib.ParserWrapper("a2l", "alignmentByte", pya2l.a2l_listener.A2LListener, debug=False)
    parser.parseFromString(fdp.ConsumeString(fdp.remaining_bytes()))
    return 0

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
