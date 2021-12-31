import time
import datetime
import pandas as pd
import numpy as np
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all','january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA= ['saturday','sunday','monday', 'tuesday', 'wednesday','thursday','friday','all']
   
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_input = ''
    while city_input.lower() not in CITY_DATA :
        city_input = input("\nplease input the of city you need to analyze data?  Input either : \nchicago\nnew york city\nwashington\n")
    if city_input.lower() in CITY_DATA:
        city = CITY_DATA[city_input.lower()]
    else:
        print("Sorry wrong input, Please input either :\nchicago\nnew york city\nwashington.\n")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = ''
    while month_input.lower() not in MONTH_DATA:
        month_input = input("\nplease input the month you need to filter data by or input all to no filter?  Input either : \njanuary\nfebruary\nmarch\napril\nmay\njune\nall\n")
    if month_input.lower() in MONTH_DATA:
        month = month_input.lower()
    else:
        print("Sorry wrong input, Please input either : \njanuary\nfebruary\nmarch\napril\nmay\njune\nall'\n")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_inpute = ''
    while day_inpute.lower() not in DAY_DATA:
        day_inpute = input("\nplease input the day you need to filter data by or input all to no filter? Input either : \nsaturday\nsunday\nmonday\ntuesday\nwednesday\nthursday\nfriday\nall\n")
        if day_inpute.lower() in DAY_DATA:
            day = day_inpute.lower()
        else:
            print("Sorry wrong input, Please input either : \nsaturday\nsunday\nmonday\ntuesday\nwednesday\nthursday\nfriday\nall\n")
             
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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour             
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
          
    return df


def time_stats(df,city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print("Statistics for City:{} filter by month={} and Day={}\n".format(city,month,day))
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: {}\n".format(MONTH_DATA[most_common_month]))

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: {}\n".format(most_common_day_of_week))

    # TO DO: display the most common start hour
    most_comman_hour=df['hour'].mode()[0]
    if most_comman_hour<=12 :
        print("The most common start hour is: {} AM\n".format(most_comman_hour))
    else :
        print("The most common start hour is: {} PM\n".format(most_comman_hour-12))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}\n".format(most_common_start_station))
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}\n".format(most_common_end_station))
   # TO DO: display most frequent combination of start station and end station trip
    most_freq_combination= (df['Start Station']+' To '+ df['End Station']).mode()[0]  
    print("The most frequent combination of start station and end station trip is:\n{}".format(most_freq_combination))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_convert=datetime.timedelta(seconds=int(total_travel_time))
    print("The total travel time in seconds:{}\nThe total travel time in days:{}\n".format(total_travel_time,total_travel_time_convert))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round()
    print("The mean travel time is: {} seconds\n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("The count of user types is:\n {}\n".format(counts_of_user_types))

    # TO DO: Display counts of gender
    if city != 'washington.csv':
        counts_of_gender = df['Gender'].value_counts()
        print("The count of user gender is:\n {}\n".format(counts_of_gender))
    # TO DO: Display earliest, most recent, and most common year of birth
        print('The Most Earliest year of birth is: {}\n'.format(int(df['Birth Year'].min())))
        print('The Most recent year of birth is: {}\n'.format(int(df['Birth Year'].max())))
        print('The Most common year of birth is: {}\n'.format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """ display 5 rows at a time """
    i = 0
    raw = input("would you like to view the row data? please input either:\nyes\nno\n".lower())
    # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) 
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("would you like to view 5 more rows\n").lower() 
            # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
  

def restart_prog():
    while True: 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
        elif restart.lower() == 'yes':
            main()
        else:
            restart = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        restart_prog()
      

if __name__ == "__main__":
	main()
