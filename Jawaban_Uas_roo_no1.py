import tkinter as tk
from tkinter import messagebox

class AplikasiHotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel SEJUK ASRI")
        
        # Bidang Input
        self.label_petugas = tk.Label(root, text="Nama Petugas:")
        self.entry_petugas = tk.Entry(root)
        self.label_pelanggan = tk.Label(root, text="Nama Pelanggan:")
        self.entry_pelanggan = tk.Entry(root)
        self.label_checkin = tk.Label(root, text="Tanggal Check-in:")
        self.entry_checkin = tk.Entry(root)
        self.label_kode_kamar = tk.Label(root, text="Kode Kamar (M/S/L/A):")
        self.entry_kode_kamar = tk.Entry(root)
        self.label_lama_sewa = tk.Label(root, text="Lama Sewa:")
        self.entry_lama_sewa = tk.Entry(root)
        self.label_uang_bayar = tk.Label(root, text="Uang Bayar:")
        self.entry_uang_bayar = tk.Entry(root)
        
        # Penempatan
        self.label_petugas.grid(row=0, column=0)
        self.entry_petugas.grid(row=0, column=1)
        self.label_pelanggan.grid(row=1, column=0)
        self.entry_pelanggan.grid(row=1, column=1)
        self.label_checkin.grid(row=2, column=0)
        self.entry_checkin.grid(row=2, column=1)
        self.label_kode_kamar.grid(row=3, column=0)
        self.entry_kode_kamar.grid(row=3, column=1)
        self.label_lama_sewa.grid(row=4, column=0)
        self.entry_lama_sewa.grid(row=4, column=1)
        self.label_uang_bayar.grid(row=5, column=0)
        self.entry_uang_bayar.grid(row=5, column=1)
        
        # Tombol Hitung
        self.button_hitung = tk.Button(root, text="Hitung Total Bayar", command=self.hitung_bayar)
        self.button_hitung.grid(row=6, columnspan=2)
        
    def hitung_bayar(self):
        nama_petugas = self.entry_petugas.get()
        nama_pelanggan = self.entry_pelanggan.get()
        tanggal_checkin = self.entry_checkin.get()
        kode_kamar = self.entry_kode_kamar.get().upper()
        lama_sewa = int(self.entry_lama_sewa.get())
        uang_bayar = int(self.entry_uang_bayar.get())
        
        harga_kamar = {
            'M': 650000,
            'S': 550000,
            'L': 400000,
            'A': 350000
        }
        
        if kode_kamar in harga_kamar:
            harga_permalam = harga_kamar[kode_kamar]
            nama_kamar = {
                'M': 'Melati',
                'S': 'Sakura',
                'L': 'Lily',
                'A': 'Anggrek'
            }[kode_kamar]
            
            jumlah_bayar = harga_permalam * lama_sewa
            
            if lama_sewa > 5:
                diskon = 0.10
            elif lama_sewa > 3:
                diskon = 0.05
            else:
                diskon = 0.0
            
            ppn = diskon * jumlah_bayar
            total_bayar = jumlah_bayar - ppn
            uang_kembali = uang_bayar - total_bayar
            
            messagebox.showinfo("Bukti Pemesanan Kamar", 
                f"Nama Petugas: {nama_petugas}\n"
                f"Nama Pelanggan: {nama_pelanggan}\n"
                f"Tanggal Check-in: {tanggal_checkin}\n"
                f"Nama Kamar: {nama_kamar}\n"
                f"Harga Sewa per Malam: Rp {harga_permalam:,}\n"
                f"Lama Sewa: {lama_sewa} malam\n"
                f"PPN: Rp {ppn:,}\n"
                f"Jumlah Bayar: Rp {jumlah_bayar:,}\n"
                f"Total Bayar: Rp {total_bayar:,}\n"
                f"Uang Kembali: Rp {uang_kembali:,}"
            )
        else:
            messagebox.showerror("Error", "Kode kamar tidak valid!")

root = tk.Tk()
app = AplikasiHotel(root)
root.mainloop()
