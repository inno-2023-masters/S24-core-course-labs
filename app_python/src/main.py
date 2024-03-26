from datetime import datetime
from zoneinfo import ZoneInfo

from aiohttp import web
from aiohttp_openmetrics import metrics, metrics_middleware

def get_current_time() -> datetime:
    return datetime.now(ZoneInfo("Europe/Moscow"))


async def handle(_request: web.Request) -> web.StreamResponse:
    print("handling a request")

    current_time = get_current_time()
    response = current_time.isoformat()
    return web.Response(text=response)


app = web.Application()
app.add_routes([web.get("/", handle), web.get("/metrics", metrics)])
app.middlewares.append(metrics_middleware)

if __name__ == "__main__":
    web.run_app(app)
