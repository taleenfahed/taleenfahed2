# str='amaama'
# num=len(str)//2
# n1=str[0:num]
# n2=str[num:0]
# if n1==n2:
#     print('symmetrical')
def sym(s1):
 str=s1
 num=len(str)//2
 n1=str[0:num]
 n2=str[num:0]
 if n1==n2:
    print('symmetrical')


sym('menmen')
sym('movemove')


