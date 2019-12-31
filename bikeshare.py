import time
import pandas as pd
pd.options.display.max_rows
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #city = ('chicago', 'new_york_city', 'washington')
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


    print('Hello! Let\'s explore some US bikeshare data!')



    while True:
      city = input("Which city would you like to filter by: New York City, Chicago or Washington?\n").lower()
      if city not in CITY_DATA:
        print("That is an invalid response. Please try again")
        continue
      else:
        break


    while True:
      month = input("Which month would you like: All, January, February, March, April, May, June?\n").lower()
      if month not in months:
        print("That is an invalid response. Please try again")
        continue
      else:
        break


    while True:
      day = input("Which day would you like? 'All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',         'Sunday'\n").lower()
      if day not in days:
        print("That is an invalid response. Please try again")
        continue
      else:
        break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1
      df = df[df['month'] == month]

    if day != 'all':
      df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month: ', most_common_month)

    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', most_popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most Common Hour:', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: ', most_common_start_station)



    most_common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', most_common_end_station)


    

    Combined_Station = df.groupby(['Start Station', 'End Station']).count()
   # combined_stat2 = df ['Start Station'] +  df ['End Station'].mode()[0]
    combined_stat2 =  ( df ['Start Station'] + '/' + df ['End Station']).mode()[0]

    print('\nMost Commonly Used Combination of Start Station and End Station Trip:\n', combined_stat2)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Trip Duration: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Type: ', user_types)


    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)

    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)

    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
     Most_Common_Year = df['Birth Year'].value_counts().idxmax()
     print('\nMost Common Year:', Most_Common_Year)

    except KeyError:
     print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disp_raw_data(df):
    '''
    Displays the data used to compute the stats
    Input:
        the df with all the bikeshare data
    Returns:
       none
    '''
    #omit irrelevant columns from visualization
   # df = df.drop(['month', 'day_of_month'], axis = 1)
    row_index = 0

    see_data = input("\nYou like to see rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
