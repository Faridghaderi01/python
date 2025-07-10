text = "Hi, I'm Farid and I'm glad to see you. This is a compression program that I wrote and I hope you enjoy it"
# ---------------------------------------------------------------------------------------------------------------------------------
#                                     Counting the letters of the text
# -------------------------------------------------------------------------------------------------------------------------------
Counter_dictionary = {}
c = 1    #Counter
for i in text:
    if i in Counter_dictionary:
        Counter_dictionary[i] += 1
    else:
        new_dict = {i : c }
        Counter_dictionary.update(new_dict)   
print(Counter_dictionary)  
print("__________________________________________________________________________________")  
# ---------------------------------------------------------------------------------------------------------------------------------------
#                              Sort the dictionary in ascending order
# ------------------------------------------------------------------------------------------------------------------------------------------
sort_orders = sorted(Counter_dictionary.items(), key=lambda x: x[1], reverse=True)
dict_key = []
dict_value = []
for i in sort_orders:
    dict_key.append(i[0])
    dict_value.append(i[1])

print('The value of variables is equal to--->',dict_value,'')
print("------------------------------------------------------------------------------------")
print('The key is equal to---->',dict_key,'')
# ------------------------------------------------------------------------------------------------------------------------------------------
#                                Program coding and compression
# --------------------------------------------------------------------------------------------------------------------------------
zip_text = ''
zip_dict = {}
for i in dict_key:
    if i == dict_key[0]:
        new_dict = {i : 0 }
        zip_dict.update(new_dict) 
        zip_text += str(0)
    else:
        c = i
        byte_data = c.encode('utf-8')
        new_dict = {i : byte_data[0] }
        zip_dict.update(new_dict)
        zip_text += str(byte_data[0])
print('The coded dictionary is equal to---->',zip_dict,'')
print("---------------------------------------------------------------------------------------------------------")
print('The compressed code and text is equal to--->',zip_text,'')