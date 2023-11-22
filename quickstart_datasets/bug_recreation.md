# Bugs in quickstart

## Quick Start Stalls

**Description:** Generating views using `ver_quick_start.py` stalls at `Find Join Graphs` step for the `airport_data` dataset.

To recreate, use paste the following example query in `ver_quick_start.py`. 
```
example_columns = [
    ExampleColumn(attr='Valid', examples=['2021-01-01 00:53', '2021-02-07 18:00']),
    ExampleColumn(attr='Station', examples=['LAX', 'ATL']),
    ExampleColumn(attr='Tmpf', examples=['67', '69']),
    ExampleColumn(attr='Alti', examples=['30.52', '30.44'])
]
```

Edit `data_path` on line 62 of `ver_quick_start.py` to `data_path = `./quickstart_datasets/airport_data`

Then, run the following commands from the top level directory:
```
$ ./quickstart_datasets/clean.sh 
$ ./quickstart_datasets/data_setup.sh `airport_data`
$ python3 ver_quick_start.py
```

After generating candidate columns, the program stalls.

## Datasets unable to create views

- `solar_data` - No views are generated when following the steps in `data_info.md`.