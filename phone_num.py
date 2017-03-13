dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")

import re

def phone(strng, num):
    # cleaning
    # очистка строки от посторонних символов
    # все символы кромен - цифр строчных, заглавных, пробельных символов, отсрых скобок и
    # символа переноса строки заменяются на пробелы
    clean = re.sub(r"[^-0-9a-z\s+A-Z<>\n.']", ' ', strng)
    # формируется список строк в которых есть номер с вхождением номера
    a = re.findall('.*\+' + num + '.*', clean)
    print(type(a),len(a),a)
    # если в списке больше 1 элемента, то пишут "ошибка@
    if (len(a) > 1): return "Error => Too many people: " + num
    # если в списке нет элементов, то выдаем сообщени о том, что не найден
    if (len(a) == 0): return "Error => Not found: " + num
    # replace num
    # вырезаем номер ин строки с вхождением норем сам номер
    c = re.sub('\+' + num, '', a[0])
    print('c=',c)
    # name
    # далее находим в том что осталось имя человека
    name = re.findall('<.*>', c)[0]
    print('name', name)
    # address

    ad = re.sub(r'\s+', ' ', re.sub(r'<.*>','', c)).strip()
    print('ad=', ad)
    return "Phone => " + num + ", Name => " + name[1:len(name)-1] + ", Address => " + ad

print(len(dr))
ans=phone(dr,'+19-421-674-8974')