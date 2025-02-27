# VLE calculations using Antoine's Equation and Raoult's Law

This project calculates the vapor-liquid equilibrium (VLE) for ideal mixtures in equilibrium with an ideal vapor. The vapor pressure is modeled using Antoine's Equation and Raoult's Law, and the program generates a T-x-y diagram that represents the equilibrium compositions of the liquid and vapor phases at different temperatures.

## List of files in this Repository:

- **TxyNotebook.ipynb**: Jupyter notebook that calculates and visualizes the T-x-y diagram.
- **antoine.py**: Python script to calculate Antoine's coefficients for components.
- **get_antoine_coefficient.py**: Python script that retrieves Antoine's coefficients from the NIST webbook using requests and BeautifulSoup.
- **raoult_law_kvalue.py**: Python script for calculating the Raoult's law constant.

#### These files demonstrate the calculation of a T-x-y diagram for ideal mixtures in equilibrium with an ideal vapor, whose vapor pressure follows the empirical correlation of Antoine's Equation.

#### We grab Antoine's coefficients from the NIST webbook using requests and BeautifulSoup. We also use numpy and matplotlib.

#### This is useful for illustrating extraction of data from structured web pages.