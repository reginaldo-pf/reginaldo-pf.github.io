"""
player.py - Implementação completa do protagonista Mega Man X.
Inclui física fiel ao SNES: corrida, pulo variável, Dash, Dash Jump,
Wall Slide, Wall Jump, carregamento do Mega Buster (3 níveis) e sistema de dano.
"""

import pygame
from .settings import (
    PLAYER_SPEED, PLAYER_DASH_SPEED, PLAYER_DASH_DURATION, PLAYER_DASH_COOLDOWN,
    PLAYER_GRAVITY, PLAYER_MAX_FALL_SPEED, PLAYER_JUMP_FORCE, PLAYER_JUMP_CUTOFF,
    PLAYER_WALL_SLIDE_SPEED, PLAYER_WALL_JUMP_X, PLAYER_WALL_JUMP_Y,
    PLAYER_WALL_JUMP_LOCK, PLAYER_MAX_HP, PLAYER_INVINCIBILITY_TIME,
    CHARGE_LEVEL_1_TIME, CHARGE_LEVEL_2_TIME,
    KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, KEY_JUMP, KEY_SHOOT, KEY_DASH
)
from .sprites import SpriteFactory
from .audio import SoundManager
from .bullet import BusterBullet

def _is_key_down(keys, key_tuple):
    for k in key_tuple:
        try:
            if keys[k]:
                return True
        except (KeyError, IndexError, TypeError):
            pass
    return False

