#!/usr/bin/python3

import os
import sys

bcntr = 0
hexes = []


def printable(char):
    if (ord(char) > 31):
        return char
    else:
        return "."

def op_0x8e():
    
    global bcntr
    global hexes
    bcntr +=1

    return ["adc a,(hl)", "0x8e", chr(0x8e)]

# see z80_dd.txt
#

def op_0xdd():

    pass
# see z80_fd.txt
#
def op_0xfd():
    pass
def op_0xce():              # adc a,n
    
    global bcntr
    global hexes
    bcntr +=1 # read n
    n = hexes[bcntr]
    n_ascii = printable(n[2:]) 

    return ["adc a," + "&" + n[2:],"0xce " +  n[2:], chr(0xce) + " " + chr(n_ascii)] 

def op_0x8f():
    global bcntr
    print ("adc a,a")
    bcntr +=1
def op_0x88():
    global bcntr 
    print("adc a,b")
    bcntr +=1
def op_0x89():
    global bcntr
    print("adc a,c")
    bcntr +=1
def op_0x8a():
    global bcntr
    print("adc a,d")
    bcntr +=1
def op_0x8b():
    global bcntr
    print("adc a,e")
    bcntr +=1
def op_0x8c():
    global bcntr
    print("adc a,c")
    bcntr +=1
def op_0x8d():
    global bcntr
    print("adc a,l")
    bcntr +=1
    # see z80_ed.txt
def op_0xed():
    global bcntr

    bcntr +=1
def op_0x86():
    pass
def op_0xc6():
    pass
def op_0x87():
    pass
def op_0x80():
    pass
def op_0x81():
    pass
def op_0x82():
    pass
def op_0x83():
    pass
def op_0x84():
    pass
def op_0x85():
    pass
def op_0x9():
    pass
def op_0x19():
    pass
def op_0x29():
    pass
def op_0x39():
    pass
def op_0xa6():
    pass
def op_0xe6():
    pass
def op_0xa7():
    pass
def op_0xa0():
    pass
def op_0xa1():
    pass
def op_0xa2():
    pass
def op_0xa3():
    pass
def op_0xa4():
    pass
def op_0xa5():
    pass
# see z80_cb.txt
#
def op_0xcb():
    pass
def op_0xcd():
    pass
def op_0xdc():
    pass
def op_0xfc():
    pass
def op_0xd4():
    pass
def op_0xc4():
    pass
def op_0xf4():
    pass
def op_0xc4():
    pass
def op_0xe4():
    pass
def op_0xcc():
    pass
def op_0x3f():
    pass
def op_0xfe():
    pass
def op_0xbe():
    pass
def op_0xbf():
    pass
def op_0xb8():
    pass
def op_0xb9():
    pass
def op_0xba():
    pass
def op_0xbb():
    pass
def op_0xbc():
    pass
def op_0xbd():
    pass
def op_0xed():
    pass
def op_0x2f():
    pass
def op_0x27():
    pass
def op_0x35():
    pass
def op_0x3d():
    pass
def op_0x5():
    pass
def op_0xb():
    pass
def op_0xd():
    pass
def op_0x15():
    pass
def op_0x1b():
    pass
def op_0x1d():
    pass
def op_0x25():
    pass
def op_0x2b():
    pass
def op_0x2d():
    pass
def op_0x3b():
    pass
def op_0xf3():
    pass
def op_0x10():
    pass
def op_0xfb():
    pass
def op_0xe3():
    pass
def op_0x8():
    pass
def op_0xeb():
    pass
def op_0xd9():
    pass
def op_0x76():
    pass
def op_0xdb():
    pass
def op_0x34():
    pass
def op_0x3c():
    pass
def op_0x4():
    pass
def op_0x3():
    pass
def op_0xc():
    pass
def op_0x14():
    pass
def op_0x13():
    pass
def op_0x1c():
    pass
def op_0x24():
    pass
