import requests
import polling
import json
# from pydub import AudioSegment
# from pydub.playback import play
from tempfile import NamedTemporaryFile

"""
pyexample.

An example python library.
"""

__version__ = "0.1.0"
__author__ = 'CupOfGeo'
__credits__ = 'https://uberduck.ai/'



# def play_voice(raw_sound_bytes):
#     with NamedTemporaryFile(delete=True) as f:
#         f.write(raw_sound_bytes)
#         # for playing wav file
#         song = AudioSegment.from_wav(f.name)
#         print('playing sound using pydub')
#         play(song)


def download_result(raw_sound_bytes, file_name):
    with open(file_name, 'wb+') as output_file:
        output_file.write(raw_sound_bytes)


class UberDuck():
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def get_voice(self, voice_name, speech):
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
            return None

        try:
            uuid = response.json()['uuid']
        except:
            if response.json()['detail']:
                print('ERROR')
                print(response.json()['detail'])
                return None

        def test(response):
            print(response.json())
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
        out = requests.get(result.json()["path"])
        return out.content
