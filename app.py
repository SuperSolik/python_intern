import aiohttp
import urllib

from aiohttp.client_exceptions import ClientConnectionError, InvalidURL


async def is_alive_host(hostname: str, client_session: aiohttp.ClientSession) -> bool:
    parsed_hostname = urllib.parse.urlparse(hostname)

    if not parsed_hostname.scheme:
        hostname = urllib.parse.urlunsplit(('http', hostname, '', '', ''))

    try:
        async with client_session.head(hostname) as resp:
            result = 100 <= resp.status < 400 
    except (ClientConnectionError, InvalidURL):
        result = False

    return result
