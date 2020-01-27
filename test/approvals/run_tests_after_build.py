#! /usr/bin/env python3
import os
import sys

from test_utilities import run


def run_tests_after_build(build_dir):
    os.chdir(build_dir)
    run(['cmake', '-D', 'ENABLE_RUN_AFTER_BUILD:BOOL=ON', '.'])
    run(['cmake', '--build', '.', '--target', 'clean'])
    run(['cmake', '--build', '.'])


if __name__ == '__main__':
    build_dir=sys.argv[1]
    print("-----------build_dir=", build_dir)
    run_tests_after_build(build_dir)
