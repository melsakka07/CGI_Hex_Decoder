def decode_4g_cgi(hex_str):
    if not hex_str:
        return {
            'MCC': '000',
            'MNC': '00',
            'TAC': '00000',
            'Cell ID': '000000000'
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
        'MCC': mcc,
        'MNC': mnc,
        'TAC (Hex)': tac_hex,
        'TAC (Dec)': tac_dec_formatted,
        'Cell ID (Hex)': cell_id_hex,
        'Cell ID (Dec)': cell_id_dec_formatted,
        '4G CGI (Dec)': cgi_dec
    }

def decode_5g_cgi(hex_str):
    if not hex_str:
        return {
            'MCC': '000',
            'MNC': '00',
            'TAC': '000000',
            'Cell ID': '00000000000'
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
        'MCC': mcc,
        'MNC': mnc,
        'TAC (Hex)': tac_hex,
        'TAC (Dec)': tac_dec_formatted,
        'Cell ID (Hex)': cell_id_hex,
        'Cell ID (Dec)': cell_id_dec_formatted,
        '5G CGI (Dec)': cgi_dec
    }

# Request user input
hex_4g_cgi = input('Enter 4G CGI in hex (or leave empty for default): ')
hex_5g_cgi = input('Enter 5G CGI in hex (or leave empty for default): ')

# Decode the input
decoded_4g_cgi = decode_4g_cgi(hex_4g_cgi)
decoded_5g_cgi = decode_5g_cgi(hex_5g_cgi)

# Print the results
print("\n4G CGI Breakdown:")
for key, value in decoded_4g_cgi.items():
    print(f'{key}: {value}')

print("\n5G CGI Breakdown:")
for key, value in decoded_5g_cgi.items():
    print(f'{key}: {value}')
