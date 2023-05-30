import struct


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = struct.calcsize(pattern)
        data = struct.unpack_from(self.order + pattern,
                                  self.stream, self.offset)
        self.offset += size
        return data[0]


def read_a(reader):
    b_size = reader.read(Types.uint16)
    b_offset = reader.read(Types.uint16)
    b_reader = reader.jump(b_offset)
    a1 = [read_b(b_reader) for _ in range(b_size)]
    a2 = [reader.read(Types.int8) for _ in range(4)]
    a3 = reader.read(Types.uint32)
    d_offset = reader.read(Types.uint16)
    d_reader = reader.jump(d_offset)
    a4 = read_d(d_reader)
    a5 = reader.read(Types.int32)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5)


def read_b(reader):
    c_array_size = reader.read(Types.uint16)  # размер массива адресов
    c_array_offset = reader.read(Types.uint16)  # адрес массива адресов
    c_array_reader = reader.jump(c_array_offset)
    c_structs_offsets = [c_array_reader.read(Types.uint32)
                         for _ in range(c_array_size)]  # адреса структур с
    b1 = [read_c(reader.jump(c_structs_offsets[j]))
          for j in range(c_array_size)]
    b2 = reader.read(Types.uint8)
    return dict(B1=b1, B2=b2)


def read_c(reader):
    c1 = [reader.read(Types.uint8) for _ in range(4)]
    c2 = reader.read(Types.uint8)
    return dict(C1=c1, C2=c2)


def read_d(reader):
    d1_size = reader.read(Types.uint32)
    d1_offset = reader.read(Types.uint16)
    d1_reader = reader.jump(d1_offset)
    d1 = [d1_reader.read(Types.int16) for _ in range(d1_size)]
    d2 = reader.read(Types.float)
    d3 = reader.read(Types.int8)
    d4 = reader.read(Types.uint32)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


SIGNATURE_OFFSET = 3


def main(stream):
    return read_a(BinaryReader(stream, SIGNATURE_OFFSET))
