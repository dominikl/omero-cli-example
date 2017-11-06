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

