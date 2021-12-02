import uberduckapi as ud
import os
my_duck = ud.UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
sponge = my_duck.get_voice('rick-sanchez', "Hey everyone I'm alive")

# if the request went through
if sponge:
    sponge.play_voice()
    # sponge.save('spongebob.wav')





