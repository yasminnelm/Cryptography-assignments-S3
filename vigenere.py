texte='zbpuevpuqsdlzgllksousvpasfpddggaqwptdgptzweemqzrdjtddefekeferdprrcyndgluaowcnbptzzzrbvpssfpashpncotemhaeqrferdlrlwwertlussfikgoeuswotfdgqsyasrlnrzppdhtticfrciwurhcezrpmhtpuwiyenamrdbzyzwelzucamrptzqseqcfgdrfrhrpatsepzgfnaffisbpvblisrplzgnemswaqoxpdseehbeeksdptdttqsdddgxurwnidbdddplncsd'
p1=""
p2=""
p3=""
p4=""
for i in range(71):
    p1="%s%s"%(p1,texte[i])
    p2="%s%s"%(p2,texte[i+72])
    p3="%s%s"%(p3,texte[i+143])
    p4="%s%s"%(p4,texte[i+214])
p4="%s%s"%(p4,'d')
print(p1)
print(p2)
print(p3)
print(p4)
