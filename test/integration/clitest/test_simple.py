from simple import SimpleControl
from test.integration.clitest.cli import CLITest
import pytest

# some parameter values to test
test_arguments = ["hello", "world"]


class TestSimple(CLITest):

    def setup_method(self, method):
        super(TestSimple, self).setup_method(method)
        self.cli.register("simple", SimpleControl, "TEST")
        self.args += ["simple"]
    
    @pytest.mark.parametrize("arg", test_arguments)
    def test_template(self, capsys, arg):
        
        # assemble the arguments and invoke CLI
        self.args += ['%s' % arg]
        self.cli.invoke(self.args, strict=True)

        # capture and check the output
        out, err = capsys.readouterr()
        assert out is not None
