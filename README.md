# spm2olca
spm2olca is a simple command line tool that converts a SimaPro LCIA method files
to a [olca-schema](https://github.com/GreenDelta/olca-schema>) (JSON-LD) package.


## Installation
The installation of the package requires that Python >= 3.4 is 
[installed](https://docs.python.org/3/using/) on your system and that the Python
`Scripts` folder is in your system path. To install `spm2olca`, 
[download](https://github.com/GreenDelta/spm2olca/archive/master.zip) the
latest latest version and extract it to a folder (or get it via `git clone ...`).
Open a command line, switch to the `spm2olca` folder, and create an egg-link:

```bash
cd spm2olca
pip install -e .
```

After this you should be able to run the tool anywhere on your system. You can 
test this by executing the following command:

```bash
spm2olca -h
```

To uninstall it, just the following command:

```bash
pip uninstall spm2olca
```


## Usage
Just type the `spm2olca` command followed by the SimaPro CSV file with LCIA
methods you want to convert:

```bash
 spm2olca <SimaPro CSV file with LCIA methods>
```

This will generate the `olca-schema` package which will have the same file name
but with a `.zip` extension. This file can be then imported into openLCA.

To see additional options use the help flag `-h`:

```bash
spm2olca -h
```

Additional options:

* `-out`: define the name of the output file
* `-skip_unmapped`: LCIA factors with unmapped flows are not included (only
  applicable when a flow mapping is provided)
* `-log`: define the log level (e.g. 'all' will log everything)
* `-units`: A CSV file with unit mappings that should be used
* `-flows`: A CSV file with flow mappings that should be used

A command with all options could look like this:

```bash
spm2olca -out=out.zip -log=all -skip_unmapped -units=units.csv -flows=flows.csv Method.csv
```

## Mapping files
You can specify mapping files for flows and units that should be used in the
conversion. If no unit mapping file is given, `spm2olca` will take a 
[default mapping](./spm2olca/data/units.csv) file in the conversion. For flows,
new flows will be created if no mapping file is provided or if they are not
contained in the mapping file. The general format of these mapping files is:

* CSV files with semicolons as separator
* UTF-8 encoded without a byte order mark
* no column headers

### Unit mappings
Units are mapped by name to openLCA units and flow properties. The mapping file
must have the following columns:

```
0.  SimaPro name of the unit
1.  openLCA reference ID of the unit
2.  openLCA name of the flow property
3.  openLCA reference ID of the flow property
```

### Flow mappings
The SimaPro flows are mapped to openLCA reference flows with a CSV mapping file
with the following columns:

```
0.  SimaPro name of the flow (string)
1.  SimaPro compartment of the flow (string)
2.  SimaPro sub-compartment of the flow (string)
3.  SimaPro unit of the flow (string)
4.  openLCA reference ID of the flow (UUID)
5.  openLCA name of the flow (string)
6.  openLCA reference ID of the reference flow property of the flow (UUID)
7.  openLCA name of the reference flow property of the flow (string)
8.  openLCA reference ID of the reference unit of the flow (UUID)
9.  openLCA name of the reference unit of the flow (string)
10. conversion factor: amount_simapro * factor = amount_openlca (double)
```

This is the same file as in the openLCA reference data. The conversion factor
:math:`f` converts a flow amount from SimaPro :math:`a_s` in the SimaPro 
reference unit to the respective amount of the flow in the openLCA reference
unit :math:`a_o`:

```
a_o = f * a_s
```

e.g. 
    
```
a_o = [m3] = 0.001 * [kg] with a_s = [kg]
```
    
Thus the value of an SimaPro LCIA factor is *divided* by the conversion factor
for such a mapped flow when converted to openLCA, e.g.:

```
lcia_o = 2000/[m3] = 2/(0.001*[kg]) with a_s = [kg] 
```

TODOS
-----
* read delimiter from file header (currently only semicolons are supported)
