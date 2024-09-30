from PIL import Image
import numpy as np
import randomS


# Load the image
def load_image(test_image):
    img = Image.open(test_image)
    img = img.convert('RGB')  # Convert image to RGB if not already
    return np.array(img)


# Save the image
def save_image(image_array, save_path):
    img = Image.fromarray(image_array)
    img.save(save_path)


# Swap pixels at random locations
def swap_pixels(image_array, swap_count=1000):
    height, width, _ = image_array.shape
    for _ in range(swap_count):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)

        # Swap pixel values
        image_array[y1, x1], image_array[y2, x2] = image_array[y2, x2], image_array[y1, x1]
    return image_array


# Apply basic mathematical operations to each pixel
def apply_operation(image_array, operation="add", value=50):
    if operation == "add":
        image_array = np.clip(image_array + value, 0, 255)  # Add and clip pixel values to stay within [0, 255]
    elif operation == "subtract":
        image_array = np.clip(image_array - value, 0, 255)
    elif operation == "xor":
        image_array = image_array ^ value  # XOR operation
    return image_array


# Encrypt image using pixel manipulation
def encrypt_image(test_image, save_path, method="swap", value=50, swap_count=1000):
    img_array = load_image(test_image)

    if method == "swap":
        img_array = swap_pixels(img_array, swap_count)
    elif method in ["add", "subtract", "xor"]:
        img_array = apply_operation(img_array, method, value)

    save_image(img_array, save_path)


# Decrypt image (this is just reapplying the same operation)
def decrypt_image(test_image, save_path, method="swap", value=50, swap_count=1000):
    encrypt_image(test_image, save_path, method, value, swap_count)


# Example Usage
if __name__ == "__main__":
    # Encrypt image using pixel swapping
    encrypt_image("test_image.png", "encrypted_image.png", method="swap", swap_count=20000)

    # Decrypt image by swapping pixels again (same swap count)
    decrypt_image("encrypted_image.png", "decrypted_image.png", method="swap", swap_count=20000)

    # Encrypt image using addition
    encrypt_image("test_image.png", "encrypted_add_image.png", method="add", value=100)

    # Decrypt image using subtraction
    decrypt_image("encrypted_add_image.png", "decrypted_add_image.png", method="subtract", value=100)