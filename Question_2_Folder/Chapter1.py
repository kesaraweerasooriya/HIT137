from PIL import Image
import time

# Step 1: Generate the number (integrating the code from your Random_number.py)
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

# Print the generated number
print("Generated number:", generated_number)

# Step 2: Modify the image using the generated number
# Load the image
img = Image.open("chapter1.jpg")

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
print("First 10 RGB values are: ", rgb_values[:10])  # Print the first 10 RGB values as an example

# Create a new blank image to store the modified pixel values
new_img = Image.new("RGB", (width, height))

# Modify the pixel values by adding the generated number 84

n = generated_number

for y in range(height):
    for x in range(width):
        r, g, b = rgb_img.getpixel((x, y))
        new_r = min(r + n, 255)
        new_g = min(g + n, 255)
        new_b = min(b + n, 255)
        new_img.putpixel((x, y), (new_r, new_g, new_b))

# Save the modified image
new_img.save("chapter1out.png")
print("Modified image saved as 'chapter1out.png'")

# Step 3: Sum up all the red (R) values in the modified image
total_red = 0
for y in range(height):
    for x in range(width):
        r, g, b = new_img.getpixel((x, y))
        total_red += r

# Output the total red sum
print("The sum of all red values in the modified image is:", total_red)

#This code generates a random number as given in the question and simultaneously adds that number with  the rgb values of the image
