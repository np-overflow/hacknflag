#!/usr/bin/env python3

mazes_file = open('map.txt', 'r')

mazes_lines = [[]]
start_pos = [0, 1]
directions = {
    'W': (0, -1),
    'A': (-1, 0),
    'S': (0, 1),
    'D': (1, 0),
}
maze_no = 0
for line in mazes_file:
    if 'END' not in line:
        mazes_lines[maze_no].append(
            list(line.strip('\n').replace('-', '+').replace('|', '+')))
    else:
        maze_no += 1
        mazes_lines.append([])


def get_surrounding_path(pos, maze):
    curr_x = pos[0]
    curr_y = pos[1]
    mini_map = []
    for y in range(0, 3):
        mini_map.append([])
        final_y = curr_y + y - 1
        for x in range(0, 3):
            final_x = curr_x + x - 1
            verdict = bounds_check((final_x, final_y), maze)
            if verdict[0] or verdict[1]:
                mini_map[y].append('+')
                continue
            if final_x == curr_x and final_y == curr_y:
                mini_map[y].append('o')
                continue
            mini_map[y].append(maze[final_y][final_x])
        mini_map[y] = ' '.join(mini_map[y])
    return '\n'.join(mini_map)


def bounds_check(final_pos, maze):
    # Check if final x/y pos is out of bound
    verdict = [False, False]
    if final_pos[0] >= len(maze[0]) or final_pos[0] < 0:
        verdict[0] = True
    if final_pos[1] >= len(maze) or final_pos[1] < 0:
        verdict[1] = True
    return verdict


def move_player(direction, curr_pos, maze):
    final_x = curr_pos[0] + direction[0]
    final_y = curr_pos[1] + direction[1]
    verdict = bounds_check((final_x, final_y), maze)
    if verdict[0] or verdict[1] or maze[final_y][final_x] == "+":
        return None, -1
    else:
        return (final_x, final_y), 1


def play_game():
    print("Type W,A,S or D to move up, left, down or right respectively. The end of the maze has a '!' mark!", flush=True)
    print(get_surrounding_path(start_pos, mazes_lines[0]), flush=True)
    while True:
        entered_input = input(
            "Key in the next move!\n").upper()[:1]
        while entered_input not in directions:
            print("Oh no the input is invalid. Try again!")
            print(get_surrounding_path(start_pos, mazes_lines[0]))
            entered_input = input("Key in next position\n").upper()[:1]
        chosen_dir = directions[entered_input]
        res, err = move_player(chosen_dir, start_pos, mazes_lines[0])
        if err == -1:
            print('You can\'t go there. Sorry!')
            print(get_surrounding_path(start_pos, mazes_lines[0]))
        else:
            start_pos[0] += chosen_dir[0]
            start_pos[1] += chosen_dir[1]
            print(get_surrounding_path(start_pos, mazes_lines[0]))
            if mazes_lines[0][start_pos[1]][start_pos[0]] == '!':
                print("You won!! Here's a flag!!")
                print("HNF{Th0M4s_woU1D_b3_pR0uD!}")
                break


play_game()
