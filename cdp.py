#/usr/bin/env python3

from scapy.all import *
import struct

def mac_to_bytes(mac):
    mac_no_colon = mac.replace(":", "")
    return bytes.fromhex(mac_no_colon)

class Eth_frame():
    def __init__(self, smac):
        self._dmac = "01:00:0C:CC:CC:CC"
        self._smac = smac
        self._payload = None

    def add_payload(self, payload):
        self._payload = payload

    def to_bytes(self):
        # siet je big endian a preto musime niekedy obracat poradie byteov
        out = mac_to_bytes(self._dmac) + mac_to_bytes(self._smac)
        out += struct.pack("!H", len(self._payload.to_bytes()))
        out += self._payload.to_bytes()
        return out

class CDP_hdr():
    def __init__(self):
        self._version = 1
        self._ttl = 180
        self._checksum = 0
        self._payload = list()

    def add_payload(self, payload):
        self._payload.append(payload)

    def to_bytes(self):
        out = struct.pack("!2BH", self._version, self._ttl, self._checksum)
        for tlv in self._payload:
            out += tlv.to_bytes()
        return out

class TLV():
    def __init__(self, type):
        self._type = type
        self._length = 4
    
    def to_bytes(self):
        return struct.pack("!2H", self._type, self._length)

class TLV_device_id(TLV):
    def __init__(self, device_id):
        super().__init__(0x0001)
        self._device_id = device_id
        self._length += len(device_id)
    
    def to_bytes(self):
        device_bytes = self._device_id.encode()
        self._length += len(device_bytes)
        out = super().to_bytes()
        out += device_bytes
        return out

class LLC():
    def __init__(self):
        self._dsap = 0XAA
        self._ssap = 0XAA
        self._ctrl = 0x03
        self._oui = "00:00:0C"
        self._pid = 0x2000
        self._payload = None

    def add_payload(self, payload):
        self._payload = payload
    
    def to_bytes(self):
        out = struct.pack("!BBB", self._dsap, self._ssap, self._ctrl)
        out += mac_to_bytes(self._oui)
        out += struct.pack("!H", self._pid)
        out += self._payload.to_bytes()
        return out

if __name__ == "__main__":
    # Create a CDP packet
    IFACES.show()
    iface = IFACES.dev_from_index(16)
    sock = conf.L2socket(iface=iface)
    
    frame = Eth_frame(smac="11:22:33:44:55:66")
    llc = LLC()
    cdp = CDP_hdr()
    TLV_device_id = TLV_device_id(device_id="BENJI")

    cdp.add_payload(TLV_device_id)
    llc.add_payload(cdp)
    frame.add_payload(llc)

    sock.send(frame.to_bytes())