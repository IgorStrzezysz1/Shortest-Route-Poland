
import heapq

# Miasta i przykładowe odległości drogowe w kilometrach
graf = {
    "Warszawa": {
        "Łódź": 130,
        "Kraków": 300,
        "Gdańsk": 340,
        "Poznań": 310
    },
    "Łódź": {
        "Warszawa": 130,
        "Wrocław": 220,
        "Poznań": 200,
        "Kraków": 220
    },
    "Kraków": {
        "Warszawa": 300,
        "Łódź": 220,
        "Wrocław": 270
    },
    "Gdańsk": {
        "Warszawa": 340,
        "Poznań": 300
    },
    "Poznań": {
        "Warszawa": 310,
        "Łódź": 200,
        "Gdańsk": 300,
        "Wrocław": 180
    },
    "Wrocław": {
        "Łódź": 220,
        "Kraków": 270,
        "Poznań": 180
    }
}


def najkrotsza_trasa(start, cel):
    kolejka = [(0, start, [start])]
    odleglosci = {start: 0}

    while kolejka:
        dystans, miasto, trasa = heapq.heappop(kolejka)

        if dystans > odleglosci[miasto]:
            continue

        if miasto == cel:
            return dystans, trasa

        for sasiad, odleglosc in graf[miasto].items():
            nowy_dystans = dystans + odleglosc

            if nowy_dystans < odleglosci.get(
                sasiad, float("inf")
            ):
                odleglosci[sasiad] = nowy_dystans
                heapq.heappush(
                    kolejka,
                    (nowy_dystans, sasiad, trasa + [sasiad])
                )

    return None, []


print("=== NAJKRÓTSZA TRASA W POLSCE ===")
print("\nDostępne miasta:")
print(", ".join(graf.keys()))

start = input("\nPodaj miasto początkowe: ").strip().title()
cel = input("Podaj miasto docelowe: ").strip().title()

if start not in graf or cel not in graf:
    print("Błąd: Nie znaleziono podanego miasta!")
else:
    dystans, trasa = najkrotsza_trasa(start, cel)

    if dystans is not None:
        print("\nNajkrótsza trasa:")
        print(" -> ".join(trasa))
        print(f"Długość trasy: {dystans} km")
    else:
        print("Nie znaleziono trasy.")
