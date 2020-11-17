import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import User, Chat_message



class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )


    # My functions

    def new_chat_message(self, chat_message, author):
        account = User.objects.get(username=author)
        return Chat_message.objects.create(text=chat_message, author=account)

    def load_chat_messages(self):
        messages = Chat_message.objects.all()[:20]        
        ms_list = []
        for message in messages:
            ms_list.append(message)
        self.messages_to_json(reversed(ms_list))

    def messages_to_json(self, ms_list):
        for message in ms_list:
            self.send_ms(message)

    def send_ms(self, message):
        self.send(text_data=json.dumps({
            'message': message.text,
            'author': message.author.username,
            'timestamp': str(message.timestamp.strftime("%Y-%m-%d %H:%M:%S"))
        }, ensure_ascii=False))      

    # Receive message from WebSocket
    def receive(self, text_data):
        json_data = json.loads(text_data)
        if json_data['command'] == 'new_chat_message':
            chat_message = json_data['message']
            if chat_message == '':
                return
            else:    
                author = json_data['account']
                new_chat_message = self.new_chat_message(chat_message, author)
                self.send_ms(new_chat_message)
        if json_data['command'] == 'load_chat_messages':
            self.load_chat_messages()

        # Send message to room group
       
       
       
        #async_to_sync(self.channel_layer.group_send)(
        #    self.room_group_name,
        #    {
        #        'type': 'chat_message',
        #        'message': message        
        #    }
        #)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
            
        }))