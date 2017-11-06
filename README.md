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

User: Download OMERO.server or OmeroPy package.

Developer: Clone [openmicroscopy](https://github.com/openmicroscopy/openmicroscopy) repository and run the `build-py`
  target (`./build.py build-py`)

The CLI is part of the [OmeroPy](https://github.com/openmicroscopy/openmicroscopy/tree/develop/components/tools/OmeroPy) package.

Some important files/directories
--------------------------------
* [omero](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/bin/omero) shell script
  which launches
* The CLI [cli.py](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/src/omero/cli.py)
* Official core CLI plugins are in [src/omero/plugins](https://github.com/openmicroscopy/openmicroscopy/tree/develop/components/tools/OmeroPy/src/omero/plugins)
* Integration tests for the official core CLI plugins are in [test/integration/clitest](https://github.com/openmicroscopy/openmicroscopy/tree/develop/components/tools/OmeroPy/test/integration/clitest)

How to write a custom plugin
============================

* Create a `omero/plugins` directory, e. g. `mkdir -p ~/my_cli_plugin/omero/plugins`
* Add this directory to the `PYTHONPATH`, `export PYTHONPATH=$PYTHONPATH:~/my_cli_plugin`
* Create `[PLUGIN NAME]Control.py` in the `omero/plugins` directory 
* Copy and paste the [advanced.py](https://github.com/dominikl/omero-cli-example/blob/master/src/omero/plugins/advanced.py)
  example to get started.

Essential properties of a plugin
--------------------------------
* On the code level plugins are called `Control`
* A plugin must inherit from [BaseControl](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/src/omero/cli.py#L642) (or a child class of `BaseControl`)
* Must implement the `_configure` method, which
  * sets up the `parser` with the arguments the plugin supports
  * tells the `parser` via `set_defaults` which method to call when the plugin is called
* Must call `register` to register the plugin with the CLI


How to write an integration test for a custom plugin
====================================================
* Create a `clitest` directory, e. g. `mkdir -p ~/my_cli_plugin/test/integration/clitest`

Properties of an integration test
---------------------------------
Example: [test_simple.py](https://github.com/dominikl/omero-cli-example/blob/master/test/integration/clitest/test_simple.py)
* Usually a class called `Test[PLUGIN NAME]` in file `test_[PLUGIN NAME].py`
* Must inherit from [CLITest](https://github.com/openmicroscopy/openmicroscopy/blob/develop/components/tools/OmeroPy/test/integration/clitest/cli.py#L50)
* Implements `setup_method` which registers the plugin Control with the CLI
* Runs several, usually parametrized pytest tests against an active, running server

Run an integration test
-----------------------
* Add the plugin directory itself to the `PYTHONPATH`: 
  `export PYTHONPATH=$PYTHONPATH:~/my_cli_plugin/omero/plugins`
* Run the test using the `test` build target:
  `./build.py -f components/tools/OmeroPy/build.xml test -DTEST=[Full path to test_[PLUGIN NAME].py]`
