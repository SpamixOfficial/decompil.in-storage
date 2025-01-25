i = __import__("importlib")
b = i.import_module("base64").b64encode
t = i.import_module("time").sleep
x = open("key", 'r').read()
z = open("key2", 'r').read()
y = open("contents", 'r').read()

def base128(s1, s2):
    a = b(bytes(s1, 'utf-8')).decode('utf-8')
    c = b(bytes(s2, 'utf-8')).decode('utf-8')
    d = a + c
    return d

print("""#######################################################
#                                                     #
#                                                     #
#                                                     #
#                       D0UBL3                        #
#                     3NCRYPTING                      #
#                                                     #
#                                                     #
#                                                     #
#                                                     #
#######################################################""")
t(1)
encrypted = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(y, x)])
encryptedd = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(y, z)])

double_encrypted = base128(encrypted, encryptedd)

open('output', 'w').write(double_encrypted)
