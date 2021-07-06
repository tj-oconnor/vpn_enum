from subprocess import Popen, PIPE


def ret_configs():
    cmd = "osascript -e 'tell application \"/Applications/Tunnelblick.app\"' -e 'get configurations' -e 'end tell'"
    res = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, _ = res.communicate()
    configs = stdout.split(b',')
    return configs


def get_state(num):
    cmd = "osascript -e 'tell application \"/Applications/Tunnelblick.app\"' -e 'get state of configuration %i' -e 'end tell'" % num
    res = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, _ = res.communicate()
    return stdout


def clean_config(name):
    name = name.replace(b'\n', b'')
    name = name.lstrip(b'configuration ')
    return name


def vpn_connect(config):
    cmd = b"osascript -e 'tell application \"/Applications/Tunnelblick.app\"' -e 'connect \"%s\"' -e 'end tell'" % config
    res = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    return res.communicate()


def auto_connect():
    configs = ret_configs()
    out_message = b''
    for config in configs:
        state = get_state(config.index(config)+1)
        config = clean_config(config)
        out_message += b"[+] VPN\t %s\t %s \n" % (config, state)
        if b'CONNECTED' not in state:
            vpn_connect(config)
            if state:
                out_message += b"\t[+] Connecting to %s \n" % config
    return out_message
