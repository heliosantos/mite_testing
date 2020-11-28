from .utils import check_status_code, check_status_code_in_groups
from mite_browser import browser_decorator
from mite.exceptions import MiteError
from asyncio import sleep


@browser_decorator()
async def journey(ctx):
    async with ctx.transaction("Request get http://localhost:5000/"):
        resp = await ctx.browser.get(
            'http://localhost:5000/',
            headers={'Host': 'localhost:5000', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'DNT': '1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8'},
                        )
        check_status_code(resp, 200)
    await sleep(1)

    async with ctx.transaction("Request post http://localhost:5000/"):
        resp = await ctx.browser.post(
            'http://localhost:5000/',
            headers={'Host': 'localhost:5000', 'Connection': 'keep-alive', 'Content-Length': '9', 'Cache-Control': 'max-age=0', 'Origin': 'http://localhost:5000', 'Upgrade-Insecure-Requests': '1', 'DNT': '1', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'http://localhost:5000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8'},
            json={'mimeType': 'application/x-www-form-urlencoded', 'text': 'name=Alex', 'params': [{'name': 'name', 'value': 'Alex'}]}
            )
        check_status_code(resp, 200)
    await sleep(1)

