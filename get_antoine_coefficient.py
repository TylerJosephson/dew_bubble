# reference:
# https://www.linkedin.com/pulse/scraping-nist-webbook-python-extract-antoine-equation-oscar-fabi%C3%A1n/

from requests import get
from bs4 import BeautifulSoup

def get_response(url):
    return get(url).content

def get_html_table(Name):

    # We treat the url attaching the Name variable to it.
    url = f"https://webbook.nist.gov/cgi/cbook.cgi?Name={Name.lower()}&Mask=4"

    # Function to get the request made, see above.
    raw_html = get_response(url)

    # Parse the html using BeautifulSoup.
    html = BeautifulSoup(raw_html, 'html.parser')

    # Extract the table that contains the data, the table has a specific
    # attributes 'aria-label' as 'Antoine Equation Parameters'.
    table = html.find('table', attrs={'aria-label': 'Antoine Equation Parameters'})

    return table

def get_antoine_coefficient(Name, Temperature):

    # Obtaining the table using the get_html function showed below. Table is a
    # BeautifulSoup Object.
    table = get_html_table(Name)

    # Extract the rows from the table. Knowing what tags have an HTML table.
    # Also, knowing that the fist row with the table header does not have the
    # class attribute 'exp' so we obtain just the rows with data.
    # The find_all function from BeautifulSoup return a list
    rows = table.find_all('tr', class_='exp')

    # Declaring the lists for storage Temperatures, and coefficients.
    Temperatures, As, Bs, Cs = [], [], [], []

    # Looping over rows to extract and fill As, Bs, and Cs variables because now
    # we are sure the Temperatues is between some range.
    for row in rows:

        # As the rows, we extract the columns for the current row. Knowing that
        # the cols have the <td> tag in HTML as well
        # The find_all function from BeautifulSoup return a list
        cols =  row.find_all('td')

        # First transform the strings into float numbers and put them in their
        # respective list
        As.append(float(cols[1].text))
        Bs.append(float(cols[2].text))
        Cs.append(float(cols[3].text))

        # For the temperatures, we have a range and we need to extract each
        # limit (lower and higher) and put them in an extra list. So
        # Temperatures variable will be a list of lists.
        lower_lim = float(cols[0].text.replace(" ","").split('to')[0])
        higher_lim = float(cols[0].text.replace(" ","").split('to')[1])
        Temperatures.append([lower_lim, higher_lim])


    # Checking if the Temperature gave fits in some interval
    index = int()
    for i, interval in enumerate(Temperatures):
        if (interval[0] <= Temperature
            and Temperature <= interval[1]):
            index = i
            break
        else:
            index = None

    if index == None:
        print('Sorry, the data for the given temperature {0}K does '
              'not exist in the Data Base'.format(Temperature))
        return None

    else:
        A = As[index]
        B = Bs[index]
        C = Cs[index]
        lower_lim, higher_lim = Temperatures[index]
        return [A, B, C, lower_lim, higher_lim]
