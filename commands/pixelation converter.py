import cv2
import numpy as np
from tkinter import Tk, filedialog, simpledialog
from pathlib import Path

def pixelate_image():
    # Prompt the user to select an image file
    Tk().withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )

    if not file_path:
        print("No file selected. Exiting.")
        return

    # Ask the user how many pixels (resolution) they want
    pixel_count = simpledialog.askinteger(
        "Pixelation Level",
        "Enter the number of pixels (e.g., 50 for 50x50 resolution):",
        minvalue=1,
        maxvalue=1000
    )

    if not pixel_count:
        print("No resolution entered. Exiting.")
        return

    # Read the image with alpha channel support
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        print("Failed to load image. Exiting.")
        return

    # Separate the alpha channel if it exists
    if image.shape[2] == 4:  # If the image has an alpha channel
        bgr = image[:, :, :3]  # Extract BGR channels
        alpha = image[:, :, 3]  # Extract alpha channel
    else:
        bgr = image
        alpha = None

    # Get the original dimensions of the image
    original_height, original_width = bgr.shape[:2]

    # Resize the image to the desired pixelation level
    pixelated_bgr = cv2.resize(bgr, (pixel_count, pixel_count), interpolation=cv2.INTER_LINEAR)

    # Scale it back to the original dimensions
    pixelated_bgr = cv2.resize(pixelated_bgr, (original_width, original_height), interpolation=cv2.INTER_NEAREST)

    if alpha is not None:
        # Process the alpha channel similarly
        pixelated_alpha = cv2.resize(alpha, (pixel_count, pixel_count), interpolation=cv2.INTER_LINEAR)
        pixelated_alpha = cv2.resize(pixelated_alpha, (original_width, original_height), interpolation=cv2.INTER_NEAREST)
        
        # Merge the pixelated BGR and alpha channels
        pixelated_image = np.dstack((pixelated_bgr, pixelated_alpha))
    else:
        pixelated_image = pixelated_bgr

    # Save the result
    output_path = Path(file_path).with_name(f"pixelated_{pixel_count}x{pixel_count}.png")
    cv2.imwrite(str(output_path), pixelated_image)

    print(f"Pixelated image saved to: {output_path}")
    cv2.imshow("Pixelated Image", pixelated_bgr if alpha is None else pixelated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    pixelate_image()
