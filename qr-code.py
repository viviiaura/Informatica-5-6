import qrcode

def main():
    song = "https://www.youtube.com/watch?v=c1ApWtP_GW4&list=RDc1ApWtP_GW4&start_radio=1"
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color="pink", back_color="white")
    img.save("youtube-qr.png")

if __name__ == "__main__":
    main()
