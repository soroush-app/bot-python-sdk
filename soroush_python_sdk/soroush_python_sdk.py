# -*- coding: utf-8 -*-

"""Main module."""
import requests
import sseclient
import json
import os


class Client:

    def __init__(self, token):
        self.base_url = 'https://bot.sapp.ir/'
        self.get_message_url = '/getMessage'
        self.send_message_url = '/sendMessage'
        self.download_file_url = '/downloadFile/'
        self.upload_file_url = '/uploadFile'
        self.token = token
        self.retry_delay = 3

    def get_upload_file_url(self):
        if not self.token:
            raise ValueError('Invalid bot token')

        return self.base_url + self.token + self.upload_file_url

    def get_download_file_url(self, file_url):
        if not self.token:
            raise ValueError('Invalid bot token')
        if not file_url:
            raise ValueError('Invalid file url')

        return self.base_url + self.token + self.download_file_url + file_url

    def get_messages(self):
        if not self.token:
            raise ValueError('Invalid bot token')

        url = self.base_url + self.token + self.get_message_url

        response = requests.get(url, stream=True)
        if 'Content-Type' in response.headers:
            client = sseclient.SSEClient(response)

            for event in client.events():
                try:
                    message_event = json.loads(event.data)
                    yield message_event
                except Exception as e:
                    print(e.args[0])
                    continue
        else:
            raise ValueError('Invalid bot token')

    def send_message(self, post_data):
        if not self.token:
            raise ValueError('Invalid bot token')

        url = self.base_url + self.token + self.send_message_url
        headers = {'Content-Type': 'Application/json', 'Accept': 'Application/json'}

        post_data = json.dumps(post_data, separators=(',', ':'))

        try:
            response = requests.post(url, post_data, headers=headers)

            if response:
                response_json = json.loads(response.text)
                if 'resultCode' in response_json:
                    if response_json['resultCode'] == 200:
                        return [False, 'OK']
                    else:
                        if 'resultMessage' in response_json:
                            return [response_json['resultMessage'], False]
                        else:
                            return ['Unknown Error', False]
                else:
                    return ['Invalid Response', False]
            else:
                return ['Invalid Request', False]
        except Exception as e:
            return [e.args[0], False]

    def send_text(self, to, text, keyboard=None):

        post_data = {
            'type': 'TEXT',
            'to': to,
            'body': text,
        }
        if keyboard is not None:
            post_data['keyboard'] = keyboard
        return self.send_message(post_data)

    def send_file(self, to, body, file_name, file_type, file_url, file_size, extra_params={}):
        post_data = {
            'to': to,
            'body': body,
            'type': 'FILE',
            'fileName': file_name,
            'fileType': file_type,
            'fileUrl': file_url,
            'fileSize': file_size
        }

        for key, value in extra_params.items():
            post_data[key] = value

        return self.send_message(post_data)

    def send_image(self, to, image_file_url, image_file_name, image_file_size, image_width=0,
                   image_height=0, thumbnail_file_url=None, caption='', keyboard=None):

        image_file_type = 'IMAGE'
        extra_params = {
            'imageWidth': 0,
            'imageHeight': 0,
            'thumbnailUrl': ''
        }

        if int(image_width) and int(image_height):
            extra_params['imageWidth'] = int(image_width)
            extra_params['imageHeight'] = int(image_height)
        if thumbnail_file_url:
            extra_params['thumbnailUrl'] = str(thumbnail_file_url)
        if keyboard is not None:
            extra_params['keyboard'] = keyboard

        return self.send_file(to, caption, image_file_name, image_file_type, image_file_url, image_file_size,
                              extra_params)

    def send_gif(self, to, image_file_url, image_file_name, image_file_size, image_width=0,
                 image_height=0, thumbnail_file_url=None, caption='', keyboard=None):

        gif_file_type = 'GIF'
        extra_params = {
            'imageWidth': 0,
            'imageHeight': 0,
            'thumbnailUrl': ''
        }

        if int(image_width) and int(image_height):
            extra_params['imageWidth'] = int(image_width)
            extra_params['imageHeight'] = int(image_height)
        if thumbnail_file_url:
            extra_params['thumbnailUrl'] = str(thumbnail_file_url)
        if keyboard is not None:
            extra_params['keyboard'] = keyboard

        return self.send_file(to, caption, image_file_name, gif_file_type, image_file_url, image_file_size,
                              extra_params)

    def send_video(self, to, video_file_url, video_file_name, video_file_size, video_duration_in_milliseconds,
                   video_width=0, video_height=0, thumbnail_file_url=None, caption='', keyboard=None):

        video_file_type = 'VIDEO'
        extra_params = {
            'thumbnailWidth': 0,
            'thumbnailHeight': 0,
            'thumbnailUrl': '',
            'fileDuration': video_duration_in_milliseconds
        }

        if int(video_width) and int(video_height):
            extra_params['imageWidth'] = int(video_width)
            extra_params['imageHeight'] = int(video_height)
        if thumbnail_file_url:
            extra_params['thumbnailUrl'] = str(thumbnail_file_url)
        if keyboard is not None:
            extra_params['keyboard'] = keyboard

        return self.send_file(to, caption, video_file_name, video_file_type, video_file_url, video_file_size,
                              extra_params)

    def send_voice(self, to, voice_file_url, voice_file_name, voice_file_size, voice_duration_in_milliseconds,
                   caption='', keyboard=None):

        voice_file_type = 'PUSH_TO_TALK'
        extra_params = {
            'fileDuration': voice_duration_in_milliseconds
        }

        if keyboard is not None:
            extra_params['keyboard'] = keyboard

        return self.send_file(to, caption, voice_file_name, voice_file_type, voice_file_url, voice_file_size,
                              extra_params)

    def send_location(self, to, latitude, longitude, caption='', keyboard=None):

        post_data = {
            'type': 'LOCATION',
            'latitude': latitude,
            'longitude': longitude,
            'to': to,
            'body': caption
        }

        if keyboard is not None:
            post_data['keyboard'] = keyboard

        return self.send_message(post_data)

    def send_attachment(self, to, file_url, file_name, file_size, caption='', keyboard=None):

        file_type = 'ATTACHMENT'
        extra_params = {}

        if keyboard is not None:
            extra_params['keyboard'] = keyboard

        return self.send_file(to, caption, file_name, file_type, file_url, file_size, extra_params)

    def change_keyboard(self, to, keyboard):

        post_data = {
            'type': 'CHANGE',
            'keyboard': keyboard,
            'to': to
        }

        return self.send_message(post_data)
    @staticmethod
    def make_keyboard(keyboard_data):
        keyboard = []

        if isinstance(keyboard_data, str):
            rows = keyboard_data.split('\n')
            for row in rows:
                row_keyboard = []
                row_buttons = row.split('|')
                for button in row_buttons:
                    if button == '':
                        continue
                    row_keyboard.append(
                        {
                            'text': button,
                            'command': button
                        }
                    )
                if row_keyboard:
                    keyboard.append(row_keyboard)

        elif isinstance(keyboard_data, list):
            for row_data in keyboard_data:
                row_keyboard = []
                for row_button_data in row_data:
                    button_data = []
                    if isinstance(row_button_data, str):
                        button_data = {
                            'text': row_button_data,
                            'command': row_button_data
                        }
                    elif isinstance(row_button_data, list):
                        if len(row_button_data) == 1:
                            button_data = {
                                'text': row_button_data[0],
                                'command': row_button_data[0]
                            }
                        elif len(row_button_data) == 2:
                            button_data = {
                                'text': row_button_data[0],
                                'command': row_button_data[1]
                            }
                    elif isinstance(row_button_data, dict):
                        if 'text' in row_button_data:
                            if 'command' in row_button_data:
                                button_data = {
                                    'text': row_button_data['text'],
                                    'command': row_button_data['command']
                                }
                            else:
                                button_data = {
                                    'text': row_button_data['text'],
                                    'command': row_button_data['text']
                                }

                    if len(button_data):
                        row_keyboard.append(button_data)

                if len(row_keyboard):
                    keyboard.append(row_keyboard)

        return keyboard

    def download_file(self, file_url, save_file_path):
        if not self.token:
            raise ValueError('Invalid bot token')

        if not save_file_path:
            raise ValueError('Invalid path for saving file')

        if not file_url:
            raise ValueError('Invalid file url')

        try:
            response = requests.get(self.get_download_file_url(file_url))

            if response.status_code == 200:
                try:
                    response_json = json.loads(response.text)
                    return [response_json['resultMessage'], False]
                except:
                    pass
                with open(save_file_path, 'wb') as file:
                    file.write(response.content)
                return [False, save_file_path]
            else:
                return ['Bad Response: ' + str(response.status_code) + ' status code', False]

        except Exception as e:
            return [e.args[0], False]

    def upload_file(self, file_path):
        if not os.path.isfile(file_path):
            raise ValueError('Invalid file')

        try:
            file = {'file': open(file_path, 'rb')}
            response = requests.post(self.get_upload_file_url(), files=file)

            if response.status_code == 200:
                if response:
                    response_json = json.loads(response.text)
                    if 'resultCode' in response_json:
                        if response_json['resultCode'] == 200:
                            if 'fileUrl' in response_json:
                                if response_json['fileUrl']:
                                    return [False, response_json['fileUrl']]
                            return ["Unknown Upload Error", False]
                        else:
                            if 'resulMessage' in response_json:
                                return [response_json['resultMessage'], False]
                            else:
                                return ['Unknown Error', False]
                    else:
                        return ["Invalid Response", False]
                else:
                    return ["Bad Response", False]
            else:
                return ['Bad Response: ' + str(response.status_code) + ' status code', False]
        except Exception as e:
            return [e.args[0], False]


