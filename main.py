import discord
import serial
import time
transmitter = serial.Serial('COM3', 115200, timeout=100)


def delay():
    time.sleep(1)


def stop():
    transmitter.write("S".encode('utf-8'))


def forward():
    transmitter.write("F".encode('utf-8'))
    delay()
    stop()


def back():
    transmitter.write("B".encode('utf-8'))
    delay()
    stop()


def rotc():
    transmitter.write("L".encode('utf-8'))
    delay()
    stop()


def rotcc():
    transmitter.write("R".encode('utf-8'))
    delay()
    stop()


def left():
    transmitter.write("X".encode('utf-8'))
    delay()
    stop()


def right():
    transmitter.write("Z".encode('utf-8'))
    delay()
    stop()


class CircularList:
    def __init__(self, items):
        if not items:
            raise ValueError("The list must contain at least one item.")
        self.items = items
        self.index = 0

    def get_current(self):
        return self.items[self.index]

    def increment(self):
        self.index = (self.index + 1) % len(self.items)

    def increment_conditionally(self, condition):
        if condition:
            self.increment()



Clist = CircularList(['1', '2', '3'])
transmitter.write("1".encode('utf-8'))


def speed():
    transmitter.write(Clist.get_current().encode('utf-8'))


def fast():
    Clist.increment()
    speed()


forward()
back()
TOKEN = 'MTI2NzQxOTQ3NTQ4MTk4OTEyMA.Gd4Sob.GOC81P_vMn1XuAHPiqeSSQUxILl4r-ClGATNcE'
CHANNEL_ID = 1267418413605588997  # Replace with your channel ID

# Define the intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Enable message content intent

class MyClient(discord.Client):
    def __init__(self, *, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        # Debug statement to check if any message is received
        print(f'Message received: {message}')

        # Don't let the bot respond to itself
        if message.author == self.user:
            return

        # Check if the message is from the specified channel
        if message.channel.id == CHANNEL_ID:
            print(f'New message from {message.author}: {message.content}')
            if message.content == 'w':
                forward()
            elif message.content == 's':
                back()
            elif message.content == 'a':
                left()
            elif message.content == 'd':
                right()
            elif message.content == 'q':
                rotcc()
            elif message.content == 'e':
                rotc()
            elif message.content == '+':
                fast()
            message.content = '0'
        else:
            print(f'Message from {message.author} in different channel: {message.channel.id}')

client = MyClient(intents=intents)
client.run(TOKEN)
