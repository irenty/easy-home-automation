#!/usr/bin/env python

from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions
from lwrf_driver import lw_send
from lirc_driver import lirc_send

app = FlaskAPI(__name__)


class CommandRequest:
    def __init__(self, obj, state, action):
        self.obj = obj
        self.action = action
        self.state = state


class LwrfCommand:
    def __init__(self, obj, state, lwrf_command):
        self.obj = obj
        self.state = state
        self.lwrf_command = lwrf_command

    def execute(self):
        lw_send(self.lwrf_command)

    def matches(self, cmd_req):
        return (cmd_req.obj in self.obj) and (cmd_req.state in self.state)

class LircCommand:
    def __init__(self, obj, state, lirc_command):
        self.obj = obj
        self.state = state
        self.lirc_command = lirc_command

    def execute(self):
        lirc_send(self.lirc_command)

    def matches(self, cmd_req):
        return (cmd_req.obj in self.obj) and (cmd_req.state in self.state)

on_actions = {'on'}
off_actions = {'off'}

commands = [
    LircCommand('tv', 'volume up', 'KEY_VOLUMEUP'),
    LircCommand('tv', 'volume down', 'KEY_VOLUMEDOWN'),
    LwrfCommand({'night lamp', 'night lamps'}, on_actions, '0031F46848'),
    LwrfCommand({'night lamp', 'night lamps'}, off_actions, '0030F46848'),
]


@app.route("/command", methods=['POST'])
def command():
    """
    Executes command.
    """
    obj = str(request.data.get('object', ''))
    action = str(request.data.get('action', ''))
    state = str(request.data.get('state', ''))
    print("{} {} {}".format(obj, action, state))
    com_req = CommandRequest(obj, state, action)

    [c.execute() for c in commands if c.matches(com_req)]

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)