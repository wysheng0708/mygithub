s = "你好世界"

# 编码为字节
s_code = s.encode('utf-8')
print(s_code)          # b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c'

# 解码为字符串
decoded_str = s_code.decode('utf-8')
print(decoded_str)         # "你好世界"

#str.encode(encoding='utf-8', errors='strict')
#bytes.decode(encoding='utf-8', errors='strict')
#errors还有ignore和replace