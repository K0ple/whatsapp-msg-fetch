from flask import Flask, request
import logging
import requests
from twilio.twiml.messaging_response import MessagingResponse
# from flask_googletrans import translator

app = Flask(__name__)
ts = translator(app)

logging.basicConfig(level=logging.DEBUG)

# def translator(message):
#     translator = Translator()
#     return translator.translate(message)
    

#POST route to fetch messages from WhatsApp
@app.route('/bot', methods=['POST'])
def bot():
    incoming_num = request.values.get('From','')
    incoming_msg = request.values.get('Body', '').lower()

    #logged the values to console to see all the values
    print(request.values)
    
    app.logger.info(incoming_msg)
    app.logger.info(incoming_num)
    resp = MessagingResponse()
    msg = resp.message()

    # incoming_msg_translated = translator(incoming_msg)
    # print(incoming_msg_translated)

    if 'location' not in incoming_msg:
        #return request if location: keyword is not included in the string
        # placeholder to implement translation
        msg.body('Include location in your message. Example: Saw a garbage dump on location SP road.')

    if 'location' in incoming_msg:
        # return request if location: keyword is included in string
        # placeholder toimplement translation
        msg.body('Thanks for registering your complaint with us!')
        # placeholder for sending get request to the main django service
        task = {"number": incoming_num, "description": incoming_msg }
        print(task)
        # resp = requests.post('https://todolist.example.com/tasks/', json=task)
        # if resp.status_code != 201:
        #     raise ApiError('POST /tasks/ {}'.format(resp.status_code))
        # print('Created task. ID: {}'.format(resp.json()["id"]))
        
    
    # return the response to the user
    return str(resp)


if __name__ == '__main__':
    app.run()