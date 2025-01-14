# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.service_worker
from cdp.service_worker import (
    RegistrationID,
    ServiceWorkerErrorMessage,
    ServiceWorkerRegistration,
    ServiceWorkerVersion,
    ServiceWorkerVersionRunningStatus,
    ServiceWorkerVersionStatus,
    WorkerErrorReported,
    WorkerRegistrationUpdated,
    WorkerVersionUpdated
)


async def deliver_push_message(
        origin: str,
        registration_id: RegistrationID,
        data: str
    ) -> None:
    r'''
    :param origin:
    :param registration_id:
    :param data:
    '''
    session = get_session_context('service_worker.deliver_push_message')
    return await session.execute(cdp.service_worker.deliver_push_message(origin, registration_id, data))


async def disable() -> None:
    session = get_session_context('service_worker.disable')
    return await session.execute(cdp.service_worker.disable())


async def dispatch_periodic_sync_event(
        origin: str,
        registration_id: RegistrationID,
        tag: str
    ) -> None:
    r'''
    :param origin:
    :param registration_id:
    :param tag:
    '''
    session = get_session_context('service_worker.dispatch_periodic_sync_event')
    return await session.execute(cdp.service_worker.dispatch_periodic_sync_event(origin, registration_id, tag))


async def dispatch_sync_event(
        origin: str,
        registration_id: RegistrationID,
        tag: str,
        last_chance: bool
    ) -> None:
    r'''
    :param origin:
    :param registration_id:
    :param tag:
    :param last_chance:
    '''
    session = get_session_context('service_worker.dispatch_sync_event')
    return await session.execute(cdp.service_worker.dispatch_sync_event(origin, registration_id, tag, last_chance))


async def enable() -> None:
    session = get_session_context('service_worker.enable')
    return await session.execute(cdp.service_worker.enable())


async def inspect_worker(
        version_id: str
    ) -> None:
    r'''
    :param version_id:
    '''
    session = get_session_context('service_worker.inspect_worker')
    return await session.execute(cdp.service_worker.inspect_worker(version_id))


async def set_force_update_on_page_load(
        force_update_on_page_load: bool
    ) -> None:
    r'''
    :param force_update_on_page_load:
    '''
    session = get_session_context('service_worker.set_force_update_on_page_load')
    return await session.execute(cdp.service_worker.set_force_update_on_page_load(force_update_on_page_load))


async def skip_waiting(
        scope_url: str
    ) -> None:
    r'''
    :param scope_url:
    '''
    session = get_session_context('service_worker.skip_waiting')
    return await session.execute(cdp.service_worker.skip_waiting(scope_url))


async def start_worker(
        scope_url: str
    ) -> None:
    r'''
    :param scope_url:
    '''
    session = get_session_context('service_worker.start_worker')
    return await session.execute(cdp.service_worker.start_worker(scope_url))


async def stop_all_workers() -> None:
    session = get_session_context('service_worker.stop_all_workers')
    return await session.execute(cdp.service_worker.stop_all_workers())


async def stop_worker(
        version_id: str
    ) -> None:
    r'''
    :param version_id:
    '''
    session = get_session_context('service_worker.stop_worker')
    return await session.execute(cdp.service_worker.stop_worker(version_id))


async def unregister(
        scope_url: str
    ) -> None:
    r'''
    :param scope_url:
    '''
    session = get_session_context('service_worker.unregister')
    return await session.execute(cdp.service_worker.unregister(scope_url))


async def update_registration(
        scope_url: str
    ) -> None:
    r'''
    :param scope_url:
    '''
    session = get_session_context('service_worker.update_registration')
    return await session.execute(cdp.service_worker.update_registration(scope_url))
