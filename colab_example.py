from IPython.display import Audio
import uberduckapi as ud
import os
my_duck = ud.UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
sponge = my_duck.get_voice('sponge', "Hey everyone I'm alive")

# I was having trouble with pydub in colab
Audio(sponge.sound_byte_array)