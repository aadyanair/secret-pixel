# Secret Pixel

Secret Pixel is a Python-based steganography tool that hides secret text messages inside PNG images using **LSB (Least Significant Bit) encoding**.

It allows users to:
- hide a text message inside an image
- extract a hidden message from a stego image
- check how much message data an image can store
- validate whether a message fits before embedding it

---

## Features

- Hide secret messages inside RGB PNG images
- Extract hidden messages from modified images
- Capacity analysis before hiding
- Menu-driven CLI interface
- Basic error handling for invalid paths and empty messages

---

## Tech Stack

- **Python**
- **Pillow**

---

## Project Structure

```bash
SecretPixel/
│── main.py          # Menu-driven CLI
│── steg.py          # Core steganography logic
│── utils.py         # Binary conversion helpers
│── sample.png       # Sample image for testing
│── requirements.txt
│── README.md
│── .gitignore

## How it Works

Secret Pixel uses **LSB steganography**.

Every pixel in an RGB image has three values:

* Red
* Green
* Blue

The tool slightly changes the **last bit** of these values to store the secret message.
Since only the least significant bit is changed, the image looks visually the same to the human eye while still carrying hidden text data.

---

## Current Functionalities

### 1. Hide a Message

* Takes an input PNG image
* Takes a secret message from the user
* Creates a new output image with the hidden message

### 2. Extract a Message

* Reads a stego image
* Extracts the hidden text back from the image

### 3. Capacity Check

* Shows how many bits / approximate characters an image can store

### 4. Message Fit Analysis

* Compares required bits for the message with available bits in the image
* Prevents embedding if the message is too large

---

## Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the program

```bash
python main.py
```

---

## Example Menu

```text
===== Secret Pixel =====
1. Hide a message in an image
2. Extract a message from an image
3. Check image capacity
4. Exit
```

---

## Behind the Code

* Converts the secret text into binary
* Appends an end marker to detect where the message stops
* Stores message bits inside the least significant bits of image pixels
* Reads those bits back during extraction
* Uses capacity analysis to prevent oversized messages from being embedded

---

## Current Limitations

* Currently supports **text hiding only**
* Designed for **RGB PNG images**
* Does not yet support password protection or encryption
* Does not yet support audio or image tampering detection

---

## Future Improvements

* Password-protected secret messages
* Encrypted message embedding
* Support for more image formats
* Detection of suspicious / stego images
* GUI version of Secret Pixel

---

## Author

**Aadya Nair**
