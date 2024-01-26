

def f1(input):
    fct1= {
    '000':'101',
    '001':'100',
    '010':'111',
    '100':'000',
    '011': '001',
    '101':'101',
    '110':'010',
    '111':'110'
    }
    return fct1.get(input, "Key not found")

def f2(input):
    fct2= {
    '000':'010',
    '001':'001',
    '010':'110',
    '100':'111',
    '011': '110',
    '101':'011',
    '110':'001',
    '111':'110'
    }
    return  fct2.get(input, "Key not found")

def binary_xor(binary1, binary2):
    if len(binary1) != 3 or len(binary2) != 3:
        raise ValueError("Both input values must be binary strings of 3 digits.")

    result = ''
    for bit1, bit2 in zip(binary1, binary2):
        if bit1 == bit2:
            result += '0'
        else:
            result += '1'
    return result

c1= input('Enter your first sequence:')
c2= input('Enter your second sequence:')

p1=binary_xor(f2(c2),c1)
p2=binary_xor(f1(p1),c2)
p=p1+p2
print(p)