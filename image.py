# Import the Image class from Pillow
from PIL import Image
# Open an image file from the current directory
img = Image.open("example.jpg")
# Print the image format, size, and mode
print(img.format, img.size, img.mode)
# Show the image using the default image viewer
img.show()
