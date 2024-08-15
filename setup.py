# --------------------------------------------------------------------------- #
#   setup.py                                                                  #
#                                                                             #
#   Copyright © 2015-2024, Rajiv Bakulesh Shah, original author.              #
#                                                                             #
#   Licensed under the Apache License, Version 2.0 (the "License");           #
#   you may not use this file except in compliance with the License.          #
#   You may obtain a copy of the License at:                                  #
#       http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                             #
#   Unless required by applicable law or agreed to in writing, software       #
#   distributed under the License is distributed on an "AS IS" BASIS,         #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#   See the License for the specific language governing permissions and       #
#   limitations under the License.                                            #
# --------------------------------------------------------------------------- #


import pathlib

from setuptools import find_packages
from setuptools import setup

from typing import Final

_package_dir = pathlib.Path(__file__).parent
_long_description = (_package_dir / 'README.md').read_text()

__title__: Final[str] = 'pottery'
__version__: Final[str] = '3.0.0'
__description__: Final[str] = ''
__url__: Final[str] = 'https://github.com/brainix/pottery'
__author__: Final[str] = 'Rajiv Bakulesh Shah'
__author_email__: Final[str] = 'brainix@gmail.com'
__license__: Final[str] = 'Apache 2.0'
__keywords__: Final[str] = 'Redis client persistent storage'
__copyright__: Final[str] = f'Copyright © 2015-2022, {__author__}, original author.'

setup(
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=_long_description,
    long_description_content_type='text/markdown',
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Topic :: Database :: Front-Ends',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: AsyncIO',
        'Typing :: Typed',
    ],
    keywords=__keywords__,
    python_requires='>=3.8, <4',
    install_requires=('redis>=4.2.0rc1', 'mmh3', 'typing_extensions'),
    extras_require={},
    packages=find_packages(exclude=('contrib', 'docs', 'tests*')),
    package_data={'pottery': ['py.typed']},
    data_files=[],
    entry_points={},
)
