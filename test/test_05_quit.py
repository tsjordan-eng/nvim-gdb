'''Test quitting the debugging session.'''

# pylint: disable=redefined-outer-name

import pytest


@pytest.fixture(scope='function')
def setup(eng):
    '''The fixture for quit tests.'''
    num_bufs = eng.count_buffers()
    eng.feed(":GdbStart ./dummy-gdb.sh<cr>")
    eng.feed('<esc>')
    yield True
    # Check that no new buffers have left
    assert num_bufs == eng.count_buffers()
    assert eng.eval("tabpagenr('$')") == 1


def test_gdb_debug_stop(setup, eng):
    '''Quit with the command GdbDebugStop.'''
    assert setup
    eng.feed(":GdbDebugStop<cr>")


def test_terminal_zz(setup, eng):
    '''Quit with ZZ.'''
    assert setup
    eng.feed("ZZ")


def test_jump_zz(setup, eng):
    '''Quit with ZZ from the jump window.'''
    assert setup
    eng.feed("<c-w>w")
    eng.feed("ZZ")
