def min_positive(l1):
  i=0
  count=0
  while i<len(l1):
    if type(l1[i]) != int:
      raise ValueError
    else:
      i+=1
  i=0
  l2=[]
  while i<len(l1):
    if l1[i]>0:
      l2.append(l1[i])
    i+=1
  if len(l2)==0:
    raise ValueError
  return min(l2)   
    
  
    
      



        
      
