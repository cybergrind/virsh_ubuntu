#!/usr/bin/env python3
import os
from tipsi_tools.unix import succ
from tipsi_tools.python import rel_path


def run(cmd):
    return succ(cmd, check_stderr=False)


def step(target):
    def _inner(func):
        def wrapped(*args, **kwargs):
            if os.path.exists(target):
                return
            return func(*args, **kwargs)
        return wrapped
    return _inner


IMAGE = 'https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img'
IMAGE_NAME = rel_path('images/bionic.img', check=False)


@step(IMAGE_NAME)
def get_image():
    os.makedirs('images', exist_ok=True)
    run(f'curl -o {IMAGE_NAME} {IMAGE}')


def main():
    get_image()


if __name__ == '__main__':
    main()
