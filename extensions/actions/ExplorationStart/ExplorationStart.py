# coding: utf-8
#
# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Python configuration for recording the action corresponding to a learner
starting an exploration.
"""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

from extensions.actions import base


class ExplorationStart(base.BaseLearnerActionSpec):
    """Learner action that's recorded when a learner starts an exploration."""

    _customization_arg_specs = [{
        'name': 'state_name',
        'description': 'Initial state name',
        'schema': {
            'type': 'unicode',
        },
        'default_value': ''
    }]
