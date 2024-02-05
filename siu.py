import tkinter as tk
from tkinter import ttk
import requests
import json

url = "https://v6.exchangerate-api.com/v6/beb0a03931457ddfd5f1ad73/latest/PKR"

try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an HTTPError for bad requests
    currency_dict = {}

    exchange_data = json.loads(r.text)
    if exchange_data["result"] == "success":
        print("Exchange rates:")
        for currency, rate in exchange_data["conversion_rates"].items():
            #print(f"{currency}: {rate}")
            currency_dict[currency] = rate
    else:
        print("Failed to retrieve exchange rates.")


    def convert_currency():
        try:
            amount = float(amount_entry.get())
            selected_currency = currency_combobox.get()

            if selected_currency in currency_dict:
                converted_amount = amount * currency_dict[selected_currency]
                result_label.config(text=f"{amount} PKR is equal to {converted_amount:.2f} {selected_currency}")
            else:
                result_label.config(text="Invalid Currency")
        except ValueError:
            result_label.config(text="Please enter a valid amount")


    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry('500x500')

    amount_label = ttk.Label(root, text="Enter the amount")
    amount_label.pack()

    amount_entry = ttk.Entry(root)
    amount_entry.pack()

    currency_label = ttk.Label(root, text="Select the currency")
    currency_label.pack()

    currency_combobox = ttk.Combobox(root, values=list(currency_dict.keys()))
    currency_combobox.pack()

    convert_button = ttk.Button(root, text="Convert", command=convert_currency)
    convert_button.pack()

    result_label = ttk.Label(root, text="")
    result_label.pack()

    root.mainloop()

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
# except requests.exceptions.ConnectionError:



























