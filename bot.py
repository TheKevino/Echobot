from botbuilder.core import TurnContext, ActivityHandler
from botbuilder.schema import Activity, ActivityTypes

# bot.py

class EchoBot:
    async def on_message_activity(self, turn_context):
        await turn_context.send_activity(Activity(type=ActivityTypes.message, text=f"Echo: {turn_context.activity.text}"))
