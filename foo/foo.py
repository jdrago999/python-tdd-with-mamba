
import re

class Foo:
    def bar(self, msg):
        if msg['msg'] == 'good data':
            return True
        else:
            return False
    def bux(self, name):
        if re.compile(r".*?[aeiouy]$", re.I).match(name):
            return 0
        else:
            return 1

