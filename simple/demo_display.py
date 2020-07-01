# 128x32 display with hardware I2C:
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
from jetbot.utils.utils import get_ip_address
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=1, gpio=1) 
disp.begin()
print("ready")
disp.clear()
disp.display()
print("cleared")
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
font = ImageFont.load_default()
#draw.text((0,0), "eth0: " + str(get_ip_address('eth0')),  font=font, fill=255)
draw.text((0,8), "wlan0: " + str(get_ip_address('wlan0')), font=font, fill=255)
draw.text((0,16), "hallo", font=font, fill=255)
disp.image(image)
disp.display()
print("used")


