import sys

def is_weak_vertex(vertex, adjacency_list):
    for neighbor in adjacency_list[vertex]:
        for candidate in adjacency_list[neighbor]:
            if candidate != vertex and candidate in adjacency_list[vertex] and candidate in adjacency_list[neighbor]:
                return False
    return True

def find_weak_vertices(vertex_count, input_lines):
    adjacency_list = {}
    for i in range(vertex_count):
        row = input_lines[i].strip().split()
        adjacency_list[i] = {index for index, val in enumerate(row) if val == '1'}

    weak_vertices = [v for v in range(vertex_count) if is_weak_vertex(v, adjacency_list)]
    print(' '.join(map(str, weak_vertices)))

input_lines = sys.stdin.read().strip().split('\n')
line_index = 0
while True:
    if line_index >= len(input_lines):
        break
    vertex_count = int(input_lines[line_index])
    line_index += 1
    if vertex_count == -1:
        break
    find_weak_vertices(vertex_count, input_lines[line_index:line_index + vertex_count])
    line_index += vertex_count
