Str=' I Love Python'
m=''
for i in range(0,len(Str)):
    if(Str[i].isupper()):
        m=m+Str[i].lower()
    elif Str[i].islower():
        m=m+Str[i].upper()
    else:
        if i%2==0:
            m=m+Str[i-1]
        else:
            m=m+'#'

print(m)