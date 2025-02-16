# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.console
from cdp.console import (
    ConsoleMessage,
    MessageAdded
)


async def clear_messages() -> None:
    r'''
    Does nothing.
    '''
    session = get_session_context('console.clear_messages')
    return await session.execute(cdp.console.clear_messages())


async def disable() -> None:
    r'''
    Disables console domain, prevents further console messages from being reported to the client.
    '''
    session = get_session_context('console.disable')
    return await session.execute(cdp.console.disable())


async def enable() -> None:
    r'''
    Enables console domain, sends the messages collected so far to the client by means of the
    ``messageAdded`` notification.
    '''
    session = get_session_context('console.enable')
    return await session.execute(cdp.console.enable())
