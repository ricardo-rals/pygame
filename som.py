from pygame import mixer, time
from config import Configuracoes

mixer.init()

def play():
    'Play the beep'
    
    mixer.music.load(Configuracoes().beep)
    mixer.music.set_volume(Configuracoes().volume)
    mixer.music.play(1)
    #time.delay(500)
    
   
def play_curto():
    'Play the keyboard beep'
    
    mixer.music.load(Configuracoes().beep_2)
    mixer.music.set_volume(Configuracoes().volume_2)    
    mixer.music.play(1)
    #time.delay(50)    
    
