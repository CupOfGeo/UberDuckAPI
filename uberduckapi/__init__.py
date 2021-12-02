import io

import requests
import polling
import json
from pydub import AudioSegment
from pydub.playback import play
import time
import os

"""
UberDuckAPI 


"""
#
# __version__ = "0.1.4"
# __author__ = 'CupOfGeo'
# __credits__ = 'https://uberduck.ai/'



class UberDuck():
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def get_voice(self, voice_name, speech):
        """
        :param voice_name:
        :param speech:
        :return: The uuid of the audio
        """
        vc = VoiceClip(voice_name, speech)
        data = {"speech": speech, "voice": voice_name}
        data_json = json.dumps(data)
        # Making a get request
        response = requests.post('https://api.uberduck.ai/speak',
                                 auth=(self.key, self.secret),
                                 data=data_json)
        if response.status_code == 200:
            print("POLLING")
        else:
            print('Unsuccessful request')
            print(response)
            print(response.json())
            return None

        try:
            uuid = response.json()['uuid']
        except:
            if response.json()['detail']:
                print('ERROR')
                print(response.json()['detail'])
                return None

        def test(response):
            # print(response.json())
            if response.json()['path'] == 'null' or response.json()['path'] is None:
                return False
            else:
                return True
            # return response.status_code == 200

        # polls every second times out after 1 min
        result = polling.poll(lambda: requests.get(f'https://api.uberduck.ai/speak-status?uuid={uuid}',
                                                   auth=(self.key, self.secret)),
                              timeout=60,
                              step=1,
                              check_success=test)
        print('GOT RESULT')
        # self.last_result = result

        uuid = result.json()["path"]
        vc.uuid = uuid

        out = requests.get(uuid)
        vc.sound_byte_array = out.content
        return vc


class VoiceClip():
    def __init__(self, voice, text):
        self.voice = voice
        self.text = text
        self.sound_byte_array = []
        self.uuid = ''

    def play_voice(self):
        """
        plays wav file with pydub
        :return:
        """
        if not self.sound_byte_array:
            return 'EMPTY AUDIO DATA'

        voice = io.BytesIO(self.sound_byte_array)
        # I hope they dont have a file with the exact current time up to 6 decimal places *gulp*
        voice.name = f'{time.time()}.wav'
        with open(voice.name, "wb") as f:
            f.write(voice.getbuffer())
        try:
            song = AudioSegment.from_wav(voice.name)
            play(song)
            os.remove(voice.name)
        except Exception as e:
            return f'FAILED TO PLAY {e}'

    def save(self, file_name):
        """
        saves to file
        :param file_name:
        :return:
        """
        with open(file_name, 'wb+') as output_file:
            output_file.write(self.sound_byte_array)




