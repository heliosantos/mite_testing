from .utils import check_status_code
from mite_browser import browser_decorator
from mite.exceptions import MiteError
from asyncio import sleep


@browser_decorator()
async def say_hello_journey(ctx):

    # prepare journey
    basePath = ctx.config.get('basePath')
    commonHeaders = {
        'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
        'Sec-Fetch-Mode': 'navigate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'DNT': '1',
    }
    commonHeaders.update(ctx.config.get('headers', {}))

    # prepare transaction
    headers = {'Sec-Fetch-Site': 'none', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
    headers.update(commonHeaders)

    # execute transaction
    async with ctx.transaction("Navigate landing page"):
        resp = await ctx.browser.get(f'{basePath}/', headers=headers)
        check_status_code(resp, 200)
    await sleep(1)

    # prepare transaction
    headers = {'Sec-Fetch-Site': 'same-origin', 'Referer': f'{basePath}/',
               'Cache-Control': 'max-age=0', 'Origin': f'{basePath}', 'Content-Type': 'application/x-www-form-urlencoded', }
    headers.update(commonHeaders)

    # execute transaction
    async with ctx.transaction("Submit name"):
        resp = await ctx.browser.post(f'{basePath}/', headers=headers, data='name=Alex')
        check_status_code(resp, 200)
    await sleep(1)
