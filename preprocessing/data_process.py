# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:06:19 2020

@author: Aatish Rana
"""

from dataflows import Flow, load, unpivot, find_replace, set_type, dump_to_path, update_resource, join, add_computed_field, delete_fields

BASE_URL = 'https://raw.githubusercontent.com/sgbro/HealthCare-EPITECT/master/dataset/'
CONFIRMED = 'covid_confirmed.csv'
DEATH = 'covid_deaths.csv'
RECOVERED = 'covid_recovered.csv'

def to_normal_date(row):
    old_date = row['Date']
    month, day, year = row['Date'].split('-')
    day = f'0{day}' if len(day) == 1 else day
    month = f'0{month}' if len(month) == 1 else month
    row['Date'] = '/'.join([month, day, year])

unpivoting_fields = [
    { 'name': '([0-9]+\/[0-9]+\/[0-9]+)', 'keys': {'Date': r'\1'} }
]

extra_keys = [{'name': 'Date', 'type': 'string'} ]
extra_value = {'name': 'Case', 'type': 'number'}

Flow(
      load(f'{BASE_URL}{CONFIRMED}'),
      load(f'{BASE_URL}{RECOVERED}'),
      load(f'{BASE_URL}{DEATH}'),
      unpivot(unpivoting_fields, extra_keys, extra_value),
      find_replace([{'name': 'Date', 'patterns': [{'find': '/', 'replace': '-'}]}]),
      to_normal_date,
      set_type('Date', type='date', format='%m-%d-%y', resources=None),
      set_type('Case', type='number', resources=None),
      join(
        source_name='covid_confirmed',
        source_key=['Province/State', 'Country/Region', 'Date'],
        source_delete=True,
        target_name='covid_deaths',
        target_key=['Province/State', 'Country/Region', 'Date'],
        fields=dict(Confirmed={
            'name': 'Case',
            'aggregate': 'first'
        })
      ),
      join(
        source_name='covid_recovered',
        source_key=['Province/State', 'Country/Region', 'Date'],
        source_delete=True,
        target_name='covid_deaths',
        target_key=['Province/State', 'Country/Region', 'Date'],
        fields=dict(Recovered={
            'name': 'Case',
            'aggregate': 'first'
        })
      ),
      add_computed_field(
        target={'name': 'Deaths', 'type': 'number'},
        operation='format',
        with_='{Case}'
      ),
      delete_fields(['Case']),
      update_resource('covid_deaths', name='covid_combined', path='covid_combined.csv'),
      dump_to_path()
).results()[0]