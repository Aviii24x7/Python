

def check_palindrome(my_str):
    if my_str==my_str[::-1]:
        return True
    else:
        return False

def cutout_string(my_string,i_index):
    my_list = []
    for f_index in range(i_index+1,len(my_string)):
        if my_string[i_index] == my_string[f_index]:
            my_list.append(f_index)
    return my_list

name= input('ENTER THE STRING:')

end_list=cutout_string(name,0)
slice_str=[]
for f in end_list:
    slice_str.append(name[0,f])

for st in slice_str:
    if check_palindrome(st):
        print(st)





        
        







