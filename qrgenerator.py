#QR Code generator

import qrcode as qr

img = qr.make("www.linkedin.com/in/pankajkumarbais")

img.save('linkedin.png') 
 
print('Qr code generated and Saved in the gallery')
