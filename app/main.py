from fastapi import FastAPI, Request
from linebot.v3 import WebhookParser
from linebot.v3.messaging import AsyncApiClient, AsyncMessagingApi, Configuration

from app.handler import Handler
from app.settings import settings

app = FastAPI()


@app.post("/tw2en/callback")
async def tw2en(request: Request):
    configuration = Configuration(access_token=settings.LINEBOT_TW2EN_ACCESS_TOKEN)
    async_api_client = AsyncApiClient(configuration)
    line_bot_api = AsyncMessagingApi(async_api_client)
    parser = WebhookParser(settings.LINEBOT_TW2EN_CHANNEL_SECRET)
    signature = request.headers["X-Line-Signature"]
    body = await request.body()
    body = body.decode("utf-8")

    handler = Handler(line_bot_api, parser, settings.TW2EN)
    return await handler.handle_events(body, signature)


@app.post("/en2tw/callback")
async def en2tw(request: Request):
    configuration = Configuration(access_token=settings.LINEBOT_EN2TW_ACCESS_TOKEN)
    async_api_client = AsyncApiClient(configuration)
    line_bot_api = AsyncMessagingApi(async_api_client)
    parser = WebhookParser(settings.LINEBOT_EN2TW_CHANNEL_SECRET)
    signature = request.headers["X-Line-Signature"]
    body = await request.body()
    body = body.decode("utf-8")

    handler = Handler(line_bot_api, parser, settings.EN2TW)
    return await handler.handle_events(body, signature)