class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.vx = 0.0
        self.vy = 0.0

        # Caixa de colisão (Hitbox ajustada para jogabilidade precisa)
        self.width = 20
        self.height = 32
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)

        # Estado e Direção
        self.facing_right = True
        self.on_ground = False
        self.is_dashing = False
        self.dash_jumping = False
        self.is_wall_sliding = False
        self.wall_dir = 0  # -1 para parede à esquerda, +1 à direita
        self.dash_timer = 0.0
        self.dash_cooldown = 0.0
        self.wall_jump_lock = 0.0

        # Animação
        self.state = "idle"
        self.anim_timer = 0.0
        self.anim_frame = 0
        self.shoot_anim_timer = 0.0
        self.ghost_timer = 0.0

        # Sistema de Tiro e Carga
        self.charge_time = 0.0
        self.is_charging = False
        self.charge_level = 0
        self.bullets = []

        # Vida e Dano
        self.hp = PLAYER_MAX_HP
        self.max_hp = PLAYER_MAX_HP
        self.invincible_timer = 0.0
        self.hurt_lock_timer = 0.0

        self.audio = SoundManager.get()
        self.sprites = SpriteFactory.get().player_sprites

    def handle_input(self, keys_pressed, just_pressed_keys, just_released_keys, camera):
        """Processa as entradas do teclado."""
        # Se estiver em recuperação de dano grave, o controle fica travado
        if self.hurt_lock_timer > 0:
            return

        # 1. Movimento Horizontal (se não estiver travado por Wall Jump)
        move_x = 0
        if _is_key_down(keys_pressed, KEY_LEFT):
            move_x -= 1
        if _is_key_down(keys_pressed, KEY_RIGHT):
            move_x += 1

        if self.wall_jump_lock <= 0:
            if move_x != 0:
                self.facing_right = (move_x > 0)
                speed = PLAYER_DASH_SPEED if (self.is_dashing or self.dash_jumping) else PLAYER_SPEED
                self.vx = move_x * speed
            else:
                if not (self.is_dashing and self.on_ground):
                    self.vx = 0.0

        # 2. Dash (Investida veloz)
        if any(k in just_pressed_keys for k in KEY_DASH):
            if self.on_ground and not self.is_dashing and self.dash_cooldown <= 0:
                self.is_dashing = True
                self.dash_timer = PLAYER_DASH_DURATION
                self.dash_cooldown = PLAYER_DASH_COOLDOWN
                direction = 1 if self.facing_right else -1
                self.vx = direction * PLAYER_DASH_SPEED
                self.audio.play('dash')

        # 3. Pulo e Wall Jump
        if any(k in just_pressed_keys for k in KEY_JUMP):
            if self.is_wall_sliding:
                # Kick na parede oposta (Wall Kick)
                self.vy = PLAYER_WALL_JUMP_Y
                self.vx = -self.wall_dir * PLAYER_WALL_JUMP_X
                self.facing_right = (self.wall_dir < 0)
                self.wall_jump_lock = PLAYER_WALL_JUMP_LOCK
                self.is_wall_sliding = False
                self.dash_jumping = False
                self.audio.play('wall_kick')
            elif self.on_ground:
                # Pulo normal do chão ou Dash Jump!
                self.vy = PLAYER_JUMP_FORCE
                self.on_ground = False
                if self.is_dashing:
                    self.dash_jumping = True  # Mantém a velocidade do dash no ar!
                    self.is_dashing = False
                self.audio.play('jump')

        # Corte do Pulo Variável (soltar a tecla corta o impulso)
        if any(k in just_released_keys for k in KEY_JUMP):
            if self.vy < PLAYER_JUMP_CUTOFF:
                self.vy = PLAYER_JUMP_CUTOFF

        # 4. Mega Buster (Disparo e Carregamento)
        shoot_held = _is_key_down(keys_pressed, KEY_SHOOT)
        shoot_pressed = any(k in just_pressed_keys for k in KEY_SHOOT)
        shoot_released = any(k in just_released_keys for k in KEY_SHOOT)

        if shoot_pressed:
            # Tiro rápido imediato se não estava carregando
            if self.charge_time < CHARGE_LEVEL_1_TIME:
                self._fire_bullet(0, camera)

        if shoot_held:
            self.is_charging = True
        else:
            if self.is_charging and shoot_released:
                # Soltou o botão de tiro: verifica se atira carga
                if self.charge_time >= CHARGE_LEVEL_2_TIME:
                    self._fire_bullet(2, camera)
                elif self.charge_time >= CHARGE_LEVEL_1_TIME:
                    self._fire_bullet(1, camera)
            self.is_charging = False
            self.charge_time = 0.0

    def _fire_bullet(self, level, camera):
        """Instancia um projétil do Buster."""
        # Limite de até 3 tiros comuns simultâneos na tela
        player_bullets = [b for b in self.bullets if b.alive]
        if level == 0 and len(player_bullets) >= 3:
            return

        direction = 1 if self.facing_right else -1
        bx = self.rect.centerx + (direction * 16)
        by = self.rect.centery - 2 if not self.is_dashing else self.rect.centery + 4

        bullet = BusterBullet(bx, by, direction, charge_level=level)
        self.bullets.append(bullet)
        self.shoot_anim_timer = 0.22  # Ativa postura com o braço buster

        if level == 2:
            self.audio.play('charge_2_shot')
            camera.add_shake(0.2, 3.5)
        elif level == 1:
            self.audio.play('charge_1_shot')
        else:
            self.audio.play('shoot')

    def update(self, dt, tiles, particle_system, camera):
        """Atualiza a física, colisões com o cenário e temporizadores."""
        # Atualiza temporizadores
        if self.dash_cooldown > 0:
            self.dash_cooldown -= dt
        if self.wall_jump_lock > 0:
            self.wall_jump_lock -= dt
        if self.invincible_timer > 0:
            self.invincible_timer -= dt
        if self.hurt_lock_timer > 0:
            self.hurt_lock_timer -= dt
        if self.shoot_anim_timer > 0:
            self.shoot_anim_timer -= dt

        # Carregamento do Buster
        if self.is_charging:
            self.charge_time += dt
            if self.charge_time >= CHARGE_LEVEL_2_TIME:
                self.charge_level = 2
            elif self.charge_time >= CHARGE_LEVEL_1_TIME:
                self.charge_level = 1
            else:
                self.charge_level = 0

            # Efeito visual de partículas de carga
            if self.charge_level > 0:
                particle_system.add_charge_particles(self.rect.center, self.charge_level)
        else:
            self.charge_level = 0

        # Atualiza Dash
        if self.is_dashing:
            self.dash_timer -= dt
            self.ghost_timer += dt
            if self.ghost_timer >= 0.04:
                self.ghost_timer = 0.0
                curr_sprite = self._get_current_frame()
                particle_system.add_ghost(curr_sprite, self.rect.x - 6, self.rect.y - 2, self.facing_right)
            particle_system.add_dash_dust(self.rect.centerx, self.rect.bottom, 1 if self.facing_right else -1)
            if self.dash_timer <= 0:
                self.is_dashing = False

        # Aplica Gravidade
        if not self.is_wall_sliding:
            self.vy += PLAYER_GRAVITY * dt
            if self.vy > PLAYER_MAX_FALL_SPEED:
                self.vy = PLAYER_MAX_FALL_SPEED
        else:
            # Ao deslizar na parede, a queda é desacelerada
            self.vy = PLAYER_WALL_SLIDE_SPEED
            particle_system.add_wall_slide_sparks(
                self.rect.left if self.wall_dir < 0 else self.rect.right,
                self.rect.centery,
                self.wall_dir
            )

        # ---------------------------------------------------------
        # MOVIMENTO E COLISÃO EM EIXOS SEPARADOS (X e Y)
        # ---------------------------------------------------------
        # 1. Eixo X
        self.x += self.vx * dt
        self.rect.x = int(self.x)

        wall_collision_left = False
        wall_collision_right = False

        for tile in tiles:
            if tile.solid and self.rect.colliderect(tile.rect):
                if self.vx > 0:
                    self.rect.right = tile.rect.left
                    self.x = self.rect.x
                    wall_collision_right = True
                    if self.is_dashing:
                        self.is_dashing = False
                elif self.vx < 0:
                    self.rect.left = tile.rect.right
                    self.x = self.rect.x
                    wall_collision_left = True
                    if self.is_dashing:
                        self.is_dashing = False

        # 2. Eixo Y
        self.y += self.vy * dt
        self.rect.y = int(self.y)
        was_on_ground = self.on_ground
        self.on_ground = False

        for tile in tiles:
            if tile.solid and self.rect.colliderect(tile.rect):
                if self.vy > 0:
                    self.rect.bottom = tile.rect.top
                    self.y = self.rect.y
                    self.vy = 0.0
                    self.on_ground = True
                    self.dash_jumping = False  # Encerra o dash jump ao pousar
                elif self.vy < 0:
                    self.rect.top = tile.rect.bottom
                    self.y = self.rect.y
                    self.vy = 0.0

        # Lógica de Wall Slide
        # Ocorre se o jogador estiver no ar, caindo e colidindo com a parede na direção que está olhando
        self.is_wall_sliding = False
        self.wall_dir = 0

        if not self.on_ground and self.vy > 0:
            keys = pygame.key.get_pressed()
            pressing_left = _is_key_down(keys, KEY_LEFT)
            pressing_right = _is_key_down(keys, KEY_RIGHT)

            # Checa contato com parede lateral
            test_rect_left = self.rect.move(-2, 0)
            test_rect_right = self.rect.move(2, 0)

            touching_left = any(tile.solid and test_rect_left.colliderect(tile.rect) for tile in tiles)
            touching_right = any(tile.solid and test_rect_right.colliderect(tile.rect) for tile in tiles)

            if touching_left and (pressing_left or not self.facing_right):
                self.is_wall_sliding = True
                self.wall_dir = -1
                self.facing_right = False
            elif touching_right and (pressing_right or self.facing_right):
                self.is_wall_sliding = True
                self.wall_dir = 1
                self.facing_right = True

        # Atualiza Projéteis do Jogador
        for b in self.bullets:
            b.update(dt, tiles)
        self.bullets = [b for b in self.bullets if b.alive]

        # Atualiza Animações
        self._update_animation(dt)

    def _update_animation(self, dt):
        """Seleciona a animação adequada conforme o estado físico."""
        self.anim_timer += dt

        if self.is_wall_sliding:
            self.state = "wall_slide"
        elif self.is_dashing:
            self.state = "dash"
        elif not self.on_ground:
            self.state = "jump" if self.vy < 0 else "fall"
        elif abs(self.vx) > 10:
            self.state = "run"
            if self.anim_timer >= 0.10:
                self.anim_timer = 0.0
                self.anim_frame = (self.anim_frame + 1) % 4
        else:
            self.state = "idle"
            if self.anim_timer >= 0.60:
                self.anim_timer = 0.0
                self.anim_frame = (self.anim_frame + 1) % 2

    def _get_current_frame(self):
        """Retorna a superfície correspondente ao estado atual."""
        is_shooting = (self.shoot_anim_timer > 0)

        if self.state == "wall_slide":
            surf = self.sprites["wall_slide"]
        elif self.state == "dash":
            surf = self.sprites["dash_shoot"] if is_shooting else self.sprites["dash"]
        elif self.state == "jump":
            surf = self.sprites["jump_shoot"] if is_shooting else self.sprites["jump"]
        elif self.state == "fall":
            surf = self.sprites["jump_shoot"] if is_shooting else self.sprites["fall"]
        elif self.state == "run":
            frames = self.sprites["run_shoot"] if is_shooting else self.sprites["run"]
            surf = frames[self.anim_frame % len(frames)]
        else: # idle
            if is_shooting:
                surf = self.sprites["idle_shoot"]
            else:
                surf = self.sprites["idle"][self.anim_frame % 2]

        if not self.facing_right:
            surf = pygame.transform.flip(surf, True, False)

        return surf

    def take_damage(self, amount, knockback_dir=0, camera=None):
        """Aplica dano ao jogador e ativa tempo de invencibilidade."""
        if self.invincible_timer > 0 or self.hp <= 0:
            return False

        self.hp = max(0, self.hp - amount)
        self.invincible_timer = PLAYER_INVINCIBILITY_TIME
        self.hurt_lock_timer = 0.22
        self.is_dashing = False
        self.dash_jumping = False
        self.is_wall_sliding = False

        # Impulso de recuo (Knockback)
        kb_dir = knockback_dir if knockback_dir != 0 else (-1 if self.facing_right else 1)
        self.vx = kb_dir * 130.0
        self.vy = -180.0
        self.on_ground = False

        self.audio.play('hurt')
        if camera:
            camera.add_shake(0.25, 4.0)
        return True

    def heal(self, amount):
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        if self.hp > old_hp:
            self.audio.play('pickup')

    def draw(self, surface, camera_offset):
        """Renderiza o X com efeito de piscada quando invencível e auras de carga."""
        # Efeito de piscar quando invulnerável (a cada 0.08 segundos)
        if self.invincible_timer > 0 and int(self.invincible_timer * 20) % 2 == 0:
            # Não desenha neste frame para dar o efeito de transparência piscante
            pass
        else:
            sprite = self._get_current_frame()
            px = self.rect.x - 6 - camera_offset[0]
            py = self.rect.y - 2 - camera_offset[1]
            surface.blit(sprite, (px, py))

        # Desenha projéteis disparados pelo jogador
        for b in self.bullets:
            b.draw(surface, camera_offset)
