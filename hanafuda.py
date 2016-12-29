import numpy as np
import sys

# Input
idata_list=[]
while 1:
    idata=int(raw_input())
    if idata==0:
        idata_list.append(0)
        idata_list.append(0)
        break
    else:
        idata_list.append(idata)

## 1D==> x * 2
idata_np=np.array(idata_list)
data_length=len(idata_list)
idata_np=idata_np.reshape(data_length/2,2)

print idata_np

#idata[0]=sors of n,[1]=cut time
#hanahuda time

hanafuda=np.arange(1,idata_np[0,0]+1)
hanafuda=hanafuda[::-1] #reverse
cut_time=idata_np[0,1]
for ct in range(1,cut_time+1):
    print hanafuda
    p=idata_np[ct,0]
    c=idata_np[ct,1]# ct + t  t:hanafudauda play time
    c_work_space=hanafuda[p-1:p-1+c]
    front_fuda=hanafuda[0:p]
    back_fuda=hanafuda[p+c:]
    hanafuda=np.hstack([c_work_space,front_fuda,back_fuda])
    print hanafuda
    print c_work_space,front_fuda,back_fuda
