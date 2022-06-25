# The \ character encodes difficult to type characters into string.

# Escape sequences:
#     \\      -->     Backslash(\)
#     \'      -->     Signle-Quote(')
#     \"      -->     Double Quote (")
#     \a      -->     Ascii bell (BEL)
#     \b      -->     Ascii BackSpace (BS)
#     \f      -->     Ascii formfeed(FF)
#     \n      -->     Ascii linefeed(LF)
#     \N{name}-->     Character named name in the Unicode database (Unicode Only)
#     \r      -->     Carriage retuen(CR)
#     \t      -->     Horizontal Tab(TAB)
#     \uxxxx  -->     Character with 16 bit hex value
#     \Uxxxxxxxx      -->     Character with 32-bit hex value
#     \v      -->     Ascii Vertical Tab(VT)
#     \ooo    -->     Character with octal value ooo
#     \xhh    -->     Character with hex value hh



print("\\")
print('\'')
print("\"")
print("hi\ahow")
print("name is\bdata")
print("will this\fformat")
print("new\nline")
# print("new\N{KeyError}line")  No idea what it does unicode name means --> pre defined name like KeyError?
print("data\rhere") 
print("data\tname")
print("what is\u1234 does")
# print("what does \U11010101 does")  Not taking 32 bit hex value need to check
print("Vertical\vtab")
# print("Character with octal value \OOOOO") need to provide an octal value
# print("\x12") need to provide a hex value