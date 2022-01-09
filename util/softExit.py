import os, signal


def pExit():
    os.kill(os.getpid(), signal.SIGTERM)