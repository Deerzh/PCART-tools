from PIL import ImageFont
font = ImageFont.load_default()
text = 'Hello, Pillow!'
mask = font.getmask(text, mode='1', start=None)