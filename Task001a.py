# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
n = int(input("Введите сколько км машина проезжает за день: "))
m = int(input("Введите сколько км ноужно проехать: "))
t = int((2 * m - 1) / n);
print(f"{m} км машина проедет за {t} день/дня/дней.")
