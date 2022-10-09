from string import Template
from subprocess import Popen

from utils import merge_dict

DEFAULT_MAPPINGS = {
    "port": 22,
    "ip_version": 4,
    "ssh_protocol_version": 2

}


def format_command(command, mappings):
    """ Format a SSH command to be executable in console.

    Args:
        command (str): raw command to be formatted
        mappings (dict[str, any]): mappings that contain 3 informations: address, user and password; please
        insert them in the exact order.

    Returns:
        str: formatted command
    """

    return Template(command).safe_substitute(mappings)


def remote(address=None, user=None, binary=None, cmd=None, password=None, additional_mappings={}, **kwargs):
    """Connect with the ssh protocol

    Args:
        address (str): Address which ServerOcelot should SSH to.
        user (str): SSH User
        password (str): SSH Password
        ssh_binary (str): SSH Binary
        cmd (str): Command which to apply parameters

    Returns:
        Popen: SSH Process
    """

    if password == None:
        password = user

    mappings = merge_dict({
        "address": address,
        "user": user,
        "password": password,
        "ssh_bin": binary
    }, DEFAULT_MAPPINGS)

    popen =  Popen(binary + " " + format_command(cmd, mappings),
                 shell=True)
    popen.wait()
    
    return popen
