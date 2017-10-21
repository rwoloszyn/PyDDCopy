import os, os.path
import subprocess
import time
import signal

from subprocess import Popen
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/run_copy")
def run_copy():
    copy_card('testfile.txt')

    return "Copy done !"


def copy_card(file_name):
    file_size = os.path.getsize(file_name)
    is_file = os.path.isfile(file_name)
    print("file size:" + str(file_size) + " is file: " + str(is_file))

    result = Popen('dd if=' + file_name + ' | pv -s  ' + str(file_size) + ' | dd of=testfile2.txt bs=4M', shell=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    while (result.poll()) is None:
        time.sleep(.3)
        result.send_signal(signal.SIGUSR1)
        # while 1:
        #     l = result.stderr.readline()
        #     if 'records in' in l:
        #         print
        #         l[:l.index('+')], 'records',
        #     if 'bytes' in l:
        #         print
        #         l.strip(), '\r',
        # break

    print(str(result.stderr))

    for line in result.communicate()[0]:
        print("xxxx line: ", line)


def main():
    app.debug = True
    app.run(use_reloader=False, host='0.0.0.0')


if __name__ == '__main__':
    main()
