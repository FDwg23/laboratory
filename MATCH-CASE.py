from Фигуры import sphere_volume, pyramid_volume


def main_program():
    print("Доступные фигуры: куб, сфера, пирамида, цилиндр")
    figure_funcs = {
        "куб": ( cube_volume, ["side"]),
        "сфера": (sphere_volume, ["radius"]),
        "пирамида": (pyramid_volume, ["base_area", "height"]),
        "цилиндр": ( cylinder_volume, ["radius", "height"])
    }
    figure = input("\nВведите название фигуры: ").strip().lower()
    if figure not in figure_funcs:
        print(f"Ошибка: фигура '{figure}' не поддерживается")
        return
    func, params = figure_funcs[figure]
    kwargs = {}
    for param in params:
        value = input(f"Введите {param} (Enter для значения по умолчанию=1): ").strip()
        kwargs[param] = float(value) if value else 1
    volume = func(**kwargs)
    print(f"Объём {figure}: {volume:.4f}")