from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import requests
from datetime import date, datetime
import csv
from explorer import models


class CollectionsList(View):
    def get(self, request):
        people_data = models.Collection.objects.all()
        return render(request, 'explorer/collections.html', {'people_data': people_data})


class FetchData(View):
    def get(self, request):
        """
        to prevent sending request with every character, a dictionary of planets is built up. With url as key and planet as value.
        """
        get_planets_count = requests.get('https://swapi.dev/api/planets')
        planets_count = get_planets_count.json()['count']
        planets_pages = (planets_count // (len(get_planets_count.json()['results'])))
        if planets_count % 10 != 0:
            planets_pages += 1

        planets = {}
        for page in range(1, planets_pages + 1):
            response = requests.get(f'https://swapi.dev/api/planets/?page={page}')
            for planet in response.json()['results']:
                planets[planet['url']] = planet['name']
        print(planets)

        get_count = requests.get('https://swapi.dev/api/people')
        count = get_count.json()['count']
        pages = (count // (len(get_count.json()['results'])))
        if count % 10 != 0:
            pages += 1
        people_data = []
        c = 1  # -------------
        for page in range(1, pages + 1):
            response = requests.get(f'https://swapi.dev/api/people/?page={page}')
            for character in response.json()['results']:
                planet = planets[character['homeworld']]
                person = [character['name'], character['height'], character['mass'], character['hair_color'],
                          character['skin_color'], character['eye_color'], character['birth_year'],
                          character['gender'], planet, date.today()]
                people_data.append(person)
                print(character['name'])  # -------------
                print(c)  # -------------
                c += 1  # -------------

        header = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender',
                  'homeworld',
                  'date']
        data = people_data
        file_name = (str(datetime.now())).replace(" ", "_")
        with open(f'{file_name}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

        csv_object = models.Collection(file_name=file_name)
        csv_object.save()

        return redirect(reverse('explorer:collections'))


class CollectionDetails(View):
    def get(self, request, pk):
        people_data = models.Collection.objects.get(pk=pk)

        return render(request, 'explorer/details.html', {'poeple_data': people_data, 'page_id': pk})


class CollectionJSONDetails(View):
    def get(self, request, pk, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = upper - 10
        jsonArray = []
        people_data = models.Collection.objects.get(pk=pk)
        with open(f"./{people_data.file_name}.csv", encoding='utf-8') as file:
            csvReader = csv.DictReader(file)
            for row in csvReader:
                jsonArray.append(row)
        number_of_characters = len(jsonArray)
        max_size = True if upper >= number_of_characters else False
        jsonArray = jsonArray[lower:upper]

        return JsonResponse({'data': jsonArray, 'max': max_size, 'page_id': pk}, safe=False)
