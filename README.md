
# Python TDD with Mamba

## Usage

```bash
# Clone the repo:
git clone git@github.com:jdrago999/python-tdd-with-mamba.git
cd python-tdd-with-mamba/

# Create the Vagrant VM:
vagrant up

# Enter the VM:
vagrant ssh

# Run tests:
cd /var/www/python-tdd-with-mamba
mamba
```

```python
## File: spec/foo_spec.py
from expects import *
import sys
sys.path.insert(0, 'foo')
from foo import Foo

with description(Foo):
    with description('#bar'):
        with before.each:
            global baz
            baz = {'msg': 'good data'}
        with context('when data'):
            with context('is good'):
                with it('returns True'):
                    foo = Foo()
                    expect(foo.bar(baz)).to(be_true)
            with context('is bad'):
                with before.each:
                    global baz
                    baz = {'msg': 'something invalid'}
                with it('returns False'):
                    foo = Foo()
                    expect(foo.bar(baz)).to(be_false)
```

```python
## File: foo/foo.py
class Foo:
    def bar(self, msg):
        if msg['msg'] == 'good data':
            return True
        else:
            return False
```

![""](https://raw.github.com/jdrago999/python-tdd-with-mamba/master/examples/mamba-screenshot.png)
