device = "RAK811"
ip_address = "172.16.10.2"
tty = "/dev/ttyUSB0"
rohc_compression = False
compress_mode ="zlib"
cipher_mode = "xor"
cipher_key = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
channel = 434000000
channelRx = channel
channelTx = channel
SF = 7
TxPower = 4
bandwidth = 0 # 0:125kHz, 1:250kHz, 2:500kHz
coderate = 1  # 1:4/5, 2:4/6, 3:4/7, 4:4/8
preambleLen = 8
mtu = 128 # 80
maxLoraFramesz = 119
#maxLoraFramesz = 51