def op_0x23():
    pass
def op_0x2c():
    pass
def op_0x33():
    pass
def op_0xc3():
    pass
def op_0xe9():
    pass
def op_0xda():
    pass
def op_0xfa():
    pass
def op_0xd2():
    pass
def op_0xc2():
    pass
def op_0xf2():
    pass
def op_0xea():
    pass
def op_0xe2():
    pass
def op_0xca():
    pass
def op_0x18():
    pass
def op_0x38():
    pass
def op_0x30():
    pass
def op_0x20():
    pass
def op_0x28():
    pass
def op_0x2():
    pass
def op_0x12():
    pass
def op_0x36():
    pass
def op_0x77():
    pass
def op_0x70():
    pass
def op_0x71():
    pass 
def op_0x72():
    pass
def op_0x73():
    pass
def op_0x74():
    pass
def op_0x75():
    pass
def op_0x32():
    pass
def op_0x22():
    pass
def op_0xa():
    pass
def op_0x1a():
    pass
def op_0x7e():
    pass
def op_0x3a():
    pass
def op_0x3e():
    pass
def op_0x7f():
    pass 
def op_0x78():
    pass
def op_0x79():
    pass
def op_0x7a():
    pass
def op_0x7b():
    pass
def op_0x7c():
    pass
def op_0x7d():
    pass
def op_0x46():
    pass
def op_0x6():
    pass
def op_0x47():
    pass
def op_0x40():
    pass
def op_0x41():
    pass
def op_0x42():
    global bcntr
    print("ld b,d")
    bcntr +=1

def op_0x43():
    pass
def op_0x44():
    pass
def op_0x45():
    pass
def op_0x1():
    pass
def op_0x4e():
    pass
def op_0xe():
    pass
def op_0x4f():
    global bcntr
    print("ld c,a" + "\t" + "; "+chr(0x04f))
    bcntr +=1
def op_0x48():
    pass
def op_0x49():
    pass
def op_0x4a():
    pass
def op_0x4b():
    pass
def op_0x4c():
    pass
def op_0x4d():
    pass
def op_0x56():
    pass
def op_0x16():
    pass
def op_0x57():
    pass
def op_0x50():
    pass
def op_0x51():
    pass
def op_0x52():
    pass
def op_0x53():
    pass
def op_0x54():
    pass
def op_0x55():
    pass
def op_0x11():
    pass
def op_0x5e():
    pass
def op_0x1e():
    pass
def op_0x5f():
    pass
def op_0x58():
    pass
def op_0x59():
    pass
def op_0x5a():
    pass
def op_0x5b():
    pass
def op_0x5c():
    pass
def op_0x5d():
    pass
def op_0x66():
    pass
def op_0x26():
    pass
def op_0x67():
    pass
def op_0x60():
    pass 
def op_0x61():
    pass
def op_0x62():
    pass
def op_0x63():
    pass
def op_0x64():
    pass
def op_0x65():
    pass
def op_0x2a():
    pass
def op_0x21():
    pass
def op_0x6e():
    pass
def op_0x2e():
    pass
def op_0x6f():
    pass
def op_0x68():
    pass
def op_0x69():
    pass
def op_0x6a():
    pass
def op_0x6b():
    pass
def op_0x6c():
    pass
def op_0x6d():
    pass
def op_0x31():
    pass
def op_0xf9():
    pass
def op_0x0():
    global bcntr
    print("nop")
    bcntr +=1
def op_0xb6():
    pass
def op_0xf6():
    pass
def op_0xb7():
    pass
def op_0xb0():
    pass
def op_0xb1():
    pass
def op_0xb2():
    pass
def op_0xb3():
    pass
def op_0xb4():
    pass
def op_0xb5():
    pass
def op_0xd3():
    pass
def op_0xf1():
    pass
def op_0xc1():
    pass
def op_0xd1():
    pass
def op_0xe1():
    pass
def op_0xf5():
    pass
