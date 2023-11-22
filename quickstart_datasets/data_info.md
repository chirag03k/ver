# Usage 

This exists to make it easier to set up extra datasets with ver, to test out the quickstart demo. 

Navigate to the top level directory and run 
```
$ ./quickstart_datasets/clean.sh
$ ./quickstart_datasets/data_setup.sh <dataset_name>
```

Currently available datasets are `airport_data`, `calschools_data`, `city_data`, `covid_data`, and `solar_data`.
See below for more information on what these datasets contain. 


# airport_data

Weather information for the top 20 busiest US airports. Includes temperature, precipitation, pressure data for 2021-2023.

_QBE Example:_
```
example_columns = [
    ExampleColumn(attr='Valid', examples=['2021-01-01 00:53', '2021-02-07 18:00']),
    ExampleColumn(attr='Tmpf', examples=['67', '69']),
    ExampleColumn(attr='Alti', examples=['30.52', '30.44'])
]
```

# calschools_data

Test score performance and absenteeism at California public schools at the school level. 

_QBE Example:_
```
example_columns = [
    ExampleColumn(attr='School Name', examples=['El Cerrito High', 'Lincoln Elementary', 'Alliance Marine - Innovation and Technology 6-12 C']),
    ExampleColumn(attr='School Code', examples=['129593', '6019558']),
    ExampleColumn(attr='Students Enrolled', examples=['1124', '59', '78']),
    ExampleColumn(attr='Mean Scale Score', examples=['193.1','214','600']),
    ExampleColumn(attr='Chronic Absenteeism Rate', examples=['22.7', '23.4','36.3'])
]
```

# city_data

Demographic information on largest cities in the US by size.

```
example_columns = [
    ExampleColumn(attr='City Name', examples=['Chicago, IL', 'Los Angeles, CA', 'Tulsa, OK']),
    ExampleColumn(attr='2010 Population', examples=['2134411', '3439809']),
    ExampleColumn(attr='Density', examples=['3439809', '1292.1', '590.1'])
]
```

# covid_data

Information on covid counts, testing numbers, vaccines, mortality rates, for several countries.

```
example_columns = [
    ExampleColumn(attr='Country', examples=['South Korea', 'United Kingdom', 'El Salvador']),
    ExampleColumn(attr='Confirmed Cases', examples=['13761','268934','227019']),
    ExampleColumn(attr='Total Covid-19 Tests', examples=['27000', '16717', '2504'])
]
```

# solar_data

Information on solar power generation from different power plants (dataset from Kaggle).

```
example_columns = [
    ExampleColumn(attr='DATE_TIME', examples=['15-05-2020 00:00', '13-06-2020 03:30']),
    ExampleColumn(attr='PLANT_ID', examples=['4135001']),
    ExampleColumn(attr='AMBIENT_TEMPERATURE', examples=['27', '26.3'])
]
```

# demo_dataset

Original demo dataset for ver. Data concerning public schools around Chicago. This dataset is not available for 
automated setup using bash files. Refer to `quick_start_cli.md` for instructions on how to use this dataset.

```
example_columns = [
    ExampleColumn(attr='school_name', examples=["Ogden International High School", "University of Chicago - Woodlawn"]),
    ExampleColumn(attr='school type', examples=["Charter", "Neighborhood"]),
    ExampleColumn(attr='level', examples=["Level 1", "Level 2+"])
]
```

