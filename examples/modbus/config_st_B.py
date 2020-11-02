device = "B-L072Z-LRWAN1"
ip_address = "172.16.10.2"
tty = "/dev/ttyACM0"
rohc_compression = False
compress_mode ="zlib"   # "zlib" or None
cipher_mode = "xor"     # "xor" or None
cipher_key = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
channelRx = 868000000
channelTx = 868300000
SF = 7
TxPower = 2 # 14 max
bandwidth = 0 # 0:125kHz, 1:250kHz, 2:500kHz, 3: Reserved
coderate = 1  # 1:4/5, 2:4/6, 3:4/7, 4:4/8
preambleLen = 8
mtu = 128
maxLoraFramesz = 255