def op_0xc5():
    pass
def op_0xd5():
    pass
def op_0xe5():
    pass
def op_0xc9():
    pass
def op_0xd8():
    pass
def op_0xf8():
    pass
def op_0xd0():
    pass
def op_0xc0():
    pass
def op_0xf0():
    pass
def op_0xe8():
    pass
def op_0xe0():
    pass
def op_0xc8():
    pass
def op_0x17():
    pass
def op_0x7():
    pass
def op_0x1f():
    pass
def op_0xf():
    pass
def op_0xc7():
    pass
def op_0xcf():
    pass
def op_0xd7():
    pass
def op_0xdf():
    pass
def op_0xe7():
    pass
def op_0xef():
    pass
def op_0xf7():
    pass
def op_0xff():
    pass
def op_0xde():
    pass
def op_0x9e():
    pass
def op_0x9f():
    pass
def op_0x98():
    pass
def op_0x99():
    pass
def op_0x9a():
    pass
def op_0x9b():
    pass
def op_0x9c():
    pass
def op_0x9d():
    pass
def op_0x37():
    pass
def op_0xd6():
    pass
def op_0x96():
    pass
def op_0x97():
    pass
def op_0x90():
    pass
def op_0x91():
    pass
def op_0x92():
    pass
def op_0x93():
    pass
def op_0x94():
    pass
def op_0x95():
    pass
def op_0xae():
    pass
def op_0xee():
    pass
def op_0xaf():
    pass
def op_0xa8():
    pass
def op_0xa9():
    pass
def op_0xaa():
    pass
def op_0xab():
    pass
def op_0xac():
    pass
def op_0xad():
    pass

