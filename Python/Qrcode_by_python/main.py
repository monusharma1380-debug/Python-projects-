import qrcode
qr = qrcode.QRCode()
data = input("Enter the data to be encoded in the QR code: ")
qr = qrcode.make(data)
qr_name = input("enter name for your Qr code : ")
qr.save(f"{qr_name}.png")
print(f"QR code generated and saved as '{qr_name}.png'")
