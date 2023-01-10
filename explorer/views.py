import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import requests
from datetime import date, datetime
import csv

# Create your views here.


class Collections(View):
    def get(self, request):
        return render(request, 'explorer/collections.html')



class FetchData(View):
    def get(self, request):
        get_count = requests.get('https://swapi.dev/api/people')
        count = get_count.json()['count']
        pages = (count // 10) + 1
        people_data = []
        for page in range(1, pages + 1):
            response = requests.get(f'https://swapi.dev/api/people/?page={page}')
            for character in response.json()['results']:
                planet = requests.get(character['homeworld'])
                person = [character['name'], character['height'], character['mass'], character['hair_color'],
                          character['skin_color'], character['eye_color'], character['birth_year'],
                          character['gender'], planet.json()['name'], date.today()]
                people_data.append(person)

        header = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender',
                  'homeworld',
                  'date']
        data = people_data
        file_name = (str(datetime.now())).replace(" ", "_")
        with open(f'{file_name}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

        return redirect(reverse('explorer:collections'))