"""
5. feladat – HónapNév
A program  olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma! A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba esetén legyen hibaüzenet!
"""

def honap_nev():
    szam = int(input("Kérem, adjon meg egy egész számot! "))
    if szam >= 1 and szam <= 12:
        if szam == 1:
            print("1. Január")
        elif szam == 2:
            print("2. Február")
        elif szam == 3:
            print("3. Március")
        elif szam == 4:
            print("4. Április")
        elif szam == 5:
            print("5. Május")
        elif szam == 6:
            print("6. Június")
        elif szam == 7:
            print("7. Július")
        elif szam == 8:
            print("8. Augusztus")
        elif szam == 9:
            print("9. Szeptember")
        elif szam == 10:
            print("10. Október")
        elif szam == 11:
            print("11. November")
        elif szam == 12:
            print("12. December")
    else:
        print("Hiba! Nem létező hónap sorszáma!")
