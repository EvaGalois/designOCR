# # import cairosvg
# from PIL import Image
# # cairosvg.svg2png(url='obsidian-logo-gradient.svg', write_to='output.png')
# png_image = Image.open('icon.png')
# png_image.save('icon.ico', format='ICO')
# png_image.close()

from PIL import Image
png_image = Image.open('icon.png')
ico_image = Image.new('RGBA', (png_image.width, png_image.height))
ico_image.paste(png_image, (0, 0))
# ico_image.save('icon.ico', format='ICO')
ico_image.save('icon.ico', format='ICO', sizes=[(64, 64)])

