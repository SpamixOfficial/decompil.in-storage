from base64 import b85encode
from time import sleep

x = open("key", 'r').read()
y = open("contents", 'r').read()

print("""#######################################################
#                                                     #
#                                                     #
#                                                     #
#                                                     #
#                     3NCRYPTING                      #
#                                                     #
#                                                     #
#                                                     #
#                                                     #
#######################################################""")
sleep(1)

encrypted_content = [chr(ord(a) ^ ord(b)) for a,b in zip(y, x)]

open('output', 'w').write(b85encode(bytes(''.join(encrypted_content), 'utf-8')).decode('utf-8'))
