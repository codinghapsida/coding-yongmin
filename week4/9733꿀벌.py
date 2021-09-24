import sys
task = []
dict = {'Re':0, 'Pt':0, 'Cc':0, 'Ea':0, 'Tb':0, 'Cm':0, 'Ex':0}

for i in range(24):
    s = input().split()
    if(s==''): break
    task.extend(s)
    if(len(task)==24): break

for i in task:
    if i in dict:
        dict[i] += 1

l = len(task)

for i in dict:
    print(f'{i} {dict[i]} {dict[i]/l:.2f}')
print(f'Total {l} 1.00')

