# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

n = int(input("Введите общее количество журавликов: "))
nPetya = n // 6
nKatya = nPetya * 4
nSerg = n - nPetya - nKatya
print(f"Петя сделал {nPetya} журавликов, Катя сделала {nKatya} журавликов, Сергей сделал {nSerg} журавликов.")
