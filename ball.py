from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None  # 모든 공이 같은 이미지를 쓰므로 한 번만 불러온다

    def __init__(self, x, y, velocity):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.velocity = velocity  # 한 프레임에 움직이는 거리, 부호가 방향

    def update(self):
        self.x += self.velocity
        # 화면 밖으로 나가면 월드에서 지운다
        if self.x < -10 or self.x > get_canvas_width() + 10:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
