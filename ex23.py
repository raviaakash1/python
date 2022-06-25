# Sstring Bytes and Character Encoding

# in in_files folder there is a file called language.txt. This file was created with a list of human languages to
# demonstrate a few interesting concepts:
#   1.  How modern computers store human languages for display and processing and how Python3 calls this strings.
#   2.  How you must "encode" and "decode" Python's string into a type called bytes
#   3.  How to handles errors in string and byte handling
#   4.  How to read code an dfind out what it means even if you've never seen it before.

# Encoding done in language.txt is UTF-8.

import sys
from ex16 import get_abs_path





def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes, "<======>", cooked_string)


if __name__ == "__main__":

    script, encoding, error = sys.argv
    languages_abs_path = get_abs_path("languages.txt")

    with open(languages_abs_path, "r") as readPtr:
        main(readPtr, encoding, error)


'''
These examples use utf-8, utf-16 and big5 encoding to demo the conversion and the types of errors we can get.
Each of these lines are called a "codec" in Python3, but you use the parameter "encoding".
At the end I have listed down a list of encodings.

Switches, Conventions and Encoding
    How data is stored in a computer?
    --> Modern Computers are very Complex but at their cores they are like huge array of light switches.
        Computer uses electricity to flip switches on/off. These switches ca represent 1 or 0, 1 for on and 0 for off
        1 represents electricity, on, power, substance. 
        0 represents off, done, gone, power down, lack of energy.
        We call these 1 and 0 bits.

        Computers takes these 0s and 1s and use them to encode larger numbers. At the small end a computer will use 8
        of these 1s and 0s to encode 256 numbers (0-255) 

        What does encode mean though?
            --> Its nothing more than agreed upon standard for how a sequence of bits should represent a number.
                like 0000 0000 would be 0 and 1111 1111 would be 255, 0000 1111 would be 15.
        
        Today we call a "byte" a sequence of 8bits (1s and 0s). There are further conventions for encoding
        larger numbers using 16,32, 64 and even more bits.

        Once you have bytes you can start to store an ddisplay text by deciding on another convention for how 
        a number maps to a letter. 
        The most popular and in use convention is ASCII. This standard maps a number to letters.
        The number 90 is Z, which in bits is 1011010, which gets mapped to the ASCII table inside the computer.

        >>> 0b1011010
        90
        >>> ord('Z')
        90
        >>> chr('90')
        'Z'

        Once we have the ASCII convention for encoding a character using 8 bits (a byte), we can then 'string' 
        them together to make a word. If we want to write my name "Ravi" i just use a sequence of bytes:
        [82, 97, 118, 105].
        Most of the early text in computers was nothing more than sequences of bytes, stored in memory, that a computer
        used to display text to a person. Again, this is just a conventions that turned switches on or off.

        The problem with ASCII is that it only encodes English and maybe a few other similar languages,

        To solve this problem UniCode was created. It sounds like "encode" and it is meant to be "universal encoding" of all
        human languages. 

        The Solution Unicode provide is like ASCII table, but it's huge in comaprision.
        You can use 32 bit to encode a UniCode character, and that is more than character than we could possibly find.

        A 32 bit number means we can store 4.294,967,295 characters (2^32), These charcters are more than enough to
        store all the human languages and the remaining bits which are unused are used to emoji's.
        
        We now have a convention for encoding any characters we want, but 32 bits is 4 bytes which means there is so
        much wasted space in most text we want to encode. We can also use 16 bit, but still there's going to be wasted space
        in most text. 

        The solution is to use a clever convention to encode most common characters using 8 bits, and then "escape"
        inot larger numbers when we need to encode more characters. 

        That means we have one more convention that is nothing more than a compression encoding, making 
        it possible for most common characters to use 8 bits and then escape out into 16 or 32 bits as needed.

        The convention for encoding text in python is called "UTF-8", which means "Unicode Transformation Format 8
        Bits". Its a convention for encoding unicode characters into sequence bytes, which are sequence bits,
        which turn sequences of switches off and on. We can also use other conventions but UTF-8 is the standard for Python.

         
    Disecting the Ouput:

    Ouput Snippet of this script:
    b'Afrikaans' <======> Afrikaans
    b'\xc3\xa1\xc5\xa0 \xc3\xa1\xcb\x86\xe2\x80\xba\xc3\xa1\xcb\x86\xc2\xad\xc3\xa1\xc5\xa0\xe2\x80\xba' <======> áŠ áˆ›áˆ­áŠ›
    b'\xc3\x90\xc2\x90\xc3\x92\xc2\xa7\xc3\x91\xc2\x81\xc3\x91\xcb\x86\xc3\x93\xe2\x84\xa2\xc3\x90\xc2\xb0' <======> Ð§ÑÑˆÓ™Ð°
    b'\xc3\x98\xc2\xa7\xc3\x99\xe2\x80\x9e\xc3\x98\xc2\xb9\xc3\x98\xc2\xb1\xc3\x98\xc2\xa8\xc3\x99\xc5\xa0\xc3\x98\xc2\xa9' <======> Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©
    b'Aragon\xc3\x83\xc2\xa9s' <======> AragonÃ©s

    The script is taking bytes written inside b' ' (byte string) and converting them into UTF-8 (or other)
    encoding as per what you have specified.

    On the left is the number for each bytes of the UTF-8 (shown in hexa decimal)
    and the right side has the characters output as actual UTF-8.
    The way to think of this is the left side <=====> is the Python numerical bytes, or the 'raw' bytes Python
    uses to store the string. You specify this with b' ' to tell python this is bytes. These raw bytes are then displayed
    "cooked" on the right so you can see the real character in the terminal.

    Disceting the Code
    <-- Imp -->
    If we have raw bytes (b' ') then we need to use .decode() to get the string.
    Raw Bytes have no convention to them. They are just sequence of bytes with no meaning other than numbers, So you
    must tell Python to decode it into a UTF-8 string. If you have a string and want to send it, store it, share it,
    or do some other operation, then usually it'll work, but sometimes python will throw up error saying it doesn't know how to "encode" it.
    Again python knows its internal conventions, but it has no idea what convention you need. In that case use .encode()
    to get the bytes you need.
    
    <-- Imp -->
    They way to remember this is to remember the mnemonic DBES, which stands for Decode Byes, Encode Strings.
    Use this method to convert bytes to string. When you have bytes and need a string, decode bytes.
    When you have a string and need to bytes, encode string.


'''