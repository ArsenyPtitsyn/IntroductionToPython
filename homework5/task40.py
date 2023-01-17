# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    encode_string = ''
    previous_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != previous_char:
            if previous_char:
                encode_string += str(count) + previous_char
            count = 1
            previous_char = char
        else:
            count += 1
    else:
        encode_string += str(count) + previous_char
        return encode_string

def rle_decode(data):
    decode_string = ''
    count = ''
    for i in range(len(data)):
        if not i % 2:
            count += data[i]
        else:
            decode_string += data[i] * int(count)
            count = ''
    return decode_string

data = '3377736'
encode_str = rle_encode(data)
print(encode_str)
decode_str = rle_decode(encode_str)
print(decode_str)