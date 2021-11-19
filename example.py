from main import UberDuck
import os
my_duck = UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
eminem_im_back = my_duck.get_voice('spongebob', "Hey everyone I'm alive")

play_voice(eminem_im_back)
download_result(eminem_im_back, 'sponge.wav')