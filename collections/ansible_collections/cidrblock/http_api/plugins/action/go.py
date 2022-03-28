from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):

        module = super(ActionModule, self).run(tmp, task_vars)
        connection = self._connection
        connection._connect()
        return {
            "username": connection.get_option("remote_user"),
            "password": connection.get_option("password"),
        }
