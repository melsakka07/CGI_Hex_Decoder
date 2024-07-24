############################################################
# Thanks for using Mohanad [CGI Cell Decoder Hex to Dec] code
############################################################

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

# Request user input
print('                                                          ')
print('############################################################')
print('Thanks for using Mohanad [CGI Cell Decoder Hex to Dec] code')
print('############################################################')
print('                                                          ')
hex_4g_cgi = input('Please Enter 4G CGI in hex (or leave empty for default): ')
hex_5g_cgi = input('Please Enter 5G CGI in hex (or leave empty for default): ')

# Decode the input
decoded_4g_cgi = decode_4g_cgi(hex_4g_cgi)
decoded_5g_cgi = decode_5g_cgi(hex_5g_cgi)

# Print the results
print("\n4G CGI Breakdown:")
for key, (value, digits) in decoded_4g_cgi.items():
    print(f'{key}: {value} (Digits: {digits})')

print("\n5G CGI Breakdown:")
for key, (value, digits) in decoded_5g_cgi.items():
    print(f'{key}: {value} (Digits: {digits})')

# end of code