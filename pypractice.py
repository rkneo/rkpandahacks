def find_missing_element(elements):
    len_e = len(elements)
    sum_acc_element = 0
    sum_element = 0

    for i in range(len_e):
        sum_acc_element += elements[i]
    
    max_ele = elements[len(elements)-1] + 1

    for i in range(max_ele):
        sum_element += i 
    print(f"missing element {sum_element - sum_acc_element}") 

if __name__ =="__main__":
    elements = [1,2,3,4,5,7,8]
    find_missing_element(elements)


    
