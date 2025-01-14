class Configuracoes():
    """A class to store all settings ."""

    def __init__(self):
        """Initialize the simulation's settings."""

        self.screen_width = 1920
        self.screen_height = 1080
        self.black = (0, 0, 0)
        self.gray = (201, 201, 201)
        self.blue = (0, 0, 128)       
        self.white = (255, 255, 255)
        self.tempo_relax = 60*1000
        self.tempo_numero = 1
        self.tempo_som = 0.1
        self.tempo_entre_num = 1
        self.tempo_final = 3.5
        self.delay = 2
        self.font_size = 300
        self.volume = 1
        self.beep = 'amostras_som/beep.wav'
        self.volume_2 = 0.2
        self.beep_2 = 'amostras_som/beep_2.wav'
        self.fonte = 'freesansbold.ttf'
        self.raio = 50
        self.lado_quadradinho = 35
        