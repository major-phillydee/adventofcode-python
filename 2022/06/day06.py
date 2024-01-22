def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    PACKET_LEN = 4
    MESSAGE_LEN = 14

    buffer = lines[0].strip()

    first_packet_idx = 0
    for index in range(PACKET_LEN, len(buffer)):
        packet = buffer[index-PACKET_LEN:index]
        if is_valid_packet(packet):
            first_packet_idx = index
            break

    first_message_idx = -1
    for index in range(MESSAGE_LEN, len(buffer)):
        message = buffer[index-MESSAGE_LEN:index]
        if is_valid_packet(message):
            first_message_idx = index
            break

    return {'first_packet_idx': first_packet_idx,
            'first_message_idx': first_message_idx}


def is_valid_packet(packet):
    bits = [ch for ch in packet]
    bit_set = set(bits)
    return len(bit_set) == len(bits)


if __name__ == '__main__':
    print(main())
