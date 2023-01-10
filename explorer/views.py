from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import requests
from datetime import date, datetime
import csv
from explorer import models


# Create your views here.


class CollectionsList(View):
    def get(self, request):
        people_data = models.Collection.objects.all()
        return render(request, 'explorer/collections.html', {'people_data': people_data})


class FetchData(View):
    def get(self, request):
        get_count = requests.get('https://swapi.dev/api/people')
        count = get_count.json()['count']
        pages = (count // 10) + 1
        people_data = []
        c = 1  # -------------
        for page in range(1, pages + 1):
            response = requests.get(f'https://swapi.dev/api/people/?page={page}')
            for character in response.json()['results']:
                planet = requests.get(character['homeworld'])
                person = [character['name'], character['height'], character['mass'], character['hair_color'],
                          character['skin_color'], character['eye_color'], character['birth_year'],
                          character['gender'], planet.json()['name'], date.today()]
                people_data.append(person)
                print(character['name'])
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
        context = []

        with open(f"./{people_data.file_name}.csv", 'r') as file:
            csvreader = csv.reader(file)
            print(csvreader)
            for row in csvreader:
                if row[0] != 'name':
                    person = {'name': row[0], 'height': row[1], 'mass': row[2], 'hair_color': row[3], 'skin_color': row[4],
                              'eye_color': row[5], 'birth_year': row[6], 'gender': row[7], 'planet': row[8],
                              'date': row[9]}
                    context.append(person)
        print(context)
        return render(request, 'explorer/details.html', {'context': context})
