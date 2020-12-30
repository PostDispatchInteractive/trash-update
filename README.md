Trash complaints grow in St. Louis. 'You have to make people know it's not OK.'
========================

* [What is this?](#what-is-this)
* [Assumptions](#assumptions)
* [How to reproduce](#how-to-reproduce)
* [Data caveats](#data-caveats)

What is this?
-------------

This repo contains data and code used for the Dec. 30, 2020 (online) and Jan. 3, 2021 (print) St. Louis Post-Dispatch story "Trash complaints grow in St. Louis. 'You have to make people know it's not OK.'" The story was reported and written by [Janelle O'Dea](https://twitter.com/jayohday).

Assumptions
-----------

The following things are assumed to be true in this documentation.

* You are running OSX.
* You are using Python 3.7.
* You have [virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) installed and working.

How to reproduce
-------------
To reproduce this data analysis, you'll need a working knowledge of virtual environments and Python.

You'll need the libraries as specified in the `requirements.txt` file. To install the libraries, change into the `parks` directory, turn on your virtual environment and run the Terminal command `pip install -r requirements.txt`.

Extract the data from the `.zip` file.

The code in the Jupyter Notebook file shows the filtering and sorting that was done to get the data points reported in the story. To see how we arrived at the data, run the code in the [Jupyter Notebook](https://jupyter.org/) file `csb-trash-update-2020.ipynb`.

Data caveats
-------------
The `csb.zip` file contains the data used for this analysis, as downloaded on Dec. 6, 2020 from the city of St. Louis Open Data portal https://www.stlouis-mo.gov/data/upload/data-files/csb.zip under the "Service Requests" link.

The data reflect complaints submitted by residents of the city of St. Louis by phone, web, email or Twitter. Each row reflects one complaint.

The data dictionary can be found at the same Open Data portal link above, under the "Service Request Field Definitions" link.

The complaint data reflects only what's reported to the city. Other trash issues may exist and nobody calls them in.

There is a unique identifier for each complaint, `REQUESTID`. There is not a unique identifier for who reported the complaint. Therefore, it's not possible to know if the same person made all of the complaints about the same pile of trash or a number of different people did.