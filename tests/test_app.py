from app import*

import pytest


def test_general_people_info():
    assert covid_G2.generate_people_info() is not None


def test_grid_analysis():
    height = 3
    width = 3
    grid = []
    for j in range(height):
        row = []
        for i in range(width):
            row.append(covid_G2.generate_people_info())
        grid.append(row)
    new_grid, victim_name, victim_count, vic_plot, time_step = covid_G2.grid_analysis(grid, height, width)
    def test_sub_1(new_grid, victim_name, victim_count, vic_plot, time_step):
        return True if new_grid != [] and victim_name != [] and victim_count  != 0 and vic_plot  != [] and time_step != 0 else False
    assert test_sub_1(new_grid, victim_name, victim_count, vic_plot, time_step) is True

def test_finding_victims():
    height = 3
    width = 3
    grid = []
    for j in range(height):
        row = []
        for i in range(width):
            row.append(covid_G2.generate_people_info())
        grid.append(row)
    i = 0
    j = 0
    time_step = 1
    victim_count = 0
    vic_plot = []
    victim_name = []
    adjacent_grid = [grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
    victim_name, victim_count, vic_plot = covid_G2.finding_victims(adjacent_grid, victim_name, victim_count, time_step, vic_plot)
    def test_sub_2( victim_name, victim_count, vic_plot):
        return True if victim_name != [] and victim_count != 0 and vic_plot != [] else False

    assert test_sub_2(victim_name, victim_count, vic_plot) is True


