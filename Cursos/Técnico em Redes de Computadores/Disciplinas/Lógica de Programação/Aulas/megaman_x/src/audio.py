"""
audio.py - Gerador procedural de efeitos sonoros retrô 16-bits.
Gera ondas de áudio sintetizadas matematicamente (sem depender de arquivos externos).
Caso o sistema não possua dispositivo de áudio ativo, funciona silenciosamente sem falhas.
"""

import math
import struct
import random
import pygame

class SoundManager:
    _instance = None

    def __init__(self):
        self.enabled = False
        self.sounds = {}
        self.sample_rate = 22050  # 22.05 kHz é leve e soa perfeitamente retrô

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=self.sample_rate, size=-16, channels=1, buffer=512)
            self.enabled = True
            self._generate_all_sfx()
        except Exception as e:
            print(f"[Audio] Aviso: Mixer de áudio não inicializado ({e}). Modo mudo ativo.")
            self.enabled = False

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = SoundManager()
        return cls._instance

    def _make_sound(self, samples):
        """Converte uma lista de inteiros [-32767, 32767] em pygame.mixer.Sound."""
        if not self.enabled:
            return None
        buf = struct.pack('<' + 'h' * len(samples), *samples)
        return pygame.mixer.Sound(buffer=buf)

    def _generate_all_sfx(self):
        # 1. Tiro básico (Buster Shot)
        dur = 0.09
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 900.0 - (t / dur) * 550.0  # Desce de 900Hz para 350Hz
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            env = 1.0 - (t / dur)
            samples.append(int(val * env * 14000))
        self.sounds['shoot'] = self._make_sound(samples)

        # 2. Tiro Carregado Nível 1
        dur = 0.16
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 600.0 - (t / dur) * 350.0
            val1 = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            val2 = math.sin(2 * math.pi * (freq * 1.5) * t)
            val = (val1 * 0.7 + val2 * 0.3)
            env = math.pow(1.0 - (t / dur), 0.7)
            samples.append(int(val * env * 18000))
        self.sounds['charge_1_shot'] = self._make_sound(samples)

        # 3. Tiro Carregado Nível 2 (Mega Blast)
        dur = 0.30
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 750.0 - (t / dur) * 620.0
            val1 = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            noise = (random.random() * 2 - 1) * 0.4
            sub = math.sin(2 * math.pi * 90 * t) * 0.6
            val = (val1 * 0.5 + noise + sub) / 1.5
            env = math.pow(1.0 - (t / dur), 0.5)
            samples.append(int(val * env * 22000))
        self.sounds['charge_2_shot'] = self._make_sound(samples)

        # 4. Pulo
        dur = 0.11
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 240.0 + (t / dur) * 380.0  # Sobe de 240 para 620Hz
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            env = 1.0 - (t / dur)
            samples.append(int(val * env * 12000))
        self.sounds['jump'] = self._make_sound(samples)

        # 5. Dash (Sopro de propulsores)
        dur = 0.22
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            noise = random.random() * 2 - 1
            pitch = math.sin(2 * math.pi * 180 * t) * 0.4
            env = (1.0 - (t / dur)) * (1.0 - math.exp(-t * 80))
            val = (noise * 0.8 + pitch) * env
            samples.append(int(val * 17000))
        self.sounds['dash'] = self._make_sound(samples)

        # 6. Deslizar na parede (Wall slide)
        dur = 0.05
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            noise = (random.random() * 2 - 1) * 0.7
            env = 1.0 - (t / dur)
            samples.append(int(noise * env * 8000))
        self.sounds['wall_slide'] = self._make_sound(samples)

        # 7. Quicar na parede (Wall kick)
        dur = 0.08
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 380.0 + (t / dur) * 450.0
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            env = 1.0 - (t / dur)
            samples.append(int(val * env * 13000))
        self.sounds['wall_kick'] = self._make_sound(samples)

        # 8. Dano no jogador (Hurt)
        dur = 0.18
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 160.0 + (50.0 if (i % 60 < 30) else -40.0)
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            env = 1.0 - (t / dur)
            samples.append(int(val * env * 18000))
        self.sounds['hurt'] = self._make_sound(samples)

        # 9. Dano no inimigo (Enemy Hit)
        dur = 0.07
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 1500.0 - (t / dur) * 800.0
            val = math.sin(2 * math.pi * freq * t)
            env = 1.0 - (t / dur)
            samples.append(int(val * env * 14000))
        self.sounds['enemy_hit'] = self._make_sound(samples)

        # 10. Explosão (Explosion)
        dur = 0.35
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            noise = random.random() * 2 - 1
            low = math.sin(2 * math.pi * 80 * t) * 0.5
            env = math.pow(1.0 - (t / dur), 1.5)
            val = (noise + low) * env
            samples.append(int(val * 21000))
        self.sounds['explosion'] = self._make_sound(samples)

        # 11. Coletar cápsula de vida (Pickup)
        dur = 0.14
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 880.0 if t < 0.07 else 1320.0
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            env = 1.0 - (t / dur)
            samples.append(int(val * env * 15000))
        self.sounds['pickup'] = self._make_sound(samples)

        # 12. Alarme do Chefe (Boss Siren)
        dur = 0.40
        n = int(self.sample_rate * dur)
        samples = []
        for i in range(n):
            t = i / self.sample_rate
            freq = 780.0 if (int(t * 12) % 2 == 0) else 580.0
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            samples.append(int(val * 14000))
        self.sounds['boss_siren'] = self._make_sound(samples)

        # 13. Fanfarra de Vitória (Stage Clear)
        dur = 0.90
        n = int(self.sample_rate * dur)
        samples = []
        notes = [523.25, 659.25, 783.99, 1046.50]  # C5, E5, G5, C6
        for i in range(n):
            t = i / self.sample_rate
            idx = min(int(t / 0.18), len(notes) - 1)
            freq = notes[idx]
            val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            env = 1.0 - ((t % 0.18) / 0.18) if idx < 3 else (1.0 - (t - 0.54) / 0.36)
            samples.append(int(val * max(0.0, env) * 16000))
        self.sounds['victory'] = self._make_sound(samples)

    def play(self, name):
        """Reproduz um som pelo nome se o áudio estiver disponível."""
        if not self.enabled:
            return
        snd = self.sounds.get(name)
        if snd:
            snd.play()
