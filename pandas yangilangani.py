# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12mVhMA4lQUIncX72qZwvuoW4HFpTUac2
"""

import pandas as pd

# 1. DataFrame yaratish
data = {
    'Ism': ['Ali', 'Vali', 'Sardor', 'Komil'],
    'Yoshi': [25, 30, 22, 15],
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro', 'Andijan']
}
df = pd.DataFrame(data)

# 2. Ma'lumotlarni ko'rish
print(df)

# 3. Filtrlash
young_people = df[df['Yoshi'] < 30]
print("30 yoshdan kichiklar:\n", young_people)

old_people = df[df['Yoshi'] > 30]

if old_people.empty:
    print("30 yoshdan kattalar yo'q")
else:
    print("30 yoshdan kattalar:\n", old_people)

# 4. O'zgartirish
df['Yoshi'] += 1  # Har bir shaxsning yoshini 1 ga oshirish
print("Yangilangan DataFrame:\n", df)

# 5. CSV formatda saqlash
df.to_csv('data.csv', index=False)