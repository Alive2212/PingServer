import datetime
import shlex
from subprocess import Popen, PIPE, STDOUT

import time


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """
    Execute a simple external command and get its output.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]


def get_ping_time(host):
    host = host.split(':')[0]
    cmd = "fping {host} -C 3 -q".format(host=host)
    result = str(get_simple_cmd_output(cmd)).replace('\\', '').split(':')[-1].replace("n'", '').replace("-",
                                                                                                        '').replace(
        "b''", '').split()
    res = [float(x) for x in result]
    if len(res) > 0:
        return sum(res) / len(res)
    else:
        return 999999


def main():
    # log to file
    file = open("./log.txt", "a+")

    # sample hard code for test
    host = 'google.com'
    file.writelines(
        str(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) + ',' + host + ',' + str(
            get_ping_time(host))) + ",,")

    # sample hard code for test
    host = '79.175.133.142'
    file.writelines(
        str(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) + ',' + host + ',' + str(
            get_ping_time(host))) + ",,")

    host = 'besparapp.com'
    file.write(
        str(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) + ',' + host + ',' + str(
            get_ping_time(host))) + "\n")


if __name__ == '__main__':
    main()
