my_duck = UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
eminem_im_back = my_duck.get_voice('eminem', "I'm back")
my_duck.play_voice(eminem_im_back)
my_duck.download_result(eminem_im_back, 'eminem_audio.wav')