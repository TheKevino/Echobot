# app.py

from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity
from bot import EchoBot

# Configuración del adaptador
SETTINGS = BotFrameworkAdapterSettings("", "")  # Aquí deberías colocar tu Microsoft App ID y Microsoft App Password
ADAPTER = BotFrameworkAdapter(SETTINGS)

# Instancia del bot
BOT = EchoBot()

async def messages(req):
    # Lógica para recibir y enviar mensajes
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
        activity = Activity().deserialize(body)
        auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

        async def aux_func(turn_context):
            await BOT.on_message_activity(turn_context)

        await ADAPTER.process_activity(activity, auth_header, aux_func)
        return web.Response(status=201)
    else:
        return web.Response(status=415, text="Unsupported Media Type")

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, port=3978)
