def convert(str, case): 
    st=""
    for i in str:
            x = ord(i)
            if (96<x<123) or (64<x<91) or x==32:
                st= st+(i)
    st=st.split()

    if(case == "camel"):
        for i in range(len(st)): 
            if i>0: 
                st[i]=st[i].capitalize()
            else: st[i]= st[i].lower()
        
        return "".join(st)
    elif case == 'snake': 
        for i in range(len(st)): 
            st[i]= st[i].lower()
        
        return "_".join(st)
    elif case == 'kebab': 
        for i in range(len(st)): 
            st[i]= st[i].lower()
        
        return "-".join(st)
    elif case == 'pascal': 
        for i in range(len(st)): 
            st[i]= st[i].capitalize()
        
        return "".join(st)
    elif case == 'uppercasesnake': 
        for i in range(len(st)): 
            st[i]= st[i].upper()
        
        return "_".join(st)


print(convert("Hello, world.","camel"))
print(convert("Hello, world.","snake"))
print(convert("Hello, world.","kebab"))
print(convert("Hello, world.","pascal"))
print(convert("Hello, world.","uppercasesnake"))