import sys
from omero.cli import BaseControl, CLI

HELP = """Simple template plugin which doesn't do anything"""

class SimpleControl(BaseControl):
    """
    Some documentation
    """

    def _configure(self, parser):
        parser.add_argument(
            "some_argument",
            help="Some argument")
        parser.set_defaults(func=self.process)

    def process(self, args):
        # Dispatch to certain methods depending on args
        self.some_method(args.some_argument)

    def some_method(self, some_argument):
        print("Do something with "+some_argument)

try:
    register("simple", SimpleControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("simple", SimpleControl, HELP)
        cli.invoke(sys.argv[1:])
