def decode_4g_cgi(hex_str):
    if not hex_str:
        return {
            'MCC': '000',
            'MNC': '00',
            'TAC_hex': '0000',
            'TAC_dec': '00000',
            'Cell_ID_hex': '0000000',
            'Cell_ID_dec': '000000000',
            'CGI_dec': '0000000000000000000'
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
        'TAC_hex': tac_hex,
        'TAC_dec': tac_dec_formatted,
        'Cell_ID_hex': cell_id_hex,
        'Cell_ID_dec': cell_id_dec_formatted,
        'CGI_dec': cgi_dec
    }

def decode_5g_cgi(hex_str):
    if not hex_str:
        return {
            'MCC': '000',
            'MNC': '00',
            'TAC_hex': '000000',
            'TAC_dec': '000000',
            'Cell_ID_hex': '000000000',
            'Cell_ID_dec': '00000000000',
            'CGI_dec': '0000000000000000000000'
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
        'TAC_hex': tac_hex,
        'TAC_dec': tac_dec_formatted,
        'Cell_ID_hex': cell_id_hex,
        'Cell_ID_dec': cell_id_dec_formatted,
        'CGI_dec': cgi_dec
    }

# Request user input
hex_4g_cgi = input('Enter 4G CGI in hex (or leave empty for default): ')
hex_5g_cgi = input('Enter 5G CGI in hex (or leave empty for default): ')

# Decode the input
decoded_4g_cgi = decode_4g_cgi(hex_4g_cgi)
decoded_5g_cgi = decode_5g_cgi(hex_5g_cgi)

# Print the decoded 4G CGI breakdown
print('\n4G CGI Breakdown:')
print(f'MCC (hex): {decoded_4g_cgi["MCC"]}')
print(f'MNC (hex): {decoded_4g_cgi["MNC"]}')
print(f'TAC (hex): {decoded_4g_cgi["TAC_hex"]} -> TAC (dec): {decoded_4g_cgi["TAC_dec"]}')
print(f'Cell ID (hex): {decoded_4g_cgi["Cell_ID_hex"]} -> Cell ID (dec): {decoded_4g_cgi["Cell_ID_dec"]}')
print(f'4G CGI (dec): {decoded_4g_cgi["CGI_dec"]}')

# Print the decoded 5G CGI breakdown
print('\n5G CGI Breakdown:')
print(f'MCC (hex): {decoded_5g_cgi["MCC"]}')
print(f'MNC (hex): {decoded_5g_cgi["MNC"]}')
print(f'TAC (hex): {decoded_5g_cgi["TAC_hex"]} -> TAC (dec): {decoded_5g_cgi["TAC_dec"]}')
print(f'Cell ID (hex): {decoded_5g_cgi["Cell_ID_hex"]} -> Cell ID (dec): {decoded_5g_cgi["Cell_ID_dec"]}')
print(f'5G CGI (dec): {decoded_5g_cgi["CGI_dec"]}')
