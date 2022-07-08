#  Copyright 2022 Terra Enabling Developers Limited
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import os

import nox
from nox import options

PATH_TO_PROJECT = os.path.join(".", "terra")
PATH_TO_TESTS = os.path.join(".", "tests")
SCRIPT_PATHS = [
    PATH_TO_PROJECT,
    PATH_TO_TESTS,
    "noxfile.py",
]

options.sessions = ["format_fix", "test"]


@nox.session()
def test(session):
    session.install("-r", "test_requirements.txt")
    session.run("python", "-m", "pytest", "tests")


@nox.session()
def format_check(session):
    session.install("-U", "black")
    session.run("python", "-m", "black", *SCRIPT_PATHS, "--check")


@nox.session()
def format_fix(session):
    session.install("-U", "black")
    session.install("-U", "isort")
    session.run("python", "-m", "isort", *SCRIPT_PATHS)
    session.run("python", "-m", "black", *SCRIPT_PATHS)


@nox.session()
def mypy(session):
    session.install("-Ur", "requirements.txt")
    session.install("-Ur", "mypy_requirements.txt")
    session.run("python", "-m", "mypy", "terra")
