# Dan rojas
# Nov 3 2025
# mod 4.2


import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'


# Broke the program up into functions. Depending on user input, will plot either high temp or low temp data. Will
# loop endlessly unless user provides "exit" as input.


def main():
    plot_temps()


def plot_temps():
    while True:
        selection = menu()
        if selection == "exit":
            print("Exiting...")
            break
        else:
            dates, temps = populate_lists(selection)
            create_figure(selection, dates, temps)


def menu():
    options = ['highs', 'lows', "exit"]
    user_input = input(f"Would you like to plot high temps or low?\n"
                       f"Enter \'highs\' for high temps,\n"
                       f"Enter \'lows\' for low temps,\n"
                       f"Enter \'exit\' to exit the program.\n"
                       f">").lower()
    if user_input in options:
        return user_input
    else:
        print("Please enter a valid selection.")
        return menu()


def populate_lists(selection):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and desired temperatures from .csv file.
        dates, temps = [], []
        if selection == "highs":
            t = 5  # row 5 highs
        else:
            t = 6  # row 6 lows
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            temp_val = int(row[t])
            temps.append(temp_val)
        return dates, temps


def create_figure(selection, dates, temps):
    color = ''
    title = ''
    # Plot the temperatures.
    # plt.style.use('seaborn')
    fig, ax = plt.subplots()
    if selection == 'highs':
        color = 'red'
        title = "Daily high temperatures - 2018"
    else:
        color = 'blue'
        title = "Daily low temperatures - 2018"
    ax.plot(dates, temps, c=color)
    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


if __name__ == "__main__":
    main()
