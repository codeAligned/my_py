from re import search
# regex='(?!=\s)(?=^.{6,}$)(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).*$'

# (?=.*[A-Z])
# regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$'


regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$'

print(search(regex, '1jds  ssssaIR9'))
print(search(regex, 'ghdj hghgAfj32'))
print(search(regex, 'fjd3IR9'))
print(search(regex, '1 sZsssZ'))
print(search(regex, 'fj1dsagdfzAgxfg'))
print(search(regex, 'fjd3  IR9'))
print(search(regex, 'fjd3IR9.;'))
