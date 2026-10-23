"""Учебная программа для поэтапного изучения Git."""


def read_integer(prompt: str) -> int:
    """Повторяет запрос, пока пользователь не введет целое число."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число, например -5 или 12.")


def main() -> None:
    print("Привет! Это учебный калькулятор.")
    first = read_integer("Введите первое целое число: ")
    second = read_integer("Введите второе целое число: ")
    print(f"Первое число: {first}; второе число: {second}")


if __name__ == "__main__":
    main()
