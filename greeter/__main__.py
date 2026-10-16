"""Print a greeting: python -m greeter NAME [CONFIG]."""

import sys

from greeter import greet, load_config


def main(argv):
    if len(argv) < 2:
        print("usage: python -m greeter NAME [CONFIG]", file=sys.stderr)
        return 2
    config = load_config(argv[2] if len(argv) > 2 else "config/greeter.json")
    print(greet(argv[1], config))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
