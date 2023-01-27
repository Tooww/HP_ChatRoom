import io

from dvic_chat.protocol import DataStream

class FakeSocket:

    def __init__(self) -> None:
        self.buffer = io.BytesIO()

    def send(self, b: bytes):
        self.buffer.write(b)

    def recv(self, size: int) -> bytes:
        self.buffer.seek(0)
        return self.buffer.read(size)
    

    #moi
    def recv_str(self, size: str) -> bytes:
        self.buffer.seek(0)
        return self.buffer.read(size)
    
    
def test_receive_int():
    fs = FakeSocket()
    fs.send(b'\x00\x00\x00*') # 42 in bytes

    ds = DataStream(fs)
    assert ds.receive_int() == 42

def test_send_int():
    fs = FakeSocket()

    ds = DataStream(fs)
    ds.send_int(42)
    fs.buffer.seek(0)
    assert fs.buffer.read() == b'\x00\x00\x00*'

#def send_int(self, i: int):
#        self.sck.send(i.to_bytes(4, 'big'))
    
#    def receive_int(self) -> int:        
#        return int.from_bytes(self.sck.recv(struct.calcsize('i')), 'big')

#    def send_str(self, s: str):
#        bs = s.encode('utf-8')
#        self.send_int(len(bs))
#        self.sck.send(bs)
    
#    def receive_str(self) -> int:
#        l = self.receive_int()
#        return self.sck.recv(l).decode('utf-8')



def test_send_str():
    bs = FakeSocket()
    ds = DataStream(bs)
    
    ds.send_str("Tom")

    bs.buffer.seek(0)
    assert bs.buffer.read() == b'\x00\x00\x00\x03Tom'
    
