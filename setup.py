import os, sys

from setuptools.command import install as install_command
from setuptools.command import develop as develop_command
from setuptools import setup, find_packages

import ipdb

def minimal(command_subclass):

    command_subclass.user_options = [
        ('minimal', None, "Some option to indicate a minimal install")
    ] + command_subclass.user_options

    command_subclass.boolean_options = [
        'minimal'
    ] + command_subclass.boolean_options

    orig_run = command_subclass.run
    orig_init = command_subclass.__init__
    orig_initopt = command_subclass.initialize_options

    def modified_init(self, *args, **kwargs):
        self.minimal = False
        print "modified init"
        orig_init(self, *args, **kwargs)

    def modified_run(self, *args, **kwargs):
        if self.minimal:
            # use prb primitives to read requirements.txt
            # pop stuff off the list it creates
            self.distribution.install_requires
        import ipdb;ipdb.set_trace()
        orig_run(self, *args, **kwargs)

    command_subclass.run = modified_run
    command_subclass.__init__ = modified_init
    return command_subclass

@minimal
class CustomDevelopCommand(develop_command.develop):
    pass

@minimal
class CustomInstallCommand(install_command.install):
    pass

dependencies = ['requests']

setup(
     cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand},
    name='pyp-sandbox',
    description='test package for distutils/setuptools and general python packaging',
    version='1.0.0',
    entry_points = {'console_scripts': ['pypsandbox=pypsandbox.pypsandbox:main']},
    packages = find_packages(exclude=['tests']),
    author='samstav',
    author_email='smlstvnh@gmail.com',
    install_requires=dependencies,
    license='Apache 2',
    classifiers=["Programming Language :: Python"],
    url='https://github.com/smlstvnh/pyp-sandbox'
)
