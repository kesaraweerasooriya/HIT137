from PIL import Image

# Load the image
image_path = "chapter1out.png"  # Replace with your image path
img = Image.open("chapter1out.png")

# Convert the image to RGB mode (if it's not already in RGB)
rgb_img = img.convert("RGB")

# Get the size of the image
width, height = rgb_img.size

# Initialize a list to store the RGB values
rgb_values = []

# Loop through every pixel in the image
for y in range(height):
    for x in range(width):
        r, g, b = rgb_img.getpixel((x, y))
        rgb_values.append((r, g, b))

# Display the first few RGB values
print(rgb_values[:10])  # Print the first 10 RGB values as an example
