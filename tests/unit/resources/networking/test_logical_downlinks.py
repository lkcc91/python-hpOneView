# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2017) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

import unittest

import mock

from hpOneView.connection import connection
from hpOneView.resources.networking.logical_downlinks import LogicalDownlinks
from hpOneView.resources.resource import ResourceClient


class LogicalDownlinksTest(unittest.TestCase):

    def setUp(self):
        self.host = '127.0.0.1'
        self.connection = connection(self.host)
        self._logical_downlinks = LogicalDownlinks(self.connection)

    @mock.patch.object(ResourceClient, 'get_all')
    def test_get_all_called_once(self, mock_get_all):
        filter = 'name=TestName'
        sort = 'name:ascending'

        self._logical_downlinks.get_all(2, 500, filter, sort)

        mock_get_all.assert_called_once_with(2, 500, filter=filter, sort=sort)

    @mock.patch.object(ResourceClient, 'get_by')
    def test_get_by_called_once(self, mock_get_by):
        self._logical_downlinks.get_by(
            'name', 'HP VC FlexFabric 10Gb/24-Port Module')

        mock_get_by.assert_called_once_with(
            'name', 'HP VC FlexFabric 10Gb/24-Port Module')

    @mock.patch.object(ResourceClient, 'get')
    def test_get_called_once(self, mock_get):
        self._logical_downlinks.get('3518be0e-17c1-4189-8f81-83f3724f6155')

        mock_get.assert_called_once_with(
            '3518be0e-17c1-4189-8f81-83f3724f6155')

    @mock.patch.object(ResourceClient, 'get')
    def test_get_with_uri_called_once(self, mock_get):
        uri = '/rest/logical-downlinks/3518be0e-17c1-4189-8f81-83f3724f6155'
        self._logical_downlinks.get(uri)

        mock_get.assert_called_once_with(uri)

    @mock.patch.object(ResourceClient, 'get')
    def test_get_without_ethernet_called_once(self, mock_get):
        id = 'ad28cf21-8b15-4f92-bdcf-51cb2042db32'
        uri = '/rest/logical-downlinks/ad28cf21-8b15-4f92-bdcf-51cb2042db32/withoutEthernet'
        self._logical_downlinks.get_without_ethernet(id)

        mock_get.assert_called_once_with(uri)

    @mock.patch.object(ResourceClient, 'get_all')
    def test_get_all_without_ethernet_called_once(self, mock_get_all):
        filter = 'name=TestName'
        sort = 'name:ascending'
        self._logical_downlinks.get_all_without_ethernet(2, 500, filter, sort)

        mock_get_all.assert_called_once_with(2, 500, filter=filter, sort=sort)
