import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
def decode_4g_cgi(hex_str):
    if not hex_str:
        return {
            'MCC': ('000', 3),
            'MNC': ('00', 2),
            'TAC': ('00000', 5),
            'Cell ID': ('000000000', 9),
            '4G CGI (Dec)': ('0000000000000000000', 19)
        }

    # Split the hex string into its components
    mcc = hex_str[:3]
    mnc = hex_str[3:5]
    tac_hex = hex_str[5:9]
    cell_id_hex = hex_str[9:]

    # Convert TAC and Cell ID to decimal
    tac_dec = int(tac_hex, 16)
    cell_id_dec = int(cell_id_hex, 16)

    # Format TAC and Cell ID with leading zeros
    tac_dec_formatted = f'{tac_dec:05d}'
    cell_id_dec_formatted = f'{cell_id_dec:09d}'

    # Combine all parts to form the final CGI in decimal
    cgi_dec = f'{mcc}{mnc}{tac_dec_formatted}{cell_id_dec_formatted}'

    return {
        'MCC': (mcc, len(mcc)),
        'MNC': (mnc, len(mnc)),
        'TAC (Hex)': (tac_hex, len(tac_hex)),
        'TAC (Dec)': (tac_dec_formatted, len(tac_dec_formatted)),
        'Cell ID (Hex)': (cell_id_hex, len(cell_id_hex)),
        'Cell ID (Dec)': (cell_id_dec_formatted, len(cell_id_dec_formatted)),
        '4G CGI (Dec)': (cgi_dec, len(cgi_dec))
    }

def decode_5g_cgi(hex_str):
    if not hex_str:
        return {
            'MCC': ('000', 3),
            'MNC': ('00', 2),
            'TAC': ('000000', 6),
            'Cell ID': ('00000000000', 11),
            '5G CGI (Dec)': ('0000000000000000000000', 22)
        }

    # Split the hex string into its components
    mcc = hex_str[:3]
    mnc = hex_str[3:5]
    tac_hex = hex_str[5:11]
    cell_id_hex = hex_str[11:]

    # Convert TAC and Cell ID to decimal
    tac_dec = int(tac_hex, 16)
    cell_id_dec = int(cell_id_hex, 16)

    # Format TAC and Cell ID with leading zeros
    tac_dec_formatted = f'{tac_dec:06d}'
    cell_id_dec_formatted = f'{cell_id_dec:011d}'

    # Combine all parts to form the final CGI in decimal
    cgi_dec = f'{mcc}{mnc}{tac_dec_formatted}{cell_id_dec_formatted}'

    return {
        'MCC': (mcc, len(mcc)),
        'MNC': (mnc, len(mnc)),
        'TAC (Hex)': (tac_hex, len(tac_hex)),
        'TAC (Dec)': (tac_dec_formatted, len(tac_dec_formatted)),
        'Cell ID (Hex)': (cell_id_hex, len(cell_id_hex)),
        'Cell ID (Dec)': (cell_id_dec_formatted, len(cell_id_dec_formatted)),
        '5G CGI (Dec)': (cgi_dec, len(cgi_dec))
    }

def decode_cgi():
    hex_4g_cgi = entry_4g.get()
    hex_5g_cgi = entry_5g.get()
    
    decoded_4g_cgi = decode_4g_cgi(hex_4g_cgi)
    decoded_5g_cgi = decode_5g_cgi(hex_5g_cgi)
    
    # Display 4G results
    result_4g.delete(1.0, tk.END)
    result_4g.insert(tk.END, "4G CGI Breakdown:\n")
    for key, (value, digits) in decoded_4g_cgi.items():
        result_4g.insert(tk.END, f'{key}: {value} (Digits: {digits})\n')
    
    # Display 5G results
    result_5g.delete(1.0, tk.END)
    result_5g.insert(tk.END, "5G CGI Breakdown:\n")
    for key, (value, digits) in decoded_5g_cgi.items():
        result_5g.insert(tk.END, f'{key}: {value} (Digits: {digits})\n')

# Create the main window
root = tk.Tk()
root.title("CGI Cell Decoder Hex to Dec")

# Add title
ttk.Label(root, text="Mohanad [CGI Cell Decoder Hex to Dec]", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Add logo image
image = Image.open("du.png")
image = image.resize((100, 100), Image.LANCZOS)
logo = ImageTk.PhotoImage(image)
logo_label = ttk.Label(root, image=logo)
logo_label.grid(row=1, column=0, columnspan=2, pady=10)

# Add input fields
ttk.Label(root, text="Enter 4G CGI in hex:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_4g = ttk.Entry(root, width=30)
entry_4g.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Enter 5G CGI in hex:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_5g = ttk.Entry(root, width=30)
entry_5g.grid(row=3, column=1, padx=10, pady=5)

# Add decode button
decode_button = ttk.Button(root, text="Decode", command=decode_cgi)
decode_button.grid(row=4, column=0, columnspan=2, pady=10)

# Add results display
result_4g = tk.Text(root, height=10, width=60)
result_4g.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

result_5g = tk.Text(root, height=10, width=60)
result_5g.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Add note
ttk.Label(root, text="Done by M. ElSakka, All Rights Reserved 2024 ©️", font=("Helvetica", 8)).grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
# end of code