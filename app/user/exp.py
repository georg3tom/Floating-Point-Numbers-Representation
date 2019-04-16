from flask import jsonify

def float_bin(number, places = 3):
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int (dec)
    res = bin(whole).lstrip("0b") + "."

    for x in range(places):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole
    return res

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

def IEEE754(n) :

    # is positive or negative
    sign = 0
    if n < 0 :
        sign = 1
        n = n * (-1)
    p = 30

    # convert float to binary
    dec = float_bin (n, places = p)

    # separate the decimal part
    # and the whole number part
    whole, dec = str(dec).split(".")
    whole = int(whole)

    # calculating the exponent(E)
    exponent = len(str(whole)) - 1
    exponent_bits = 127 + exponent

    # converting the exponent from
    # decimal to binary
    exponent_bits = bin(exponent_bits).lstrip("0b")

    # finding the mantissa
    mantissa = str(whole)[1:exponent + 1]
    mantissa = mantissa + dec
    mantissa = mantissa[0:23]

    final = str(sign) + str(exponent_bits) + mantissa
    bourne={}
    bourne['status']="pass"
    bourne['sign']=sign
    bourne['exponent']=exponent+127
    bourne['exponent_bits']=exponent_bits
    bourne['mantissa']=mantissa
    bourne['final']=final
    return jsonify(bourne)

# print (IEEE754(263.3))
# print (IEEE754(-263.3))
