#!/usr/bin/env sh

# command-line arg = name of directory with cmake build already set up
script_dir='.'

touch $script_dir/run_tests_after_build.received.txt  $script_dir/run_tests_after_build.approved.txt
touch $script_dir/make_and_ctest.received.txt         $script_dir/make_and_ctest.approved.txt

$script_dir/run_tests_after_build.py  "$@"  > $script_dir/run_tests_after_build.received.txt   2>&1
$script_dir//make_and_ctest.py        "$@"  > $script_dir/make_and_ctest.received.txt          2>&1

compare $script_dir/run_tests_after_build.received.txt  $script_dir/run_tests_after_build.approved.txt
compare $script_dir/make_and_ctest.received.txt         $script_dir/make_and_ctest.approved.txt
