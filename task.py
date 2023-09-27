import csv

print("Введите путь к файлу, оканчивающийся на самом файле.")
p=input()
print("Введите номер ряда.")
l=int(input())
print("Введите номер колонки.")
c=int(input())
with open(p) as f:
    data=list(csv.reader(f))
    print(data[l][c])
