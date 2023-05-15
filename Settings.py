a = [48.91, 47.05, 48.29]
sum_a = sum(a)
mean_a = sum_a / len(a)
b = [50.23, 49.01, 46.2]
sum_b = sum(b)
mean_b = sum_b / len(b)
c = [47.27, 47.5, 48.69]
sum_c = sum(c)
mean_c = sum_c / len(c)
d = [45.74, 45.67, 44.09]
sum_d = (sum(d))
mean_d = sum_d / len(d)
grand_val = a + b + c + d
total_n = len(a + b + c + d)
SSt = float(0)
gmean = ((sum_a + sum_b + sum_c + sum_d) / total_n)
print(total_n)
print(gmean)

for i in grand_val:
    e = ((i - gmean)**2)
    SSt += e

print(SSt)

SSw = float(0)
SSa = float(0)
SSb = float(0)
SSc = float(0)
SSd = float(0)
for i in a:
    f = ((i - mean_a)**2)
    SSw += f
    SSa += f
for i in b:
    f = ((i - mean_b)**2)
    SSw += f
    SSb += f
for i in c:
    f = ((i - mean_c)**2)
    SSw += f
    SSc += f
for i in d:
    f = ((i - mean_d)**2)
    SSw += f
    SSd += f

print(SSa)
print(SSb)
print(SSc)
print(SSd)
dfb = 3
dfw = 8
SSb = SSt - SSw
MSb = SSb / dfb
MSw = SSw / dfw
Fcal = MSb / MSw
print("SSt is", SSt)
print("SSw is", SSw)
print("SSB is", SSb)
print("MSb is", MSb)
print("MSw is", MSw)
print("F is", Fcal)