from aiohttp import web
app = web.Application()
app.router.add_static('/static/', '/home/zhang/aiohttp', chunk_size=262144)