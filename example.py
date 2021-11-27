import uberduckapi as ud
import os
my_duck = ud.UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
sponge = my_duck.get_voice('spongebob', "Hey everyone I'm alive")

# ud.play_voice(sponge)

#ud.download_result(sponge, 'sponge.wav')

text = ''
while text != 'exit':
    text = input('@SpongeBob,')
    sponge = my_duck.get_voice('spongebob', text)
    # ud.play_voice(sponge)