arr = [1,2,3,4,5,6,7,8,9]
par_elm = []
not_par = []

for i in range (len(arr)):
    if arr[i] % 2 == 0:
        par_elm.append(arr[i])
    if arr[i] % 2 == 1:
        not_par.append(arr[i])

sum = 0
for i in range(len(par_elm)):
    sum += par_elm[i]

sum = 0
for i in range(len(not_par)):

    sum += not_par[i]

print(f"сума елементів {par_elm} = {sum}")
print(f"сума елементів {not_par} = {sum}")

print(f"{par_elm} \n{not_par}")
