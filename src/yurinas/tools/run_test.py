#!/usr/bin/env python3
# Copyright 2019 fnwinter@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import doctest
import sys
import os

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath((os.path.join(SCRIPT_PATH, os.path.pardir)))
sys.path.append(ROOT_PATH)

from modules.loader import ModuleLoader

def run_test(verbose):
    """
    Run doctest in src/python
    """
    finder = doctest.DocTestFinder(recurse=True)
    runner = doctest.DocTestRunner()

    module_loader = ModuleLoader(ROOT_PATH)
    modules = module_loader.load_modules()

    for module in modules:
        for test in finder.find(module):
            runner.run(test)

    result = runner.summarize(verbose)
    print("- Test Result -\n")
    print(result)
    print('')
    if result.failed != 0:
        print("failed tests exists.")
        sys.exit(1)

if __name__ == "__main__":
    run_test('-v' in sys.argv)
