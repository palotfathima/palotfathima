def min_positive(l1):
  i=0
  count=0
  while i<len(l1):
    if type(i[l1]) != int:
      raise ValueError
      break
    else:
      i+=1
  i=0
  l2=[]
  while i<len(l1):
    if l1[i]>0:
      l2.append(l1[i])
    i+=1
  if i==0:
    raise ValueError
  return min(l2)   
    
  
    
      



        
      
