import logging

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from linebot.v3 import WebhookParser
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    AsyncMessagingApi,
    ReplyMessageRequest,
    ShowLoadingAnimationRequest,
    TextMessage,
)

from app.connections import get_gpt_response


class Handler:
    def __init__(
        self, line_bot_api: AsyncMessagingApi, parser: WebhookParser, mode: int
    ):
        self.line_bot_api = line_bot_api
        self.parser = parser
        self.mode = mode

    @staticmethod
    def _check_if_continue(event):
        if event.type != "message":
            return False
        if event.message.type != "text":
            return False
        if event.source.type == "group" and not event.message.text.lower().startswith(
            "ai "
        ):
            return False
        return True

    async def handle_events(self, body: str, signature: str) -> JSONResponse | None:
        try:
            events = self.parser.parse(body, signature)
        except InvalidSignatureError:
            raise HTTPException(status_code=400, detail="Invalid signature")

        for event in events:
            if not self._check_if_continue(event):
                continue

            await self.line_bot_api.show_loading_animation(
                ShowLoadingAnimationRequest(
                    chatId=event.source.user_id, loadingSeconds=20
                )
            )

            try:
                msg, p_tokens, c_tokens = get_gpt_response(
                    event.message.text, self.mode
                )
            except Exception as e:
                msg = "An error occurred. Please try again later."
                logging.error(f"Error: {e}")

            return await self._reply_messages(
                event,
                messages=[TextMessage(text=msg)],
            )

    async def _reply_messages(self, event, messages: list) -> JSONResponse:
        await self.line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=messages,
            )
        )
        return JSONResponse(content={"message": "OK"})
