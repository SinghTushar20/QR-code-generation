import qrcode as qr
s = input("Paste a valid Link")
img = qr.make(s)
img.save("Barcode.png")
