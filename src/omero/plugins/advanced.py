import sys
from omero.cli import BaseControl, CLI, ExceptionHandler

HELP = """Advanced template plugin which doesn't do much"""

class AdvancedControl(BaseControl):
    """
    Some documentation
    """

    def _configure(self, parser):
        # Add an exception handler
        self.exc = ExceptionHandler()

        # Add default login arguments, prompting the user for
        # server login credentials
        parser.add_login_arguments()

        # Add some 'commands', i.e. operations the plugin can perform
        parser.add_argument(
            "command", nargs="?",
            choices=("foo", "bar"),
            help="Some operation to be performed")

        # Add an additional argument
        parser.add_argument(
            "--some_argument", help="An additional argument")

        parser.set_defaults(func=self.process)

    def process(self, args):
        # Check for necessary arguments
        if not args.command:
            # Exit with code 100
            self.ctx.die(100, "No command provided")

        # Dispatch to the respective method handling
        # the command
        if args.command == "foo":
            self.foo(args)

        if args.command == "bar":
            self.bar(args)

    def foo(self, args):
        # Check for the --some_argument
        if args.some_argument:
            # Print to stout
            self.ctx.out("Some argument was %s" % args.some_argument)
        else:
            # Print to sterr
            self.ctx.err("Some argument was empty")

        # Create a connection to the server
        conn = self.ctx.conn(args)

        session_id = conn.getSessionId()
        self.ctx.out("Connected with session ID %s " % session_id)

        # Interact with the server via the ServiceFactory (sf),
        # see omero/api/ServiceFactory documentation
        config_service = conn.sf.getConfigService()
        server_version = config_service.getVersion()
        self.ctx.out("Server version %s " % server_version)

    def bar(self, args):
        # Throw an exception
        raise Exception("Not implemented yet.")

try:
    # Register the plugin with the name 'advanced'
    # i.e. it will be available as `./omero advanced ...`
    # on the command line
    register("advanced", AdvancedControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("advanced", AdvancedControl, HELP)
        cli.invoke(sys.argv[1:])
