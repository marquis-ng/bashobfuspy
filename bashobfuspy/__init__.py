import math as _math
import re as _re
import random as _random
import sys as _sys

def _int2chr(num):
    return chr(num + (65 if num < 26 else 71))

def _genID(num):
    res = ""
    while num > 0 or len(res) == 0:
        res += _int2chr(num % 51)
        num = _math.floor(num / 51)
    res += "z"
    return res

def obfuscate(content, chunk_size=4, rand=True):
    count = -1
    table = {}
    lines = []

    for line in filter(lambda line: line.strip() and line.strip()[0] != "#", content.split("\n")):
        chunks = []
        for chunk in _re.findall(".{1," + str(chunk_size) + "}", line):
            chunk = chunk.replace("'", "'\\\''")
            if chunk not in table:
                table[chunk] = _genID(count := count + 1)
            chunks.append("$" + table[chunk])
        lines.append("".join(chunks))

    res = "z=\"\n\";"
    t = list(table.items())
    if rand:
        _random.shuffle(t)

    for k, i in t:
        res += i + "='" + k + "';"
    res += "\neval \"" + "$z".join(lines) + "\""
    return res

def _main():
    import argparse
    try:
        import shtab
    except ImportError:
        from types import ModuleType
        class Dummy(ModuleType):
            def __getattr__(self, attr):
                return lambda *args, **kwargs: None
        shtab = Dummy("shtab")

    parser = argparse.ArgumentParser(prog="bash-obfuspy",
        description="Bash obfuscator written in Python",
        epilog="Ported from: https://github.com/willshiao/node-bash-obfuscate"
    )
    shtab.add_argument_to(parser, ["-s", "--print-completion"])
    parser.add_argument("-o", "--outfile", help="Output file", default=_sys.stdout).complete = shtab.FILE
    parser.add_argument("-c", "--chunk-size", help="Chunk size (for variables in obfuscated code)", type=int, default=4)
    parser.add_argument("-n", "--no-randomize", help="Do not randomize variable order", action="store_true")
    parser.add_argument("infile", nargs="?", default=_sys.stdin).complete = shtab.FILE
    args = parser.parse_args()

    if args.infile != _sys.stdin:
        args.infile = open(args.infile, "r")
    if args.outfile != _sys.stdout:
        args.outfile = open(args.outfile, "w")

    print(obfuscate(args.infile.read(), chunk_size=args.chunk_size, rand=not args.no_randomize), file=args.outfile)

if __name__ == "__main__":
    _main()
