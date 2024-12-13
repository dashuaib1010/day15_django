from PIL import Image, ImageDraw, ImageFont
import string
import random

class CaptchaGenerator:
    def __init__(self, width=250, height=60, font_size=48):
        """
        初始化验证码生成器。

        Args:
        - width (int): 图片宽度，默认为250像素。
        - height (int): 图片高度，默认为60像素。
        - font_size (int): 字体大小，默认为48像素。
        """
        self.width = width
        self.height = height
        self.font_size = font_size
        self.chars = string.ascii_letters + string.digits  # 验证码字符集合
        self.bgcolor = (255, 255, 255)  # 图片背景颜色
        self.linecolor = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))  # 干扰线颜色
        self.dotcolor = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))  # 干扰点颜色
        self.fontcolor = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))  # 字体颜色

    def generate_captcha(self):
        """
        生成验证码图片和文本。

        Returns:
        - image (PIL.Image.Image): 生成的验证码图片对象。
        - captcha_text (str): 生成的验证码文本。
        """
        captcha_text = ''.join(random.choice(self.chars) for _ in range(4))  # 随机生成验证码文本
        image = Image.new('RGB', (self.width, self.height), self.bgcolor)  # 创建RGB模式的空白图片
        draw = ImageDraw.Draw(image)  # 创建可在图像上绘图的对象

        font = ImageFont.load_default().font_variant(size=self.font_size)  # 加载默认字体并调整大小

        # 绘制干扰线
        for i in range(5):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line((x1, y1, x2, y2), fill=self.linecolor, width=3)

        # 绘制干扰点
        for i in range(200):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            draw.point((x, y), fill=self.dotcolor)

        # 绘制验证码文字，包括阴影效果
        for i, char in enumerate(captcha_text):
            shadow_offset = random.randint(0, 3)
            shadow_color = (0, 0, 0)
            draw.text((20 + i * 50 + shadow_offset, 5 + shadow_offset), char, font=font, fill=shadow_color)  # 绘制阴影效果的文字
            draw.text((20 + i * 50, 5), char, font=font, fill=self.fontcolor)  # 绘制文字

        return image, captcha_text



if __name__ == '__main__':
    c = CaptchaGenerator()
    a ,b = c.generate_captcha()
    print(a,b)