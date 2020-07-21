# Python metric-imperial converter microservice

This is a Python/[Flask](https://flask.palletsprojects.com/en/1.1.x/) port of my [Node.js metric-imperial converter microservice project](https://ty-metricimpconverter.glitch.me/). It fulfills the following user stories:

1.  I can **GET** `/api/convert` with a single parameter containing an accepted number and unit and have it converted.
2.  Hint: Split the input by looking for the index of the first character.
3.  I can convert 'gal' to 'L' and vice versa. **(1 gal to 3.78541 L)**
4.  I can convert 'lbs' to 'kg' and vice versa. **(1 lbs to 0.453592 kg)**
5.  I can convert 'mi' to 'km' and vice versa. **(1 mi to 1.60934 km)**
6.  If my unit of measurement is invalid, returned will be 'invalid unit'.
7.  If my number is invalid, returned with will 'invalid number'.
8.  If both are invalid, return will be 'invalid number and unit'.
9.  I can use fractions, decimals or both in my parameter (e.g., 5, 1/2, 2.5/6), but if nothing is provided it will default to 1.
10. My return will consist of the `initNum`, `initUnit`, `returnNum`, `returnUnit`, and `string` spelling out units in format `{initNum} {initial_Units} converts to {returnNum} {return_Units}` with the result rounded to 5 decimals.
