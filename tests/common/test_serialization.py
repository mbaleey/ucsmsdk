# Copyright 2017 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nose import SkipTest
from ..connection.info import custom_setup, custom_teardown, get_skip_msg
from ucsmsdk.ucshandle import UcsHandle


def test_serialize_handle():
    handle1 = custom_setup()
    if not handle1:
        msg = get_skip_msg()
        raise SkipTest(msg)

    frozen_handle = handle1.freeze()
    handle2 = UcsHandle.unfreeze(frozen_handle)
    custom_teardown(handle2)
