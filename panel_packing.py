from typing import List, Dict, Tuple
import json

def calculate_panels(panel_width: int, panel_height: int, 
                     roof_width: int, roof_height: int) -> int:
    """
    Calcula la cantidad máxima de paneles enteros que caben en un techo,
    permitiendo rotación de los paneles, sin cortar paneles.
    """

    # Lista de espacios libres, cada espacio es (x, y, ancho, alto)
    free_spaces: List[Tuple[int, int, int, int]] = [(0, 0, roof_width, roof_height)]
    placed = 0  # contador de paneles colocados

    while True:
        placed_this_round = False

        for i, (x, y, w, h) in enumerate(free_spaces):
            # Intentar colocar panel sin rotar
            if panel_width <= w and panel_height <= h:
                placed += 1
                placed_this_round = True
                free_spaces.pop(i)
                # crear subespacios libres: derecha y abajo
                free_spaces.append((x + panel_width, y, w - panel_width, panel_height))  # derecha
                free_spaces.append((x, y + panel_height, w, h - panel_height))          # abajo
                break

            # Intentar colocar panel rotado
            elif panel_height <= w and panel_width <= h:
                placed += 1
                placed_this_round = True
                free_spaces.pop(i)
                free_spaces.append((x + panel_height, y, w - panel_height, panel_width))  # derecha
                free_spaces.append((x, y + panel_width, w, h - panel_width))             # abajo
                break

        if not placed_this_round:
            break  # ya no cabe ningún panel

    return placed


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]

    print("Corriendo tests:")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"],
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]

        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    run_tests()


if __name__ == "__main__":
    main()
