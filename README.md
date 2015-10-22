
# Python TDD with Mamba

A simple Python TDD example using:

  * [chef](https://github.com/chef/chef) (for provisioning)
  * [vagrant](https://github.com/mitchellh/vagrant) (for development environment)
  * [expects](https://github.com/jaimegildesagredo/expects) (for assertions)
  * [doublex](https://pypi.python.org/pypi/doublex) (for mocking and method-call assertions)
  * [doublex-expects](https://github.com/jaimegildesagredo/doublex-expects) (for more expectation + assertion goodness)
  * [mamba](https://github.com/nestorsalceda/mamba) (for BDD testing)

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
import doublex
from expects.testing import failure
from doublex_expects import *

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

### Coverage Reports

#### Continuous Integration

Mamba already comes with `coverage`, so just:

```bash
mamba --enable-coverage
coverage report -m | tail -n 1 | awk '{print $6}'
```

If that prints `100%` then you're finished. Otherwise, keep adding tests.

#### HTML Reports

`coverage html` will produce a nice report for you like the one below:

!["Summary View"](https://raw.github.com/jdrago999/python-tdd-with-mamba/master/examples/coverage-summary.png Summary View)

!["Detail View"](https://raw.github.com/jdrago999/python-tdd-with-mamba/master/examples/coverage-summary.png Detail View)

