from PIL import Image

tolerance=20

def is_color_close(rgb1, rgb2):
    global tolerance
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return (
        abs(r1 - r2) <= tolerance and
        abs(g1 - g2) <= tolerance and
        abs(b1 - b2) <= tolerance
    )

def filter_image(input_image_path, output_image_path, target_color_rgb):
    # Open the input image
    image = Image.open(input_image_path)

    # Create a new image with the same dimensions and a white background
    filtered_image = Image.new("RGB", image.size, (255, 255, 255))

    # Get the width and height of the image
    width, height = image.size

    # Iterate through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB color of the current pixel
            pixel_color = image.getpixel((x, y))
            #print(pixel_color)

            # Check if the current pixel's color matches the target color
            if is_color_close(pixel_color, target_color_rgb):
                # If it matches, set the pixel in the filtered image to the same color
                filtered_image.putpixel((x, y), pixel_color)

    # Save the filtered image to the specified output path
    filtered_image.save(output_image_path)

if __name__ == "__main__":
    #input_image_path = "parque omega - copia.jpg"  # Replace with the path to your input image
    input_image_path = "test.jpg"
    output_image_path = "result2.jpg"  # Replace with the desired output path
    target_color_rgb = (162, 215, 229)  # Replace with the RGB color you want to preserve

    filter_image(input_image_path, output_image_path, target_color_rgb)
    print("\n\n END OF LINE \n\n")
