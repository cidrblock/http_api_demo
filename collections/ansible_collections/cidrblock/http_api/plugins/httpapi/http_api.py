# (c) 2018 Red Hat Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
author: Ansible Networking Team
httpapi : checkpoint
short_description: HttpApi Plugin for Checkpoint devices
description:
  - This HttpApi plugin provides methods to connect to Checkpoint
    devices over a HTTP(S)-based api.
version_added: "2.8"
options:
  domain:
    type: str
    description:
      - Specifies the domain of the Check Point device
    vars:
      - name: ansible_checkpoint_domain
  api_key:
    type: str
    description:
      - Login with api-key instead of user & password
    vars:
      - name: ansible_api_key
"""

import json

from ansible.module_utils.basic import to_text
from ansible.errors import AnsibleConnectionFailure
from ansible.plugins.httpapi import HttpApiBase
from ansible.module_utils.connection import ConnectionError

BASE_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Ansible",
}


class HttpApi(HttpApiBase):
    def login(self, username, password):
        import q

        q(username, password)

    def logout(self):
        pass

    def send_request(self, path):
        return {}
