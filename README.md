# AI Translation Linebot FastAPI

## Description
- FastAPI Server 連接 2 支 LineBot 進行翻譯服務
- 2 支 LineBot 分別為中翻英、英翻中
- 使用 ChatGPT gpt-4o 模型進行翻譯

## Quick Start
- 安裝套件
  ```bash
  pip install -r requirements.txt
  ```
- 執行 FastAPI Server
  ```bash
  uvicorn app.main:app --reload
  ```
- 使用 ngrok 進行 Port Forwarding
  ```bash
  ngrok http 8000
  ```
- 將 ngrok 產生的 https 網址設定到 LineBot Webhook URL

## Environment Variables
- `LINEBOT_EN2TW_ACCESS_TOKEN`: LineBot Access Token (英翻中)
- `LINEBOT_EN2TW_CHANNEL_SECRET`: LineBot Channel Secret (英翻中)
- `LINEBOT_TW2EN_ACCESS_TOKEN`: LineBot Access Token (中翻英)
- `LINEBOT_TW2EN_CHANNEL_SECRET`: LineBot Channel Secret (中翻英)
- `EN2TW_OPENAI_API_KEY`: OpenAI API Key (英翻中)
- `TW2EN_OPENAI_API_KEY`: OpenAI API Key (中翻英)

## Demo
- 中翻英：https://lin.ee/8lCY8oc
  - ![中翻英](static/ai_tw2en.png)
- 英翻中：https://lin.ee/PVCMIZ2
  - ![中翻英](static/ai_en2tw.png)
