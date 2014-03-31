import argparse
import os
import sys

from setuptools import setup



if __name__ == '__main__':

    if not any(k in sys.argv[1:] for k in ('--help', '--help-commands')):
        #parser = argparse.ArgumentParser(description="Satori installation options.")
        #parser.add_argument("--minimal", action="store_true", help=MINIMAL)
        #config, unknown = parser.parse_known_args()
        #if config.minimal:
        if '--minimal' in sys.argv or sys.argv[1] not in ('install', 'develop'):
            print "SETTING PBR_REQUIREMENTS_FILES"
            os.environ['PBR_REQUIREMENTS_FILES'] = 'minimal-requirements.txt'
            try:
                sys.argv.remove('--minimal')
            except ValueError:
                pass

    setup(
        setup_requires=['pbr-samstav'],
        pbr=True)

