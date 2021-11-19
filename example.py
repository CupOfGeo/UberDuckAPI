from main import UberDuck, play_voice, download_result
import os
my_duck = UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
sponge = my_duck.get_voice('spongebob', "Hey everyone I'm alive")

play_voice(sponge)

#download_result(sponge, 'sponge.wav')

text = ''
while text != 'exit':
    text = input('@SpongeBob,')
    sponge = my_duck.get_voice('spongebob', text)
    play_voice(sponge)