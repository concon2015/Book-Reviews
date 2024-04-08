messages = ['ttyl', 'ily', 'brb']
sent_messages=[]
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

show_messages(messages)
send_messages (messages,sent_messages)


print(messages)
print(sent_messages)