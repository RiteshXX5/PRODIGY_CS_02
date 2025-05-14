from PIL import Image  #import the pillow to handle image

# function to encrypt the image

def encrypt_image(img_path, key):
    img = Image.open(img_path)
    pixels = img.load ()
    width, height = img.size

    for x in range(width):        #loop through every pixel
        for y in range(height):
            r, g,b = pixels[x,y]  #get the red, green, blue value
         
            r=(r + key) % 256     #encrypt each color by adding key
            g=(g + key) % 256
            b=(b + key) % 256
            pixels[x,y]=(r, g, b) #setting new pixel value
    
    #save the encrypted image

    img.save("encrypted_image.png")
    print("Image Encrypted and saved as 'encrypted_image.png'")
def decrypt_image(img_path, key):
    img = Image.open(img_path).convert('RGB')  # Convert to RGB to avoid pixel issues
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    img.save("decrypted_image.png")
    print("Image Decrypted and saved as 'decrypted_image.png'.")

#main function that control program

def main():
    print("Image Encryption and Decryption Tool")

    choice = input ("Do you want to (E)encrypt or (D)decrypt: ").upper()
    image_path = input(" enter image filename with extension, e.g., photo.png : ")
    print("opening image at: {image_path}")
    try:
      key = int(input("Enter the key between 0-255 : "))
    except:
      print ("Invalid key !")
      return

    #call the function based on user choice
    if choice == "E":
        encrypt_image(image_path, key)
    elif choice == "D":
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()


