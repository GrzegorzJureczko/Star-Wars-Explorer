from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import requests
from datetime import date, datetime
import csv

from explorer import models


class CollectionsList(View):
    """displays list of all files saved"""

    def get(self, request):
        characters_data = models.Collection.objects.all()

        return render(request, 'explorer/collections.html', {'characters_data': characters_data})


class FetchData(View):
    """data fetch takes about 30 seconds to get all data"""

    def get(self, request):
        """
        counts how many pages of planets exists
        """
        get_homelands_count = requests.get('https://swapi.dev/api/planets')
        homelands_count = get_homelands_count.json()['count']
        homelands_pages = (homelands_count // (len(get_homelands_count.json()['results'])))
        if homelands_count % 10 != 0:
            homelands_pages += 1

        """
        to prevent sending request with every character, a dictionary of homelands is built up. With url as key and planet as value.
        """
        homelands = {}
        for page in range(1, homelands_pages + 1):
            response = requests.get(f'https://swapi.dev/api/planets/?page={page}')
            for homeland in response.json()['results']:
                homelands[homeland['url']] = homeland['name']

        """counts how many pages of characters exists"""
        get_count = requests.get('https://swapi.dev/api/people')
        count = get_count.json()['count']
        pages = (count // (len(get_count.json()['results'])))
        if count % 10 != 0:
            pages += 1
        characters_data = []

        """collects data of characters and transforms it into saveable in csv file"""
        for page in range(1, pages + 1):
            response = requests.get(f'https://swapi.dev/api/people/?page={page}')
            for character in response.json()['results']:
                homeland = homelands[character['homeworld']]  # takes homeland name from created dict
                char = [character['name'], character['height'], character['mass'], character['hair_color'],
                        character['skin_color'], character['eye_color'], character['birth_year'],
                        character['gender'], homeland, date.today()]
                characters_data.append(char)

        """
        creates header and saves it to csv file
        for improvement csv files should be stored in proper destination
        """
        header = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender',
                  'homeworld',
                  'date']
        data = characters_data
        file_name = (str(datetime.now())).replace(" ", "_")
        with open(f'{file_name}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

        """saves files information in database"""
        csv_object = models.Collection(file_name=file_name)
        csv_object.save()

        return redirect(reverse('explorer:collections'))


class CollectionDetails(View):
    def get(self, request, pk):
        """Displays list of saved csv files"""
        characters_data = models.Collection.objects.get(pk=pk)

        return render(request, 'explorer/details.html', {'characters_data': characters_data, 'page_id': pk})


class CollectionJSONDetails(View):
    def get(self, request, pk, *args, **kwargs):
        """logic for 'load more' functionality. Starts with range 0 to 10. Adds 10 with every button click"""
        upper = kwargs.get('num_posts')
        lower = upper - 10
        jsonArray = []
        characters_data = models.Collection.objects.get(pk=pk)
        with open(f"./{characters_data.file_name}.csv", encoding='utf-8') as file:
            csvReader = csv.DictReader(file)
            for row in csvReader:
                jsonArray.append(row)
        number_of_characters = len(jsonArray)
        max_size = True if upper >= number_of_characters else False
        jsonArray = jsonArray[lower:upper]

        return JsonResponse({'data': jsonArray, 'max': max_size}, safe=False)


class CollectionDetailsFilter(View):
    def get(self, request, pk):
        """
        displays data to template with filter functionality
        for improvement it can be merged with CollectionDetails view
        count functionality is not implemented
        """
        jsonArray = []
        characters_data = models.Collection.objects.get(pk=pk)
        with open(f"./{characters_data.file_name}.csv", encoding='utf-8') as file:
            csvReader = csv.DictReader(file)
            for row in csvReader:
                jsonArray.append(row)

        return render(request, 'explorer/filter.html', {'collection': jsonArray, 'characters_data': characters_data})
