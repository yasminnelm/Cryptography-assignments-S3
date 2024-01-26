text='gmyxzoocxziancxktanmyolupjrztgxwshctzluibuicyzwxyqtvqxzukibkotuxkagbknmimzzyajvjzampqyzloinoiqknaumbknknvkaiakgwtnilvvzvqydmvjcximrvzkilxzqtomrgqmdjrzyazvzmyjgkoaknkuiaivknvvy'
alphabet='abcdefghijklmnopqrstuvwxyz'

def IC(text):
    list=[]
    IC=0
    for j in range(len(alphabet)):
        nba=0
        for i in range(len(text)) :
            if text[i]==alphabet[j]:
                nba+=1
        list.append(nba*(nba-1))

    for i in range(len(list)):
        IC+=list[i]
    return IC/(len(text)*(len(text)-1))

#texte entier
print("cle=>une lettre")
print(IC(text))

#2 paragraphs
text2p1=""
text2p2=""
for i in range(87):
    text2p1="%s%s"%(text2p1,text[i])
    text2p2="%s%s"%(text2p2,text[i+87])
text2p2+='y'
print("cle=>2 lettres")
print("IC1=",IC(text2p1))
print("IC2=",IC(text2p2))


#3 paragraphs
text3p1=""
text3p2=""
text3p3=""
for i in range(58):
    text3p1="%s%s"%(text3p1,text[i])
    text3p2="%s%s"%(text3p2,text[i+58])
    text3p3="%s%s"%(text3p3,text[i+116])
text3p3+='y'

print("cle=>3 lettres")
print("IC1=",IC(text3p1))
print("IC2=",IC(text3p2))
print("IC3=",IC(text3p3))

#4 paragraphs
text4p1=""
text4p2=""
text4p3=""
text4p4=""
for i in range(43):
    text4p1="%s%s"%(text4p1,text[i])
    text4p2="%s%s"%(text4p2,text[i+43])
    text4p3="%s%s"%(text4p3,text[i+86])
    text4p4="%s%s"%(text4p4,text[i+129])
text4p4+='vvy'

print("cle=>4 lettres")
print("IC1=",IC(text4p1))
print("IC2=",IC(text4p2))
print("IC3=",IC(text4p3))
print("IC4=",IC(text4p4))

#5 paragraphs
text5p1=""
text5p2=""
text5p3=""
text5p4=""
text5p5=""
for i in range(35):
    text5p1="%s%s"%(text5p1,text[i])
    text5p2="%s%s"%(text5p2,text[i+35])
    text5p3="%s%s"%(text5p3,text[i+70])
    text5p4="%s%s"%(text5p4,text[i+105])
    text5p5="%s%s"%(text5p5,text[i+140])

print("cle=>5 lettres")
print("IC1=",IC(text5p1))
print("IC2=",IC(text5p2))
print("IC3=",IC(text5p3))
print("IC4=",IC(text5p4))
print("IC5=",IC(text5p5)) 


#6 paragraphs
text6p1=""
text6p2=""
text6p3=""
text6p4=""
text6p5=""
text6p6=""
for i in range(29):
    text6p1="%s%s"%(text6p1,text[i])
    text6p2="%s%s"%(text6p2,text[i+29])
    text6p3="%s%s"%(text6p3,text[i+58])
    text6p4="%s%s"%(text6p4,text[i+87])
    text6p5="%s%s"%(text6p5,text[i+116])
    text6p6="%s%s"%(text6p6,text[i+145])
text6p6+='y'
print("cle=>6 lettres")
print("IC1=",IC(text6p1))
print("IC2=",IC(text6p2))
print("IC3=",IC(text6p3))
print("IC4=",IC(text6p4))
print("IC5=",IC(text6p5))
print("IC6=",IC(text6p6))

            
