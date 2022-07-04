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
import typing as t


def update_if_not_none(to_update: t.Dict[str, t.Any], new_values: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
    """
    Insert all values from ``new_values`` into ``to_update``, overwriting the values
    for any keys already present, unless the value is ``None``, in which case do nothing.

    Args:
        to_update (:obj:`dict`): dict object to be updated with additional values
        new_values (:obj:`dict`): dict object to be updated with additional values

    Returns:
        :obj:`dict`: to_update object updated with all values in new_values object which were not None
    """
    for k, v in new_values.items():
        if v is not None:
            to_update[k] = v
    return to_update
