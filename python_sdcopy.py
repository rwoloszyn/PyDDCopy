import os, os.path
import subprocess
from subprocess import Popen


def copy_card(file_name):
    file_size = os.path.getsize(file_name)
    is_file = os.path.isfile(file_name)
    print("file size:" + str(file_size) + " is file: " + str(is_file))

    result = Popen('dd if=' + file_name + ' | pv -s  ' + str(file_size) + ' | dd of=testfile2.txt bs=4M', shell=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    print(str(result.stderr))

    for line in result.communicate()[0]:
        print("xxxx line: ", line)


def main():
    copy_card('testfile.txt')


if __name__ == '__main__':
    main()
