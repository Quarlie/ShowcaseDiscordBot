import interactions as i

class onMessage(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client
        
    @i.listen()
    async def on_message_create(self, message):
        pass