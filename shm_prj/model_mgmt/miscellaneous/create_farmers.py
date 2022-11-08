#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import argparse


def do_rand(lim_inf, lim_sup):
    """Returns a random float between lim_inf and lim_sup."""
    return lim_inf + random.random()*(lim_sup-lim_inf)


def get_place(counter_places):
    """Returns a progresive random-choosen place's name."""
    place = random.choice(list(counter_places.keys()))
    j = counter_places[place]
    counter_places.update({place: j+1})

    return place + '_' + str(j)


def create_data(n, m):
    """Prints python command lines to create n Farmers and m Parcels."""
    # common first names
    f_names = {'M': ['Krishna', 'Shiva', 'Ram', 'Narayan', 'Piyush',
                     'Vishwajeet', 'Arjuna', 'Hariom', 'Karan', 'Pavan',
                     'Aditya', 'Vihaan', 'Sai', 'Pranav', 'Dhruv', 'Rithvik',
                     'Aarush'],
               'F': ['Swathi', 'Shruthi', 'Bhavani', 'Preeti', 'Anushka',
                     'Shailaja', 'Supriya', 'Sweta', 'Shilpa', 'Swapna']}
    # common last names
    l_names = ['Kumar', 'Lal', 'Sharma', 'Shaan', 'Jai', 'Kumbhar', 'Sutar',
               'Kulkarni', 'Deshpande', 'Deshmukh', 'Patil', 'Pawar', 'Desai',
               'Joshi']
    sex = ['M', 'F']
    # Palces inside Maharashtra, India.
    places = ['Ahmadnagar', 'Akola', 'Amravati', 'Aurangabad', 'Bhandara', 'Bid',
              'Buldana', 'Chandrapur', 'Dhule', 'Gadchiroli', 'Gondiya', 'Hingoli',
              'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Mumbai', 'Nagpur',
              'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Parbhani', 'Pune',
              'Raigad', 'Ratnagiri', 'Sangli', 'Satara', 'Sindhudurg', 'Solapur',
              'Thane', 'Wardha', 'Washim', 'Yavatmal']

    counter_places = {place: 0 for place in places}

    already_given = []
    while True:
        s = random.choice(sex)
        f_name = random.choice(f_names[s])
        l_name = random.choice(l_names)
        name = f_name + '_' + l_name
        if not name in already_given:
            already_given.append(name)
            print(name + ' = Farmer.objects.create(fName = "' + f_name + '"' +
                  ', lName = "' + l_name + '", age = ' + 
                  str(random.randint(18, 100)) + ', sex =' + s +')')
        if len(already_given) == n:
            break

    for i in range(m):
        name = get_place(counter_places)
        lon = do_rand(74, 77)
        lat = do_rand(18, 21)
        s = round(do_rand(0, 100)*100)/100
        g = round(do_rand(0, 100)*100)/100
        fer = round(do_rand(0, 100)*100)/100
        ls = round(do_rand(0, 100)*100)/100
        k = round(do_rand(0, 100)*100)/100
        inc = round(do_rand(0, 100)*100)/100
        farmer = random.choice(already_given)

        print('Parcel.objects.create(name= "' + name + '", lon = ' + str(lon) + 
              ', lat = ' + str(lat) + ', storage = ' + str(s) + ', grass = ' + 
              str(g) + ', fertility = ' + str(fer) + ', livestock = ' + 
              str(ls) + ', capital = ' + str(k) + ', income = ' + str(inc) +
              ', farmer = ' + farmer + ')')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Creates farmers and parcels.')
    parser.add_argument('-n', type=int, help='number of farmers')
    parser.add_argument('-m', type=int, help='number of parcels')

    args = parser.parse_args()
    create_data(args.n, args.m)
