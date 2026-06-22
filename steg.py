from PIL import Image
from utils import text_to_binary, encrypt_message, decrypt_message

END_MARKER = "#####"
ENC_PREFIX = "ENC::"


def get_image_capacity(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size

        total_bits = width * height * 3
        total_chars = total_bits // 8

        return total_bits, total_chars

    except FileNotFoundError:
        print("Error: Image file not found.")
        return None, None
    except Exception as e:
        print("Error reading image:", e)
        return None, None


def analyze_message_capacity(image_path, secret_message):
    total_bits, total_chars = get_image_capacity(image_path)

    if total_bits is None:
        return None

    full_message = secret_message + END_MARKER
    binary_message = text_to_binary(full_message)
    required_bits = len(binary_message)

    return {
        "available_bits": total_bits,
        "available_chars": total_chars,
        "required_bits": required_bits,
        "required_chars": len(full_message),
        "fits": required_bits <= total_bits
    }


def hide_message(image_path, secret_message, output_path, password=None):
    if not secret_message:
        print("Error: Secret message cannot be empty.")
        return

    try:
        img = Image.open(image_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        # Encrypt message if password is provided
        if password:
            secret_message = ENC_PREFIX + encrypt_message(secret_message, password)

        full_message = secret_message + END_MARKER
        binary_message = text_to_binary(full_message)

        pixels = list(img.getdata())
        new_pixels = []

        data_index = 0
        message_length = len(binary_message)

        max_bits = len(pixels) * 3
        if message_length > max_bits:
            print("Error: Message is too long for this image.")
            return

        for pixel in pixels:
            r, g, b = pixel

            if data_index < message_length:
                r = (r & 254) | int(binary_message[data_index])
                data_index += 1

            if data_index < message_length:
                g = (g & 254) | int(binary_message[data_index])
                data_index += 1

            if data_index < message_length:
                b = (b & 254) | int(binary_message[data_index])
                data_index += 1

            new_pixels.append((r, g, b))

        img.putdata(new_pixels)
        img.save(output_path)
        print(f"Success: Message hidden in '{output_path}'")

    except FileNotFoundError:
        print("Error: Input image file not found.")
    except Exception as e:
        print("Error hiding message:", e)


def extract_message(image_path, password=None):
    try:
        img = Image.open(image_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        pixels = list(img.getdata())
        binary_data = ""

        for pixel in pixels:
            r, g, b = pixel
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

        extracted_text = ""

        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]

            if len(byte) < 8:
                break

            extracted_text += chr(int(byte, 2))

            if extracted_text.endswith(END_MARKER):
                extracted_text = extracted_text[:-len(END_MARKER)]

                # Check if encrypted
                if extracted_text.startswith(ENC_PREFIX):
                    encrypted_payload = extracted_text[len(ENC_PREFIX):]

                    if not password:
                        return "This message is password-protected. Please provide a password."

                    decrypted = decrypt_message(encrypted_payload, password)
                    if decrypted is None:
                        return "Wrong password or corrupted message."

                    return decrypted

                return extracted_text

        return "No hidden message found."

    except FileNotFoundError:
        return "Error: Image file not found."
    except Exception as e:
        return f"Error extracting message: {e}"