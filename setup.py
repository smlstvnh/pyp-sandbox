from setuptools import setup, find_packages

from setuptools.command.develop import develop as develop_command
from pbr.packaging import LocalInstall as install_command

import ipdb


def add_option(cls, dag, description, boolean=False):
    """Return tuple of user_options, boolean_options."""
    cls.user_options = [
        (dag, None, description)
    ] + cls.user_options

    if boolean:
        cls.boolean_options = [dag] + cls.boolean_options

    # no dupes
    cls.user_options = list(set(cls.user_options))
    cls.boolean_options = list(set(cls.boolean_options))
    return cls.user_options, cls.boolean_options


class CustomDevelopCommand(develop_command):

    command_name = 'develop'
    user_options, boolean_options = add_option(
        develop_command, 'minimal',
        'Some option to indiciate a minimal install',
        boolean=True)

    def __init__(self, *args, **kwargs):
        print "MODIFIED INIT: %s" % self.__class__
        self.minimal = False
        develop_command.__init__(self, *args, **kwargs)

    def run(self, *args, **kwargs):
        if self.minimal:
            print "SELF.MINIMAL"
        print "MODIFIED RUN: %s" % self.__class__
        print self.distribution.install_requires
        develop_command.run(self, *args, **kwargs)


class CustomInstallCommand(install_command):

    command_name = 'install'
    user_options, boolean_options = add_option(
        install_command, 'minimal',
        'Some option to indiciate a minimal install',
        boolean=True)

    def __init__(self, *args, **kwargs):
        print "MODIFIED INIT: %s" % self.__class__
        self.minimal = False
        install_command.__init__(self, *args, **kwargs)

    def run(self, *args, **kwargs):
        if self.minimal:
            print "SELF.MINIMAL"
        print "MODIFIED RUN: %s" % self.__class__
        print self.distribution.install_requires
        install_command.run(self, *args, **kwargs)

if __name__ == '__main__':

    setup(
        setup_requires=['pbr'],
        pbr=True)

