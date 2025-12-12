import math
def cube_volume(side: float = 1) -> float:
    """Объём куба: V = a³"""
    return side ** 3
def sphere_volume(radius: float = 1) -> float:
    """Объём сферы: V = 4/3 π r³"""
    return (4/3) * math.pi * radius ** 3
def pyramid_volume(base_area: float = 1, height: float = 1) -> float:
    """Объём пирамиды: V = 1/3 S h"""
    return  (1/3) * base_area * height
def cylinder_volume(radius: float = 1, height: float = 1) -> float:
    """Объём цилиндра: V = π r² h"""
    return math.pi * radius ** 2 * height
