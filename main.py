# 29-masala
dict1 = {
    "a": 5,
    "b": 9,
    "c": 7
}
dict2 = {
    "a": 7,
    "d": 3,
    "c": 4
}
natija = dict1.copy()
for k, v in dict2.items():
    if k in natija:
        natija[k] += v
    else:
        natija[k] = v

print(natija)
# 30-masala
dict = {
    "a": 1,
    "b": 2,
    "c": 1,
}

new_dict = {}
for k, v in dict.items():
    new_dict[v] = k

print(new_dict)
# 31-masala
text = "salom python yaxshi va zor python salom zor python"
words = text.split()

dict = {}
for w in words:
    dict[w] = dict.get(w, 0) + 1

top3 = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:3]

print(dict)
print(top3)
# 32-masala
dict = {
    "a": 10,
    "b": 5,
    "c": 20,
    "d": 3
}
limit = 7

new_dict = {k: v for k, v in dict.items() if v > limit}

print(new_dict)
# 33-masala
oquvchilar = {
    "Ali": 95,
    "Vali": 82,
    "Hasan": 74,
    "Husan": 65,
    "Olim": 50
}

baholar = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": []
}

for ism, natija in oquvchilar.items():
    if natija >= 90:
        baholar["A"].append(ism)
    elif natija >= 80:
        baholar["B"].append(ism)
    elif natija >= 70:
        baholar["C"].append(ism)
    elif natija >= 60:
        baholar["D"].append(ism)
    else:
        baholar["F"].append(ism)

print(baholar)
# 34-masala
narx = {
    "olma": 3000,
    "banan": 5000,
    "nok": 4000
}
miqdori = {
    "olma": 2,
    "banan": 3
}

jami = {}

for mahsulot in narx:
    if mahsulot in miqdori:
        jami[mahsulot] = narx[mahsulot] * miqdori[mahsulot]

print(jami)
# 35-masala
d = {'banana': 3, 'apple': 5, 'cherry': 2}

sorted_dict = dict(sorted(d.items()))

print(sorted_dict)
