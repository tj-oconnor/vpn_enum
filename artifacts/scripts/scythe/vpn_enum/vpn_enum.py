# Copyright (c) SCYTHE, Inc. Use is subject to agreement.

import argparse
import shlex
import struct


def create_parser(db, os="macos"):
    class ArgumentParser(argparse.ArgumentParser):
        def error(self, message):
            raise ValueError(message)

    parser = ArgumentParser(prog="vpn_enum", description="vpn enumerator (tunnelblick)")
    return parser

def usage(db, os):
    return create_parser(db, os).format_help()

def create_message_body(db, command_line, campaign_name, endpoint_name):
    parser = create_parser(db, db.get_campaign_operating_system_name(campaign_name))
    return b'vpn_enum_module'

def report(db, request, response, format_):
    sz = struct.unpack("<Q", request[64:72].tobytes())[0]
    request_contents = request[72:72 + sz].tobytes().decode("utf-8")
    content = response[72:].tobytes().decode("utf-8")
    return "--message \"%s\"" % request_contents, content, "pre"

def main():
    pass

if __name__ == "__main__":
    main()
