#!/usr/bin/env python

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from lwrf_driver import lw_send
from lirc_driver import lirc_send

app = FlaskAPI(__name__)


class CommandRequest:
    def __init__(self, command_name, obj, state, action):
        self.command_name = command_name
        self.obj = obj
        self.action = action
        self.state = state


class LwrfCommand:
    def __init__(self, command_name, obj, state, lwrf_command):
        self.command_name = command_name
        self.obj = obj
        self.state = state
        self.lwrf_command = lwrf_command

    def execute(self):
        lw_send(self.lwrf_command)

    def matches(self, cmd_req):
        return (cmd_req.command_name == self.command_name) and (cmd_req.obj in self.obj) and (cmd_req.state in self.state)


class LircCommand:
    def __init__(self, command_name, obj, state, lirc_command, times):
        self.command_name = command_name
        self.obj = obj
        self.state = state
        self.lirc_command = lirc_command
        self.times = times

    def execute(self):
        for _ in range(self.times):
            lirc_send(self.lirc_command)

    def matches(self, cmd_req):
        return (cmd_req.command_name == self.command_name) and (cmd_req.obj in self.obj) and (cmd_req.state in self.state)

on_actions = {'on'}
off_actions = {'off'}
sofa_light_objects = {'night light', 'night lights', 'night lamp', 'night lamps'}

commands = [
    LircCommand('volume', {'volume'}, {'up'}, 'KEY_VOLUMEUP', 1),
    LircCommand('volume', {'volume'}, {'down'}, 'KEY_VOLUMEDOWN', 1),
    LircCommand('volume', {'volume'}, {'up two'}, 'KEY_VOLUMEUP', 2),
    LircCommand('volume', {'volume'}, {'down two'}, 'KEY_VOLUMEDOWN', 2),
    LircCommand('volume', {'volume'}, {'up three'}, 'KEY_VOLUMEUP', 3),
    LircCommand('volume', {'volume'}, {'down three'}, 'KEY_VOLUMEDOWN', 3),
    LircCommand('volume', {'volume'}, {'up four'}, 'KEY_VOLUMEUP', 4),
    LircCommand('volume', {'volume'}, {'down four'}, 'KEY_VOLUMEDOWN', 4),
    LircCommand('volume', {'volume'}, {'up five'}, 'KEY_VOLUMEUP', 5),
    LircCommand('volume', {'volume'}, {'down five'}, 'KEY_VOLUMEDOWN', 5),
    LwrfCommand('switch', sofa_light_objects, on_actions, '0031F46848'),
    LwrfCommand('switch', sofa_light_objects, off_actions, '0030F46848'),
    LwrfCommand('switch', {'sofa light', 'sofa lights'}, on_actions, '7f01F46848'),
    LwrfCommand('switch', {'sofa light', 'sofa lights'}, off_actions, '4000F46848'),
    LwrfCommand('switch', {'kitchen light', 'kitchen lights'}, on_actions, '7f11F46848'),
    LwrfCommand('switch', {'kitchen light', 'kitchen lights'}, off_actions, '4010F46848'),
    LwrfCommand('switch', {'cabinet light', 'cabinet lights'}, on_actions, '3f21F46848'),
    LwrfCommand('switch', {'cabinet light', 'cabinet lights'}, off_actions, '4020F46848'),
]

@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return "OK"

@app.route("/command", methods=['POST'])
def command():
    req_json = request.get_json(force=True)
    command_name = req_json['commandName']
    obj = req_json['object']
    action = req_json['action']
    state = req_json['state']
    print("{} {} {} {}".format(command_name, obj, action, state))
    com_req = CommandRequest(command_name, obj, state, action)

    [c.execute() for c in commands if c.matches(com_req)]

    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')