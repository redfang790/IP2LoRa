device = "LoStick"
ip_address = "172.16.10.1"
tty = "/dev/ttyUSB0"
rohc_compression = False
compress_mode ="zlib"
cipher_mode = "xor"
cipher_key = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
channel = 868300000
channelRx = channel
channelTx = channel
SF = 7
TxPower = 2 # 14 max
bandwidth = 0 # 0:125kHz, 1:250kHz, 2:500kHz, 3: Reserved
coderate = 1  #1:4/5, 2:4/6, 3:4/7, 4:4/8
preambleLen = 8
mtu = 200
maxLoraFramesz = 255
