from __future__ import annotations
import sys
from typing import List, Tuple
import multiprocessing as mp
import os

def get_files(dir: str) -> List[str]:
    files: List[str] = os.listdir(dir)
    files = sorted(files)
    files = [os.path.join(dir, file) for file in files]

    return files

def read_points(file: str) -> List[Tuple[int, int]]:
    ret: List[Tuple[int, int]] = []
    with open(file, "r") as f:
        while(line:= f.readline().split()):
            assert len(line) == 2, line
            x: int = int(line[0])
            y: int = int(line[1])
            query: Tuple[int, int] = (x, y)
            if query not in ret:
                ret.append((x, y))
    return ret

def int2float(points: List[Tuple[int, int]]) -> List[Tuple[float, float]]:
    x_list: List[int] = [point[0] for point in points]
    y_list: List[int] = [point[1] for point in points]
    x_max: int = max(x_list)
    y_max: int = max(y_list)
    base: int = max(x_max, y_max) + 1
    ret: List[Tuple[float, float]] = [(point[0]/base, point[1]/base) for point in points]
    return ret

def worker(file: str) -> List[Tuple[float, float]]:
    points: List[Tuple[int, int]] = read_points(file)
    ret: List[Tuple[float, float]] = int2float(points)
    return ret

def get_point_sets(dir: str) -> List[List[Tuple[float, float]]]:
    files: List[str] = get_files(dir)
    with mp.Pool() as pool:
        point_sets: List[List[Tuple[float, float]]]= pool.map(worker, files)
    return point_sets

def write_file(point_sets: List[List[Tuple[float, float]]], file_name: str) -> None:
    with open(file_name, "w") as f:
        for point_set in point_sets:
            for point in point_set:
                f.write(f"{point[0]} {point[1]} ")
            f.write("\n")

def main() -> None:
    dir_name: str = sys.argv[1]
    output_name: str = sys.argv[2]
    point_sets: List[List[Tuple[float, float]]] = get_point_sets(dir_name)
    write_file(point_sets, output_name)

if __name__ == "__main__":
    main()