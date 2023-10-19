import qrcode

# Your text or data for the QR code
data = "https://docs.google.com/forms/d/e/1FAIpQLScsTY64rtqgz2qa9zgTH1Gc2s9V4eCoX5xPZHcR8tcgFzIJmg/viewform"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create a PIL image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image
img.save("my_qr_code.png")

# Optionally, display the QR code
img.show()
