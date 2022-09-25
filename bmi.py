# -*- coding: utf-8 -*-

vikt = float(input('Ange din vikt i kg: '))
l = float(input('Ange din längd i meter: '))
l2 = l**2
bmi = float(vikt/l2)
bmi = round(bmi,2)

print ('Ditt BMI är: '  +str(bmi))
if bmi < 18.5:
    print('Viktklass: Undervikt')
if 18.5 < bmi < 24.9:
    print('Viktklass: Normalvikt')
if 25 < bmi < 29.9:
    print('Viktklass: Övervikt')
if 30 < bmi < 34.9:
    print('Viktklass: Fetma Grad 1')
if 35 < bmi < 39.9:
    print('Viktklass: Fetma Grad 2')
if bmi > 40:
    print('Viktklass: Fetma grad 3')
