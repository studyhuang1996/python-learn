dict1={'x':7,'y':4,'z':5}
print(type(dict1))
dict1['x'] =3

print(dict1)


a_list=[]
for i in range(1,11):
    if(i%2 == 0):
        a_list.append(i*i)
print(a_list)

b_list = [i*i for i in range(1,11) if(i%2==0)]

print(b_list)