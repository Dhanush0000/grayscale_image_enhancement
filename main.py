import os
import cv2
from scipy import ndimage

# Path to the input image
input_image_path = "File_Path"
# Path to save the output image
output_image_path = "Results.jpg"

# Create RESULTS directory if it doesn't exist
os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

def enhanceImage(image_path, output_path):
    try:
        image = cv2.imread(image_path)
        if image is not None:
            # Convert image to gray scale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Non-Linear filter for noise removal
            deNoised = ndimage.median_filter(gray_image, 3)

            # Histogram Equalizer
            # High pass filter for improving the contrast of the image
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            highPass = clahe.apply(deNoised)

            # Gamma Transformation
            # Prevent bleaching or darkening of images
            gamma = highPass / 255.0
            gammaFilter = cv2.pow(gamma, 1.5)
            gammaFilter = gammaFilter * 255

            cv2.imwrite(output_path, gammaFilter)
            print(f'Image saved to {output_path}')
        else:
            print('Error: Image not found')
    except Exception as e:
        print(f'Error processing image: {e}')

print("--------IMAGE ENHANCEMENT TECHNIQUE----------")
print("---------------------------------------------")
print("--------INITIALIZED IMAGE PROCESSING---------")
# Enhance Image Quality
enhanceImage(image_path=input_image_path, output_path=output_image_path)
print("--------IMAGE PROCESSING COMPLETED-----------")
