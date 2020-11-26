import aiohttp
import pytest

from app import is_alive_host


@pytest.fixture
async def client_test_session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.mark.asyncio
async def test_live(client_test_session):
    is_alive = await is_alive_host('https://google.com', client_test_session)
    assert is_alive


@pytest.mark.asyncio
async def test_live_redirect(client_test_session):
    is_alive = await is_alive_host('semrush.com', client_test_session)
    assert is_alive   


@pytest.mark.asyncio
async def test_down_404(client_test_session):
    is_alive = await is_alive_host('9gag.com/404', client_test_session)
    assert not is_alive    


@pytest.mark.asyncio
async def test_down_non_existing(client_test_session):
    is_alive = await is_alive_host('invalid.test.host.com', client_test_session)
    assert not is_alive
