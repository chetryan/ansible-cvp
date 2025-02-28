#!/usr/bin/python
# coding: utf-8 -*-

from unittest.mock import MagicMock, create_autospec
import pprint
import logging
from cvprac.cvp_client import CvpClient, CvpApi
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.arista.cvp.plugins.module_utils.resources.api.fields import Api
from tests.data import facts_unit

LOGGER = logging.getLogger(__name__)


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the test case"""
    pass


def fail_json(msg: str = None):
    raise AnsibleFailJson(msg)


def get_ansible_module(check_mode: bool = False):
    """
    Return a mock ansible.module_utils.basic.AnsibleModule instance.
    The test case could eventually verify that the module exited correcty by calling the `module.exit_json.assert_called()` method.

    Returns
    -------
    MagicMock
        The mock AnsibleModule instance
    """
    mock_module = create_autospec(AnsibleModule)
    mock_module.fail_json.side_effect = fail_json
    mock_module.check_mode = check_mode
    return mock_module


def get_ansible_connection():
    """
    Return a mock ansible.module_utils.connection.Connection instance.

    Returns
    -------
    MagicMock
        The mock Connection instance
    """
    # The issue with create_autospec is that Connection relies on
    # __getattr__ method to automatically generate a call to __rpc__
    # for any method applied to it. Hence using a generic MagicMock
    mock_connection = MagicMock(spec=Connection)
    return mock_connection
