"""
13. feladat – Kör
A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!
"""

# kör terület számítása: 2 × r × pí
# kör terület képlete: r2 × pí

import math


def kor():
    kor_sugara = float(input("Kérem, adja meg egy kör sugarát! "))
    eredmeny_kerulet = round(2 * kor_sugara * math.pi, 2)
    eredmeny_terulet = round(kor_sugara ** 2 * math.pi, 2)
    if eredmeny_kerulet >= 0 and eredmeny_terulet >= 0:
        print("A kör kerülete: " + str(eredmeny_kerulet))
        print("A kör területe: " + str(eredmeny_terulet))
    else:
        eredmeny_kerulet < 0 and eredmeny_terulet < 0
        print("Hiba: a kör sugara nem pozitív!")
