spm2olca
========
spm2olca is a small command line tool that converts a SimaPro LCIA method files 
to a `olca-schema https://github.com/GreenDelta/olca-schema`_  (JSON-LD) package.

Installation
------------
The installation of the package requires that Python >= 3.4 is 
`installed https://docs.python.org/3/using/`_ on your system and that the Python
`Scripts` folder is in your system path. If this is the case you just need to
install it from the command shell via:

.. code-block:: bash

    pip install spm2olca
    
After this you should be able to run the tool anywhere on your system. You can 
test this by executing the following command:

.. code-block:: bash

    spm2olca help
    
If you want to modify or improve the tool you can download the source and create
an egg-link with pip:
 
.. code-block:: bash

    git clone https://github.com/GreenDelta/spm2olca
    cd spm2olca
    pip install -e .

This will install the tool but with a link to this source code folder where you
can modify the respective functions.

Usage
-----
Just type the `spm2olca` command followed by the SimaPro CSV file with LCIA
methods you want to convert:

.. code-block:: bash
 
    spm2olca <SimaPro CSV file with LCIA methods>

This will generate the `olca-schema` package which will have the same file name
but with a `.zip` extension. This file can be then imported into openLCA.


Unit mapping
------------


Flow mapping
------------
