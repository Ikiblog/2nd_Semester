import tkinter as tk

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def calculate_total(self):
        total = 0
        for item, quantity in self.items:
            total += item.price * quantity
        return total

    def print_receipt(self):
        receipt = "Struk Belanja:\n"
        items_dict = {}
        for item, quantity in self.items:
            if item.name not in items_dict:
                items_dict[item.name] = {"harga": item.price, "jumlah": quantity}
            else:
                items_dict[item.name]["jumlah"] += quantity

        for item_name, item_info in items_dict.items():
            receipt += f"{item_name}: Rp {item_info['harga']:,.2f} x {item_info['jumlah']}\n"

        receipt += f"Total: Rp {self.calculate_total():,.2f}"
        return receipt

def add_to_order(item_name, quantity):
    global order
    if item_name in menu:
        order.add_item(Item(item_name, menu[item_name]), quantity)
        update_receipt_text()

def update_receipt_text():
    receipt_text.delete(1.0, tk.END)
    receipt_text.insert(tk.END, order.print_receipt())

def process_payment():
    try:
        amount_paid = float(entry_payment.get())
        total_amount = order.calculate_total()
        change = amount_paid - total_amount
        receipt_text.insert(tk.END, f"\nUang Pembeli: Rp {amount_paid:,.2f}\n")
        receipt_text.insert(tk.END, f"Kembalian: Rp {change:,.2f}")
    except ValueError:
        receipt_text.insert(tk.END, "Jumlah pembayaran tidak valid.")

def main():
    global menu, order, receipt_text, entry_payment

    menu = {
        "Oli Mesin": 20000.00,
        "Busi": 5000.00,
        "Kampas Rem": 25000.00,
        "Rantai": 30000.00,
        "Filter Udara": 10000.00,
        # Tambahkan item lain jika diperlukan
    }

    root = tk.Tk()
    root.title("Toko Suku Cadang Motor")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    order = Order()

    label_menu = tk.Label(frame, text="Menu:")
    label_menu.grid(row=0, column=0, sticky="w")

    for i, (item, price) in enumerate(menu.items(), start=1):
        label_item = tk.Label(frame, text=f"{item}: Rp {price:,.2f}")
        label_item.grid(row=i, column=0, sticky="w")

        entry_quantity = tk.Entry(frame, width=5)
        entry_quantity.grid(row=i, column=1)

        btn_add = tk.Button(frame, text="Tambah", command=lambda item=item, entry=entry_quantity: add_to_order(item, int(entry.get())))
        btn_add.grid(row=i, column=2, padx=5)

    label_payment = tk.Label(frame, text="Jumlah Pembayaran (Rp):")
    label_payment.grid(row=len(menu)+2, column=0, sticky="w")

    entry_payment = tk.Entry(frame, width=10)
    entry_payment.grid(row=len(menu)+2, column=1)

    btn_pay = tk.Button(frame, text="Proses Pembayaran", command=process_payment)
    btn_pay.grid(row=len(menu)+2, column=2, padx=5)

    label_receipt = tk.Label(frame, text="Struk:")
    label_receipt.grid(row=len(menu)+3, column=0, sticky="w")

    receipt_text = tk.Text(frame, width=30, height=10)
    receipt_text.grid(row=len(menu)+4, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()
