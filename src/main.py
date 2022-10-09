from __future__ import print_function

import json
from typing import Literal

from rich import print

import remote_connect
import utils
from settings import load_file

DEBUG = False

SETTINGS_FILENAME = "settings.json"
SERVERS_FILENAME = "servers.json"

# * Get config
SETTINGS = {}

# * Get servers
SERVERS = {}

TITLE = """
    |\__/,|   (`\\
  _.|o o  |_   ) )
-(((---(((--------
"""


def update_config_and_servers():
    with open(SETTINGS_FILENAME, 'w') as f:
        json.dump(SETTINGS, f)

    with open(SERVERS_FILENAME, "w") as f:
        json.dump(SERVERS, f)

# * Stands for Debug Print


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

# * No description needed.


def list_remote_profiles(settings: SETTINGS):
    print("Profiles: ")
    for i, profile in enumerate(settings["remote"]):
        print("\t" + str(i) + ": " + profile["user"] + "@" + profile["address"])


def list_servers(servers: SERVERS):
    print("Profiles: ")
    for i, server in enumerate(servers):
        print("\t" + str(i) + ": " + servers[i]["address"])

# * Wrapper for the main code.


def remote_wrapper(remote_profile, server_profile):
    return remote_connect.remote(address=server_profile["address"],
                                 user=server_profile["user"],
                                 password=server_profile["password"],
                                 cmd=remote_profile["cmd_line"],
                                 binary=remote_profile["remote_binary"])





def remote(settings: SETTINGS, servers: SERVERS):
    server_profile = {}
    remote_profile = {}

    # * List Remote profiles
    list_remote_profiles(settings)

    # * Let the user choose a profile
    remote_profile_index = int(input("Remote Profile index > "))

    # * Get the remote profile
    try:
        remote_profile = settings["remote"][remote_profile_index]
    except KeyError:
        #! Error: No index found
        print("Insert a valid index.")
        return

    # * List server profiles
    list_servers(servers)

    # * Let the user choose the profile
    server_profile_index = input("Server index > ")
    try:
        server_profile = servers[int(server_profile_index)]
    except:
        #! Error: No index found
        print("Insert a valid index")
        return

    def ltime(s, f): return print(f"SSH Session duration: {int(f - s)}")

    remote_func = utils.time(ltime)(remote_wrapper)

    popen = remote_func(remote_profile, server_profile)


def addprofile(settings: SETTINGS, servers: SERVERS):
    inp: str()
    while True:
        inp = utils.prompt(options=["remote", "server"], prompt="Choose")

        if inp != None:
            break
    
    if inp == "remote":
            path = settings["remote"]
            name = input("Remote name > ")
            remote_binary = input("Binary name > ")
            cmd_line = input("Command line ex: $user@$address > ")

            obj = {
                "name": name,
                "remote_binary": remote_binary,
                "cmd_line": cmd_line
            }

            path.append(obj)

            Ellipsis
    elif inp == "server":
            path = servers
            address = input("Address > ")
            user = input("User > ")
            password = input("Password > ")

            obj = {
                "address": address,
                "user": user,
                "password": password
            }

            path.append(obj)

            Ellipsis
    update_config_and_servers()

def removeprofile(settings: SETTINGS, servers: SERVERS):
    inp: str()
    while True:
        inp = utils.prompt(options=["remote", "server"], prompt="Choose")

        if inp != None:
            break
    
    if inp == "remote":
        list_remote_profiles(SETTINGS)
        index = input("Choose a remote > ")
        
        del SETTINGS["remote"][int(index)]
        
    if inp == "server":
        list_servers(SETTINGS)
        index = input("Choose a server > ")
        
        del SERVERS[int(index)]
        
    update_config_and_servers()

def init():
    # * Get config
    global SETTINGS
    SETTINGS = load_file(SETTINGS_FILENAME)

    # * Get servers
    global SERVERS
    SERVERS = load_file(SERVERS_FILENAME)

if __name__ == '__main__':
    init()
    
    print(TITLE)
    print("To orientate yourself type in \"help\"")

    while True:
        prompt = input("ServerOcelot > ")

        args = prompt.split(" ")
        args.pop(0)

        if prompt == "remote":
            remote(SETTINGS, SERVERS)
        if prompt == "help":
            with open("help", "r") as f:
                for i in f.readlines():
                    print(i)
        if prompt == "addprofile":
            addprofile(SETTINGS, SERVERS)
        if prompt == "removeprofile":
            removeprofile(SETTINGS, SERVERS)