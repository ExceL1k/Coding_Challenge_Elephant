with open("input.txt") as file_handler:
    matrix = None
    result_file_name = 'result.txt'
    for line in file_handler:
        lower_line = line.lower()
        if 'c' in lower_line:
            mass_x_y = lower_line.split(' ')
            dx = int(mass_x_y[1])
            dy = int(mass_x_y[2]) + 2
            matrix = [[0 for x in range(dx)] for y in range(dy)]
            for i in range(dy):
                if i == 0 or i == dy - 1:
                    for j in range(dx):
                        matrix[i][j] = '-'
                else:
                    matrix[i][0] = '|'
                    for j in range(1, dx-1):
                        matrix[i][j] = ' '
                    matrix[i][dx-1] = '|'

            with open(result_file_name, 'w') as file_write:
                for i in range(dy):
                    for j in range(dx):
                        file_write.write(matrix[i][j])
                    file_write.write('\n')

        elif 'l' in lower_line and matrix:
            mass_x_y = lower_line.split(' ')
            x1 = int(mass_x_y[1])
            y1 = int(mass_x_y[2])
            x2 = int(mass_x_y[3])
            y2 = int(mass_x_y[4])

            if y1 == y2:
                for i in range(x1, x2 + 1):
                    matrix[y1][i] = 'x'

                with open(result_file_name, 'a') as file_write:
                    for i in range(dy):
                        for j in range(dx):
                            file_write.write(matrix[i][j])
                        file_write.write('\n')

            elif x1 == x2:
                for i in range(y1, y2 + 1):
                    matrix[i][x1] = 'x'

                with open(result_file_name, 'a') as file_write:
                    for i in range(dy):
                        for j in range(dx):
                            file_write.write(matrix[i][j])
                        file_write.write('\n')

        elif 'r' in lower_line and matrix:
            mass_x_y = lower_line.split(' ')
            x1 = int(mass_x_y[1])
            y1 = int(mass_x_y[2])
            x2 = int(mass_x_y[3])
            y2 = int(mass_x_y[4])

            for i in range(y1, y2 + 1):
                matrix[i][x1] = 'x'
                matrix[i][x2 - 1] = 'x'

            for i in range(x2 - x1):
                matrix[y1][x1 + i] = 'x'
                matrix[y2][x2 - i -1] = 'x'

            with open(result_file_name, 'a') as file_write:
                for i in range(dy):
                    for j in range(dx):
                        file_write.write(matrix[i][j])
                    file_write.write('\n')

        elif 'b' in lower_line and matrix:
            mass_x_y = lower_line.split(' ')
            x1 = int(mass_x_y[1])
            y1 = int(mass_x_y[2])
            color = mass_x_y[3].strip()

            for i in range(y1 + 1):
                for j in range(x1, len(matrix[i])):
                    if matrix[i][j] == 'x' or matrix[i][j] == '|' or matrix[i][j] == '-':
                        break
                    matrix[i][j] = color

                for j in range(x1, -1, -1):
                    if matrix[i][j] == 'x' or matrix[i][j] == '|' or matrix[i][j] == '-':
                        break
                    matrix[i][j] = color

            with open(result_file_name, 'a') as file_write:
                for i in range(dy):
                    for j in range(dx):
                        file_write.write(matrix[i][j])
                    file_write.write('\n')

        elif not matrix:
            print("You don't create canvas")
            break

print('Done')

