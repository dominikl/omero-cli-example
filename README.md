CLI plugin example
==================

This repository provides two example CLI plugins which can be used as template for
developing custom OMERO CLI plugins.

* [simple.py](https://github.com/dominikl/omero-cli-example/blob/master/src/omero/plugins/simple.py): A very simple
  example showing how a plugin is basically structured.
* [advanced.py](https://github.com/dominikl/omero-cli-example/blob/master/src/omero/plugins/advanced.py): A more
  advanced example showing various aspects like how to interact with the server, handle exceptions, etc.

It is good practice to test a plugin with an integration test, see:

* [test_simple.py](https://github.com/dominikl/omero-cli-example/blob/master/test/integration/clitest/test_simple.py):
  A basic example which can be used as template for writing an integration test for an OMERO CLI plugin

How to get the CLI
==================

The CLI is part of the [OmeroPy](https://github.com/openmicroscopy/openmicroscopy/tree/develop/components/tools/OmeroPy)
and server package.

You can clone the [openmicroscopy](https://github.com/openmicroscopy/openmicroscopy) repository and run the `build-py`
target (`./build.py build-py`) to build the OmeroPy package or just download the current version from
https://www.openmicroscopy.org/omero/downloads/ .


Some important files/directories
--------------------------------
* [omero](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/bin/omero) shell script
  which launches
* The CLI [cli.py](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/src/omero/cli.py)
* Official core CLI plugins are in [src/omero/plugins](https://github.com/openmicroscopy/openmicroscopy/tree/develop/components/tools/OmeroPy/src/omero/plugins)
* Integration tests for the official core CLI plugins are in [test/integration/clitest](https://github.com/openmicroscopy/openmicroscopy/tree/develop/components/tools/OmeroPy/test/integration/clitest)

Principles
----------
* Functionality is implemented in 'Plugins'
* Plugins can be anywhere on your `PYTHONPATH`. As long as they are in a directory called `omero/plugins` the CLI
  will pick them up automatically
* 'Plugins' are called 'Controls' on the code level
* Each 'Control' inherits from [BaseControl](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/src/omero/cli.py#L642)

How to write a custom plugin
============================

Setup OmeroPy:

* Get the OmeroPy package (see above), and extract it, e. g. to `~/OmeroPy`
* Add `~/OmeroPy/lib/python` to the `PYTHONPATH`: `export PYTHONPATH=$PYTHONPATH:~/OmeroPy/lib/python`

Setup the plugin environment:

* Create a `omero/plugins` directory, e. g. `mkdir -p ~/my_cli_plugins/omero/plugins`
* Add this directory to the `PYTHONPATH`: `export PYTHONPATH=$PYTHONPATH:~/my_cli_plugins`
* Create `[PLUGIN NAME]Control.py` in the `omero/plugins` directory 
* Copy and paste the [advanced.py](https://github.com/dominikl/omero-cli-example/blob/master/src/omero/plugins/advanced.py)
  example to get started. Adjust the name of the class to match `[PLUGIN NAME]Control` and the name with which the
  plugin registers itself with the CLI (see bottom of the example).

Essential properties of a plugin
--------------------------------
* Must inherit from [BaseControl](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/src/omero/cli.py#L642) (or a child class of `BaseControl`)
* Must implement the `_configure` method, which
  * sets up the `parser` with the arguments the plugin supports
  * tells the `parser` via `set_defaults` which method to call when the plugin is called
* Must call `register` to register the plugin with the CLI with a certain name

Run the plugin
--------------
Before you go into the details of the implementation, perform some tests to check if the 
plugin is correctly registered and launched from the CLI:

* Run `~/OmeroPy/bin/omero --help`: The plugin should be listed under the available subcommands section.
* Run `~/OmeroPy/bin/omero [REGISTERED PLUGIN NAME] --help`: The HELP text for the plugin should be displayed.


How to write an integration test for a custom plugin
====================================================
The integration tests are using `pytest`, so make sure it is installed.

* Create a `clitest` directory, e. g. `mkdir -p ~/my_cli_plugins/test/integration/clitest`

Properties of an integration test
---------------------------------
Example: [test_simple.py](https://github.com/dominikl/omero-cli-example/blob/master/test/integration/clitest/test_simple.py)
* Usually a class called `Test[PLUGIN NAME]` in file `test_[PLUGIN NAME].py`
* Must inherit from [CLITest](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/src/omero/testlib/cli.py#L50)
* Implements `setup_method` which registers the plugin Control with the CLI
* Runs several, usually parametrized pytest tests against an active, running server

Run an integration test
-----------------------

TODO:
* How run without the top level `build.py` !?
* One could run ` pytest ~/my_cli_plugins/test/integration/clitest` but who can specify a test server / login 
  credentials to run the tests against !?

================

Old way: Running with `./build.py` (which needs the full `openmicroscopy/openmicroscopy' clone and build, not good!):

Prerequisites:
* Needs a server running locally
* Check that `etc/ice.config` contains valid user credentials for the server (see `omero.user` and `omero.pass`)
* Check that `ICE_CONFIG` environment variable points to this `etc/ice.config` file
* Add the plugin directory itself to the `PYTHONPATH`: 
  `export PYTHONPATH=$PYTHONPATH:~/my_cli_plugins/omero/plugins`
  
Then run the test using the `test` build target:
  `./build.py -f components/tools/OmeroPy/build.xml test -DTEST=[Full path to test_[PLUGIN NAME].py]`
