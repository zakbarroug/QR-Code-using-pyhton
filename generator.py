import tkinter as tk
import qrcode

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        self.label = tk.Label(self.master, text="Enter URL:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.button = tk.Button(self.master, text="Generate QR Code", command=self.generate_qr)
        self.button.pack()

        self.qr_label = tk.Label(self.master)

    def generate_qr(self):
        url = self.entry.get()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((250, 250))
        photo = tk.PhotoImage(master=self.master, data=img.tobytes())
        self.qr_label.config(image=photo)
        self.qr_label.image = photo
        self.qr_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
