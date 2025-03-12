"""Temperature conversion"""

__author__ = ''

import argparse


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature in Celsius to Fahrenheit
    
    Keyword arguments:
    celsius -- The temperature in Celsius
    """
    pass


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature in Fahrenheit to Celsius
    
    Keyword arguments:
    fahrenheit -- The temperature in Fahrenheit
    """
    pass


if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Parse temperature arguments')
    # An argument for the temperature that will be converted
    parser.add_argument('temperature', type=float, 
        help='The temperature to convert')
    # An argument for the from unit - this will be the unit 
    # of the temperature argument
    parser.add_argument('from_unit', type=str, 
        choices=['f', 'c', 'fahrenheit', 'celsius'], 
        help='The unit of the temperature argument')
    
    # Parse the arguments
    args = parser.parse_args()

    pass
