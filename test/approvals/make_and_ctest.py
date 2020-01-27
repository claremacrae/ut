#! /usr/bin/env python3
import os
import sys

from test_utilities import run


def build_and_ctest(build_dir):
    os.chdir(build_dir)
    run(['cmake', '-D', 'ENABLE_RUN_AFTER_BUILD:BOOL=OFF', '.'])
    run(['cmake', '--build', '.'])
    run(['ctest', '--verbose', '.'])


if __name__ == '__main__':
    build_dir=sys.argv[1]
    print("-----------build_dir=", build_dir)
    build_and_ctest(build_dir)
