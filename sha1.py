import struct
def sha1(data):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    data = bytearray(data, 'ascii')  # Convert to bytearray
    orig_len_bits = (8 * len(data)) & 0xffffffffffffffff
    data.append(0x80)
    while len(data) % 64 != 56:
        data.append(0)

    data += struct.pack('>Q', orig_len_bits)

    # Process each 512-bit chunk
    for i in range(0, len(data), 64):
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', data[i + j * 4:i + j * 4 + 4])[0]

        for j in range(16, 80):
            w[j] = left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


# Example usage
print(sha1("hello world"))
