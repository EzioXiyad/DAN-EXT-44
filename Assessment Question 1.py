enc_count = {}
dec_count = {}
enc_map = {}

def encryption(shift1, shift2):
    with open('raw_text.txt', 'r', encoding='utf-8') as f_in, open('encrypted_text.txt', 'w', encoding='utf-8') as f_out:
        for n in f_in.read():
            if n.islower() and "a" <= n <= "m":
                final_value = chr(ord(n) + (shift1 * shift2))
            elif n.islower() and "n" <= n <= "z":
                final_value = chr(ord(n) - (shift1 + shift2))
            elif n.isupper() and "A" <= n <= "M":
                final_value = chr(ord(n) - shift1)
            elif n.isupper() and "N" <= n <= "Z":
                final_value = chr(ord(n) + (shift2 ** 2))
            else:
                final_value = n
            enc_count[final_value] = enc_count.get(final_value, 0) + 1
            enc_map[f'{final_value}{enc_count[final_value]}'] = n
            f_out.write(final_value)
    return enc_map

def decryption(enc_map):
    with open('encrypted_text.txt', 'r', encoding='utf-8') as f_in, open('decrypted_text.txt', 'w', encoding='utf-8') as f_out:
        for n in f_in.read():
            dec_count[n] = dec_count.get(n, 0) + 1
            f_out.write(enc_map.get(f'{n}{dec_count[n]}', n))

def comparing():
    with open('raw_text.txt', 'r', encoding='utf-8') as f1, open('decrypted_text.txt', 'r', encoding='utf-8') as f2:
        print("Decryption successful" if f1.read() == f2.read() else "Decryption failed")

v1 = int(input("Enter a number (1-9): "))
v2 = int(input("Enter a number (1-9): "))
encryption(v1, v2)
decryption(enc_map)
comparing()
