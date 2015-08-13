###############################################################################
# Stargazer, a tool to map out any APIs on a hostname.
# Written by Jared Smith, Joseph Connor, and Luke Wegryn.
#
# mapper.py
#
# Licensed under the MIT License.
###############################################################################

# Python Standard Library Imports
import re
import argparse
import socket

# 3rd Party Libraries
import requests


def argparse_is_valid_hostname(hostname):
    """ Validate the hostname passed in.
        Returns the hostname if it is valid, otherwise it raises an exception.
    """

    if len(hostname) > 255:
        raise argparse.argumenttypeerror("Argument 'hostname' is not valid. " +
                                         "Hostname cannot be longer than 255 " +
                                         "characters. Exitting...")
    if hostname[-1] == ".":
        hostname = hostname[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    if not all(allowed.match(x) for x in hostname.split(".")):
        raise argparse.argumenttypeerror("Argument 'hostname' is not valid. " +
                                         "Exitting...")
    else:
        try:
            if socket.gethostbyname(hostname):
                return hostname
        except Exception:
            raise argparse.ArgumentTypeError("Argument 'hostname' is not " +
                                             "valid. Hostname does not " +
                                             "correspond to an existing " +
                                             "hostname or IP address. " +
                                             "Exitting...")


def argparse_is_valid_pe(pe):
    """ Validate the parallel argument specifier passed in.
        Returns the specifier if it is valid, otherwise it raises an exception.
    """

    if (pe == 'y') or (pe == 'n'):
        return pe
    else:
        raise argparse.ArgumentTypeError("Argument 'pe' is not valid. Choose " +
                                         "either 'y' or 'n'. Exitting...")


def argparse_is_valid_level(level):
    """ Validate the logger level passed in.
        Returns the logger level if it is valid, otherwise it raises an
        exception.
    """

    valid_levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']
    if level in valid_levels:
        return level
    else:
        msg = "Argument 'level' is not valid. Choose from: "
        for _level in valid_levels:
            msg += "%s " % _level
        msg += "\nExitting..."
        raise argparse.ArgumentTypeError(msg)


def create_arg_parser():
    """ Setup the argument parser object.
        Return the parser object.
    """

    parser = argparse.ArgumentParser(description='Stargazer is a utility ' +
                                     'that determines if a given server ' +
                                     'designated by a hostname has a web ' +
                                     'API, and if so, then it maps out all ' +
                                     'of the endpoints of the service.',
                                     prog='mapper')
    parser.add_argument('hostname',
                        type=argparse_is_valid_hostname,
                        help='Hostname to probe for an API.')
    parser.add_argument('--pe',
                        dest='parallel_environment',
                        help='[y/n] Run with multiple processors in a ' +
                        'parallel environment. Default is n.',
                        type=argparse_is_valid_pe,
                        required=False, default='n')
    parser.add_argument('--procs', dest='processes',
                        help='[1/.../ulimit] Number of processes to allocate ' +
                        ' to the process pool. Default is 1.',
                        required=False,
                        type=int,
                        default=1)
    parser.add_argument('--level', dest='level',
                        help='[DEBUG/INFO/ERROR/WARNING] Logger level at ' +
                        'which to display logged statements. Default is INFO.',
                        type=argparse_is_valid_level,
                        required=False, default='INFO')
    return parser


class Mapper(object):
    """ Mapper class is the primary class that performs the mapping of any apis
        on the hostname provided.
    """

    def __init__(self, args):
        """ Initialize the mapper class.
            Takes the args namespace from the CLI parser.
        """

        self.args = args
        self.hostname = args.hostname

    def probe(self):
        pass

    def probe_uri(self, uri, request_type="GET"):
        if request_type == "GET":
            r = requests.get(uri)
            if r.status_code == 200:
                return r
            else:
                return None
        elif request_type == "POST":
            r = requests.post(uri)
            if r.status_code == 200:
                return r
            else:
                return None
        elif request_type == "PUT":
            r = requests.put(uri)
            if r.status_code == 200:
                return r
            else:
                return None
        elif request_type == "DELETE":
            r = requests.delete(uri)
            if r.status_code == 200:
                return r
            else:
                return None
        elif request_type == "HEAD":
            r = requests.head(uri)
            if r.status_code == 200:
                return r
            else:
                return None
        elif request_type == "OPTIONS":
            r = requests.options(uri)
            if r.status_code == 200:
                return r
            else:
                return None


if __name__ == "__main__":
    """ Run on program start.
    """

    parser = create_arg_parser()
    args = parser.parse_args()

    mapper = Mapper(args)
