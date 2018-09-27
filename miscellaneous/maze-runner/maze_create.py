mazes_file = open('test.txt', 'r')

mazes_lines = []
start_pos = (0, 1)
for line in mazes_file:
    if 'END' not in line:
        mazes_lines.append(
            list(line.strip('\n').replace('-', '+').replace('|', '+')))


def get_surrounding_path(pos, maze):
    curr_x = pos[0]
    curr_y = pos[1]
    mini_map = []
    for y in range(-1, 2):
        mini_map.append([])
        final_y = curr_y + y
        for x in range(-1, 2):
            final_x = curr_x + x
            if final_x < 0 or final_x > len(maze) or final_y < 0 or final_y > len(maze):
                mini_map[final_y].append('+')
                continue
            mini_map[final_y].append(maze[final_y][final_x])
        mini_map[final_y] = ' '.join(mini_map[final_y])

    return '\n'.join(mini_map)
