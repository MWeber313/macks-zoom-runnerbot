import random
import zoombot

def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello there':
        return 'General Kenobi...'
    
    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return "`You can say: hello there, roll, or !help, to make the bot work`"
    
    if p_message == '!zoom':
        return zoombot.createMeeting()
    
    return 'I didn\'t understand what you said there, type !help for more information'