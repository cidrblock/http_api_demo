from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible.plugins.httpapi import HttpApiBase

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
