
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
