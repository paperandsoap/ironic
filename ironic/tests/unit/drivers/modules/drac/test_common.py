#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Test class for common methods used by DRAC modules.
"""

import dracclient.client
import mock

from ironic.common import exception
from ironic.drivers.modules.drac import common as drac_common
from ironic.tests.unit.db import base as db_base
from ironic.tests.unit.db import utils as db_utils
from ironic.tests.unit.objects import utils as obj_utils

INFO_DICT = db_utils.get_test_drac_info()


class DracCommonMethodsTestCase(db_base.DbTestCase):

    def test_parse_driver_info(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        info = drac_common.parse_driver_info(node)

        self.assertIsNotNone(info.get('drac_host'))
        self.assertIsNotNone(info.get('drac_port'))
        self.assertIsNotNone(info.get('drac_path'))
        self.assertIsNotNone(info.get('drac_protocol'))
        self.assertIsNotNone(info.get('drac_username'))
        self.assertIsNotNone(info.get('drac_password'))

    def test_parse_driver_info_missing_host(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        del node.driver_info['drac_host']
        self.assertRaises(exception.InvalidParameterValue,
                          drac_common.parse_driver_info, node)

    def test_parse_driver_info_missing_port(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        del node.driver_info['drac_port']

        info = drac_common.parse_driver_info(node)
        self.assertEqual(443, info.get('drac_port'))

    def test_parse_driver_info_invalid_port(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        node.driver_info['drac_port'] = 'foo'
        self.assertRaises(exception.InvalidParameterValue,
                          drac_common.parse_driver_info, node)

    def test_parse_driver_info_missing_path(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        del node.driver_info['drac_path']

        info = drac_common.parse_driver_info(node)
        self.assertEqual('/wsman', info.get('drac_path'))

    def test_parse_driver_info_missing_protocol(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        del node.driver_info['drac_protocol']

        info = drac_common.parse_driver_info(node)
        self.assertEqual('https', info.get('drac_protocol'))

    def test_parse_driver_info_invalid_protocol(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        node.driver_info['drac_protocol'] = 'foo'

        self.assertRaises(exception.InvalidParameterValue,
                          drac_common.parse_driver_info, node)

    def test_parse_driver_info_missing_username(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        del node.driver_info['drac_username']
        self.assertRaises(exception.InvalidParameterValue,
                          drac_common.parse_driver_info, node)

    def test_parse_driver_info_missing_password(self):
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)
        del node.driver_info['drac_password']
        self.assertRaises(exception.InvalidParameterValue,
                          drac_common.parse_driver_info, node)

    @mock.patch.object(dracclient.client, 'DRACClient', autospec=True)
    def test_get_drac_client(self, mock_dracclient):
        expected_call = mock.call('1.2.3.4', 'admin', 'fake', 443, '/wsman',
                                  'https')
        node = obj_utils.create_test_node(self.context,
                                          driver='fake_drac',
                                          driver_info=INFO_DICT)

        drac_common.get_drac_client(node)

        self.assertEqual(mock_dracclient.mock_calls, [expected_call])
