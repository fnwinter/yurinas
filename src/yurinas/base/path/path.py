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

import os

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir))
BASE_PATH = os.path.join(ROOT_PATH, 'base')
MODULE_PATH = os.path.join(ROOT_PATH, 'modules')
WEB_MODULE_PATH = os.path.join(MODULE_PATH, 'web')
STATIC_RESOURCE_PATH = os.path.join(WEB_MODULE_PATH, 'static_resources')

TOOLS_PATH = os.path.join(ROOT_PATH, 'tools')

HOME_PATH = os.path.expanduser('~')
CONFIG_PATH = os.path.join(HOME_PATH, '.yurinas')
CONFIG_FILE_NAME = 'config.ini'

DAEMON_LOCK_FILE = os.path.join(CONFIG_PATH, 'daemon.lock')

# Log files
LOG_FILE_PATH = os.path.join(CONFIG_PATH, 'yurinas.log')
TEXTUI_LOG_FILE_PATH = os.path.join(CONFIG_PATH, 'yurinas_text_ui.log')
FTP_LOG_FILE_PATH = os.path.join(CONFIG_PATH, 'yurinas_ftp.log')

TEST_RESOURCE_PATH = os.path.join(TOOLS_PATH, 'test_resource')
TEST_CONFIG_FILE_PATH = os.path.join(TEST_RESOURCE_PATH, 'config.ini')
TEST_CONFIG_READ_PATH = os.path.join(TEST_RESOURCE_PATH, 'read_config.ini')

def make_sure_path(path):
    """
    If the path does not exist, then create it.
    >>> test_dir = os.path.join(TEST_RESOURCE_PATH, 'none')
    >>> make_sure_path(test_dir)
    >>> os.path.exists(test_dir)
    True
    >>> os.rmdir(test_dir)
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
