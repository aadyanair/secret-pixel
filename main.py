from steg import hide_message, extract_message, get_image_capacity, analyze_message_capacity


def show_menu():
    print("\n===== Secret Pixel =====")
    print("1. Hide a message in an image")
    print("2. Extract a message from an image")
    print("3. Check image capacity")
    print("4. Exit")


def hide_flow():
    image_path = input("Enter path of the input image: ").strip()
    secret_message = input("Enter the secret message: ").strip()
    output_path = input("Enter output image name (example: secret_output.png): ").strip()

    if not output_path:
        print("Error: Output file name cannot be empty.")
        return

    if not secret_message:
        print("Error: Secret message cannot be empty.")
        return

    analysis = analyze_message_capacity(image_path, secret_message)

    if analysis is None:
        return

    print("\n--- Capacity Analysis ---")
    print("Available bits in image:", analysis["available_bits"])
    print("Approx max characters in image:", analysis["available_chars"])
    print("Required bits for your message:", analysis["required_bits"])
    print("Characters in your message (+ marker):", analysis["required_chars"])

    if not analysis["fits"]:
        print("Error: Message is too large for this image.")
        return

    print("Status: Message fits. Proceeding to hide it...\n")
    hide_message(image_path, secret_message, output_path)


def extract_flow():
    image_path = input("Enter path of the image to extract from: ").strip()
    if not image_path:
        print("Error: Image path cannot be empty.")
        return

    message = extract_message(image_path)
    print("Recovered Message:", message)


def capacity_flow():
    image_path = input("Enter path of the image: ").strip()
    if not image_path:
        print("Error: Image path cannot be empty.")
        return

    total_bits, total_chars = get_image_capacity(image_path)

    if total_bits is not None:
        print("Total bits available:", total_bits)
        print("Approx max characters:", total_chars)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            hide_flow()
        elif choice == "2":
            extract_flow()
        elif choice == "3":
            capacity_flow()
        elif choice == "4":
            print("Exiting Secret Pixel. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()