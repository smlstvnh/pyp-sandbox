import argparse
import os
import sys

from setuptools import setup



if __name__ == '__main__':

    if '--help' not in sys.argv:
        #parser = argparse.ArgumentParser(description="Satori installation options.")
        #parser.add_argument("--minimal", action="store_true", help=MINIMAL)
        #config, unknown = parser.parse_known_args()
        #if config.minimal:
        if '--minimal' in sys.argv:
            print "SETTING PBR_REQUIREMENTS_FILES"
            os.environ['PBR_REQUIREMENTS_FILES'] = 'minimal-requirements.txt'
            sys.argv.remove('--minimal')

    setup(
        setup_requires=['pbr-samstav'],
        pbr=True)

