def find_largest_integer(k):
    list_k=list(k)
    #finding largest number
    largest_ind=-1
    for i  in range(len(list_k)-1):
        if list_k[i]>list_k[i+1]:
            largest_ind=i
            break
  
    # finding secind largest number
    second_largest=-1
    for i in range(largest_ind+1,len(list_k)):  
        if second_largest==-1 and list_k[i]<list_k[largest_ind]: 
            second_largest=i
            
        elif second_largest>-1 and list_k[i]<list_k[largest_ind] and list_k[second_largest]<= list_k[i]:
    
            second_largest=i

    if largest_ind ==-1:
        return k
    else:
        list_k[largest_ind],list_k[second_largest]=list_k[second_largest],list_k[largest_ind]
        
    result="".join(list_k)
    return result