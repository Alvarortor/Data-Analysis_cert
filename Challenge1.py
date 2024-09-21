

import numpy as np



#make  3x3 array using a list of 9 numbers
#This could probably be cool with a user input for numbers tbh
in_list = [0,1,2,3,4,5,6,7,8]

#Output lists
mean =[]
vari = []
stdev = []
MX = []
MN = []
SM = []

#Give each list a pretty introduction


#Turn list into array and mold into shape we want
a = np.array(in_list).reshape(3,3) 

#Loop with the axis we want 2 is a placeholder for entire array
axis = [0,1,2]

def calculate(a):
    if (a.size < 9):

        raise ValueError ("List must contain nine numbers.")
    for ax in axis:
        if ax == 2:
            men = np.mean(a)
            var = np.var(a)
            std = np.std(a)
            mx = np.max(a)
            mn = np.min(a)
            sm= np.sum(a)
        else:    
            men = np.mean(a, axis = ax)
            var = np.var(a,axis = ax)
            std = np.std(a, axis= ax)
            mx = np.max(a,axis = ax)
            mn = np.min(a,axis = ax)
            sm = np.sum(a,axis = ax)
            
        #Convert into lists    
        men_l = men.tolist()
        var_l = var.tolist()
        std_l = std.tolist()
        mx_l = mx.tolist()
        mn_l = mn.tolist()
        sm_l = sm.tolist()     

        
        mean.append(men_l)
        vari.append(var_l)
        stdev.append(std_l)
        MX.append(mx_l)
        MN.append(mn_l)
        SM.append(sm_l)
        
#Run function on dataset a
calculate(a)

#Get outputs
print("'mean'", ': ', mean) 
print("'variance'", ': ', vari)
print("'standard deviation'", ': ', stdev)
print("'max'", ': ', MX)
print("'min'", ': ', MN)
print("'sum'", ': ', SM)
    