mcode = { '0x0':  op_0x0,
          '0xdd': op_0xdd, 
          '0xfd': op_0xfd,
          '0xce': op_0xce,
          '0x8f': op_0x8f,
          '0x88': op_0x88,
          '0x89': op_0x89,
          '0x8a': op_0x8a,
          '0x8b': op_0x8b,
          '0x8c': op_0x8c,
          '0x8d': op_0x8d,
          '0xed': op_0xed,
          '0x8e': op_0x8e,
          '0x86': op_0x86,
          '0xc6': op_0xc6,
          '0x87': op_0x87,
          '0x80': op_0x80,
          '0x81': op_0x81,
          '0x82': op_0x82,
          '0x83': op_0x83,
          '0x84': op_0x84,
          '0x85': op_0x85,
          '0x9': op_0x9,
          '0x19': op_0x19,
          '0x29': op_0x29,
          '0x39': op_0x39,
          '0xa6': op_0xa6,
          '0xe6': op_0xe6,
          '0xa7': op_0xa7,
          '0xa0': op_0xa0,
          '0xa1': op_0xa1,
          '0xa2': op_0xa2,
          '0xa3': op_0xa3,
          '0xa4': op_0xa4,
          '0xa5': op_0xa5,
          '0xcb': op_0xcb,
          '0xcd': op_0xcd,
          '0xdc': op_0xdc,
          '0xfc': op_0xfc,
          '0xd4': op_0xd4,
          '0xc4': op_0xc4,
          '0xf4': op_0xf4,
          '0xec': op_0xe4,
          '0xe4': op_0xe4,
          '0xcc': op_0xcc,
          '0x3f': op_0x3f,
          '0xfe': op_0xfe,
          '0xbe': op_0xbe,
          '0xbf': op_0xbf,
          '0xb8': op_0xb8,
          '0xb9': op_0xb9,
          '0xba': op_0xba,
          '0xbb': op_0xbb,
          '0xbc': op_0xbc,
          '0xbd': op_0xbd,
          '0xed': op_0xed,
          '0x2f': op_0x2f,
          '0x27': op_0x27,
          '0x35': op_0x35,
          '0x3d': op_0x3d,
          '0x5': op_0x5,
          '0xb': op_0xb,
          '0xd': op_0xd,
          '0x15': op_0x15,
          '0x1b': op_0x1b,
          '0x1d': op_0x1d,
          '0x25': op_0x25,
          '0x2b': op_0x2b,
          '0x2d': op_0x2d,
          '0x3b': op_0x3b,
          '0xf3': op_0xf3,
          '0x10': op_0x10,
          '0xfb': op_0xfb,
          '0xe3': op_0xe3,
          '0x8': op_0x8,
          '0xeb': op_0xeb,
          '0xd9': op_0xd9,
          '0x76': op_0x76,
          '0xdb': op_0xdb,
          '0x34': op_0x34,
          '0x3c': op_0x3c,
          '0x4': op_0x4,
          '0x3': op_0x3,
          '0xc': op_0xc,
          '0x14': op_0x14,
          '0x13': op_0x13,
          '0x1c': op_0x1c,
          '0x24': op_0x24,
          '0x23': op_0x23,
          '0x2c': op_0x2c,
          '0x33': op_0x33,
          '0xc3': op_0xc3,
          '0xe9': op_0xe9,
          '0xda': op_0xda,
          '0xfa': op_0xfa,
          '0xd2': op_0xd2,
          '0xc2': op_0xc2,
          '0xf2': op_0xf2,
          '0xea': op_0xea,
          '0xe2': op_0xe2,
          '0xca': op_0xca,
          '0x18': op_0x18,
          '0x38': op_0x38,
          '0x30': op_0x30,
          '0x20': op_0x20,
          '0x28': op_0x28,
          '0x2': op_0x2,
          '0x12': op_0x12,
          '0x36': op_0x36,
          '0x77': op_0x77,
          '0x70': op_0x70,
          '0x71': op_0x71,
          '0x72': op_0x72,
          '0x73': op_0x73,
          '0x74': op_0x74,
          '0x75': op_0x75,
          '0x32': op_0x32,
          '0x22': op_0x22,
          '0xa': op_0xa,
          '0x1a': op_0x1a,
          '0x7e': op_0x7e,
          '0x3a': op_0x3a,
          '0x3e': op_0x3e,
          '0x7f': op_0x7f,
          '0x78': op_0x78,
          '0x79': op_0x79,
          '0x7a': op_0x7a,
          '0x7b': op_0x7b,
          '0x7c': op_0x7c,
          '0x7d': op_0x7d,
          '0x46': op_0x46,
          '0x6': op_0x6,
          '0x47': op_0x47,
          '0x40': op_0x40,
          '0x41': op_0x41,
          '0x42': op_0x42,
          '0x43': op_0x43,
          '0x44': op_0x44,
          '0x45': op_0x45,
          '0x1': op_0x1,
          '0x4e': op_0x4e,
          '0xe': op_0xe,
          '0x4f': op_0x4f,
          '0x48': op_0x48,
          '0x49': op_0x49,
          '0x4a': op_0x4a,
          '0x4b': op_0x4b,
          '0x4c': op_0x4c,
          '0x4d': op_0x4d,
          '0x56': op_0x56,
          '0x16': op_0x16,
          '0x57': op_0x57,
          '0x50': op_0x50,
          '0x51': op_0x51,
          '0x52': op_0x52,
          '0x53': op_0x53,
          '0x54': op_0x54,
          '0x55': op_0x55,
          '0x11': op_0x11,
          '0x5e': op_0x5e,
          '0x1e': op_0x1e,
          '0x5f': op_0x5f,
          '0x58': op_0x58,
          '0x59': op_0x59,
          '0x5a': op_0x5a,
          '0x5b': op_0x5b,
          '0x5c': op_0x5c,
          '0x5d': op_0x5d,
          '0x66': op_0x66,
          '0x26': op_0x26,
          '0x67': op_0x67,
          '0x60': op_0x60,
          '0x61': op_0x61,
          '0x62': op_0x62,
          '0x63': op_0x63,
          '0x64': op_0x64,
          '0x65': op_0x65,
          '0x2a': op_0x2a,
          '0x21': op_0x21,
          '0x6e': op_0x6e,
          '0x2e': op_0x2e,
          '0x6f': op_0x6f,
          '0x68': op_0x68,
          '0x69': op_0x69,
          '0x6a': op_0x6a,
          '0x6b': op_0x6b,
          '0x6c': op_0x6c,
          '0x6d': op_0x6d,
          '0x31': op_0x31,
          '0xf9': op_0xf9,
          '0x0': op_0x0,
          '0xb6': op_0xb6,
          '0xf6': op_0xf6,
          '0xb7': op_0xb7,
          '0xb0': op_0xb0,
          '0xb1': op_0xb1,
          '0xb2': op_0xb2,
          '0xb3': op_0xb3,
          '0xb4': op_0xb4,
          '0xb5': op_0xb5,
          '0xd3': op_0xd3,
          '0xf1': op_0xf1,
          '0xc1': op_0xc1,
          '0xd1': op_0xd1,
          '0xe1': op_0xe1,
          '0xf5': op_0xf5,
          '0xc5': op_0xc5,
          '0xd5': op_0xd5,
          '0xe5': op_0xe5,
          '0xc9': op_0xc9,
          '0xd8': op_0xd8,
          '0xf8': op_0xf8,
          '0xd0': op_0xd0,
          '0xc0': op_0xc0,
          '0xf0': op_0xf0,
          '0xe8': op_0xe8,
          '0xe0': op_0xe0,
          '0xc8': op_0xc8,
          '0x17': op_0x17,
          '0x7': op_0x7,
          '0x1f': op_0x1f,
          '0xf': op_0xf,
          '0xc7': op_0xc7,
          '0xcf': op_0xcf,
          '0xd7': op_0xd7,
          '0xdf': op_0xdf,
          '0xe7': op_0xe7,
          '0xef': op_0xef,
          '0xf7': op_0xf7,
          '0xff': op_0xff,
          '0xde': op_0xde,
          '0x9e': op_0x9e,
          '0x9f': op_0x9f,
          '0x98': op_0x98,
          '0x99': op_0x99,
          '0x9a': op_0x9a,
          '0x9b': op_0x9b,
          '0x9c': op_0x9c,
          '0x9d': op_0x9d,
          '0x37': op_0x37,
          '0xd6': op_0xd6,
          '0x96': op_0x96,
          '0x97': op_0x97,
          '0x90': op_0x90,
          '0x91': op_0x91,
          '0x92': op_0x92,
          '0x93': op_0x93,
          '0x94': op_0x94,
          '0x95': op_0x95,
          '0xae': op_0xae,
          '0xee': op_0xee,
          '0xaf': op_0xaf,
          '0xa8': op_0xa8,
          '0xa9': op_0xa9,
          '0xaa': op_0xaa,
          '0xab': op_0xab,
          '0xac': op_0xac,
          '0xad': op_0xad
}

def slurp(filename):

    cpcbin_fname = filename        
    cpcbin = open(cpcbin_fname, "rb")
    cpcbin_len = (os.stat(cpcbin_fname)).st_size
    cpcbin_bytes = cpcbin.read(cpcbin_len)
    cpcbin_hex_list = [hex(i) for i in cpcbin_bytes]
    cpcbin.close()

    return cpcbin_hex_list


hexes = slurp(sys.argv[1])
while(1):
    byte = hexes[bcntr]
    op_func = mcode[byte]
    op_func()
    print(bcntr)
    print(byte)

#
#
# NOTE: make op_0x?? calls return a list, not print the disassembly.
# Delegate the printing/formating to another function. Otherwise every single change you make in opcodes, # will need to propagate to 150+ functions. Also, you need to put code that outputs different formats,
# depending: i) just the asm source? ii) the asm source and the ascii codes? iii) addresses/labels?


