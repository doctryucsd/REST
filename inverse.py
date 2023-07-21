from __future__ import annotations
from typing import List, Tuple
import sys

def read_file(path: str) -> List[List[Tuple[float, float]]]:
    ret: List[List[Tuple[float, float]]] = []
    with open(path, "r") as f:
        while(line:=f.readline().split(" ")):
            if len(line) < 2:
                break
            assert len(line) % 2 == 0, len(line)
            point_set: List[Tuple[float, float]] = []
            num_points: int = len(line) // 2
            for point_id in range(num_points):
                x: float = float(line[point_id * 2])
                y: float = float(line[point_id * 2 + 1])
                point_set.append((x, y))
            ret.append(point_set)
    return ret

def main() -> None:
    point_sets: List[List[Tuple[float, float]]] = read_file(sys.argv[1])
    print(point_sets[3])

if __name__ == "__main__":
    main()