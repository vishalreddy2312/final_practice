import names
from gender_detector import gender_detector as gd
from random import *



# Randomly generating people information
def generate_people_info():
    name= names.get_first_name()  # Generating random names

    detector= gd.GenderDetector('us')
    gender = detector.guess(name)     # Detection of genders corresponding to the random names
    if gender == 'unknown':
        gender = 'male'

    age = randint(1,95)     # Randomly generating age

    item = [0,1]
    x = sample(item,1)
    corona = x[0]        # Randomly generating corona postive or not

    people_info = [name,gender,age,corona]
    return people_info

def finding_victims(adjacent_grid,victim_name,victim_count,time_step,vic_plot):
    y = []
    for x in adjacent_grid:
        if x[3] == 0:
            x[3] = 1
            y.append(x[0])
            victim_name.append(x[0])
    victim_count = victim_count + len(y)
    vic_plot.append(len(y))

    print("At time step {} the victims are: {}".format(time_step, y))
    return victim_name, victim_count, vic_plot



def grid_analysis(grid, height, width):
    print("================= Start Analysis ===================")
    time_step = 0
    victim_count = 0
    vic_plot = []
    victim_name = []
    for i in range(height):
        for j in range(width):
            time_step = time_step+1
            temp_list = grid[i][j]
            if temp_list[3] == 1:
                if i == 0 and j == 0:
                    adjacent_grid = [grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif i == height-1 and j == 0:
                    adjacent_grid = [grid[i][j + 1], grid[i - 1][j], grid[i - 1][j + 1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif i == 0 and j == width-1:
                    adjacent_grid = [grid[i][j - 1], grid[i + 1][j], grid[i + 1][j - 1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif i == height-1and j == width-1:
                    adjacent_grid = [grid[i][j - 1], grid[i - 1][j], grid[i - 1][j - 1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif j == 0:
                    adjacent_grid = [grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1], grid[i-1][j], grid[i-1][j+1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif j == width-1:
                    adjacent_grid = [grid[i][j - 1], grid[i + 1][j], grid[i + 1][j - 1], grid[i - 1][j], grid[i+1][j-1]]
                    victim_name, victim_count,vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif i == 0:
                    adjacent_grid = [grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1], grid[i][j-1], grid[i + 1][j - 1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                elif i == height-1:
                    adjacent_grid = [grid[i][j + 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j-1], grid[i - 1][j - 1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
                else:
                    adjacent_grid = [grid[i][j + 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1], grid[i - 1][j - 1], grid[i+1][j], grid[i+1][j+1], grid[i+1][j-1]]
                    victim_name, victim_count, vic_plot = finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
    return grid, victim_name, victim_count, vic_plot, time_step









if __name__=='__main__':

    width = int(input("Enter the width of grid : "))  # Getting the width of  grid from the User
    height = int(input("Enter the height of grid : "))  # Getting the height of  grid from the User

    # Generating the grid
    grid = []
    for j in range(height):
        row = []
        for i in range(width):
            row.append(generate_people_info())
        grid.append(row)
    print("============The generated grid================ ")
    for i in range(height):
        print(grid[i])

    # Calculating the number of people already affected
    count_affected = 0
    affected_name_list = []
    for i in range(height):
        for j in range(width):
            temp_list = grid[i][j]
            if temp_list[3] == 1:
                count_affected = count_affected+1
                affected_name_list.append(temp_list[0])

    print("==========The total number of people already affected===========")
    print(count_affected)
    print("==========People already affected================:")
    for x in affected_name_list:
        print(x)
    # After analysis
    new_grid, victim_name, victim_count, vic_plot, time_step = grid_analysis(grid, height, width)
    print("==========The total number of people having higher chance of getting affected===========")
    print(victim_count)
    print("==========People having higher chance of getting affected================:")
    for x in victim_name:
        print(x)

