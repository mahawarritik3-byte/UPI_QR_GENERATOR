import qrcode

upi_id = input("Enter your UPI ID: ")

name = "Recipient Name"
currency = "INR"
note = "Test Payment"

upi_url = f"upi://pay?pa={upi_id}&pn={name}&cu={currency}&tn={note}"

print(upi_url)

qr = qrcode.make(upi_url)

qr.save("upi_qr.png")

qr.show()

print("UPI QR Generated Successfully!")