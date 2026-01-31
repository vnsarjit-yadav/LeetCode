# # li=[2,4,3,24,32,45]
# # li.append(56)
# # li.insert(0,10)
# # li.extend([12,13])
# # print(li)
# # li.pop(5)
# # del li[3]
# # li.remove(2)
# # li.clear()
# # print(li)
# # li.append(56)
# # li.insert(0,10)
# # li.extend([12,13])
# # print(li)
# # print(li.count(2),max(li),min(li),sum(li))
# # li.sort(reverse=True)
# # print(li)
# st={3,8,4,6}

# print(type(st))
# st.add(2)
# st.pop()
# # st.remove(8)
# # st.discard(60)
# # st.update([10])
# print(st,st.discard(60),st.pop())
# # dit={'name':{'n1':'anuj','n2':'vivek','n3':'sachin','n4':'aadesh'},'cast':'obc','age':20}
# # print(dit.get('name'),dit.values(),dit.keys(),dit.items(),dit.update({'name':'male'}),dit.pop('name'))
# # print(dit['name']['n1'])
with open("simle.py","r") as file:
    with open("simpel.txt","w") as file1:
        file_content=file.readlines()
        file1.writelines(file_content)

        