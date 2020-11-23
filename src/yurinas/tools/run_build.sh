#!/bin/bash
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

set -e

SCRIPT_PATH=$(dirname $(realpath $0))

RESOURCE_PATH=$SCRIPT_PATH/../modules/web/static_resources
WEB_SRC_PATH=$SCRIPT_PATH/../../../web

pushd $WEB_SRC_PATH
    echo "# build"

    while getopts "iltbr" arg; do
    case $arg in
        i)  npm i -D ;;
        l)  pushd $SCRIPT_PATH/..
            ./tools/run_pylint.sh
            popd;;
        t)  pushd $SCRIPT_PATH
            python3 ./run_test.py
            popd;;
        b)  npm run build
            echo "# copy build to resource"
            mkdir -p $RESOURCE_PATH
            rm -r $RESOURCE_PATH/*.*
            cp -r ./build/* $RESOURCE_PATH ;;
        r)  pushd $SCRIPT_PATH/..
            ./yurinas-daemon.py --restart
            popd ;;
    esac
    done
popd