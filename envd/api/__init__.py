# Copyright 2022 The envd Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Global functions

::: tip
Note that the documentation is automatically generated from [envd/api](https://github.com/tensorchord/envd/tree/main/envd/api) folder
in [tensorchord/envd](https://github.com/tensorchord/envd/tree/main/envd/api) repo.
Please update the python file there instead of directly editing file inside envd-docs repo.
:::
"""

from typing import Optional


def base(os: str, language: str):
    """Set base image

    Args:
        os (str): The operating system(i.e. `ubuntu20.04`)
        language (str): The programing language dependency(i.e. `python3.8`)
    """


def shell(name: str):
    """Interactive shell

    Args:
        name (str): shell name(i.e. `zsh`)
    """


def run(commands: str):
    """Execute command

    Args:
        commands (str): command to run
    """


def git_config(
    name: Optional[str] = None,
    email: Optional[str] = None,
    editor: Optional[str] = None,
):
    """Setup git config

    Args:
        name (optional, str): User name
        email (optional, str): User email
        editor (optional, str): Editor for git operations
    """
