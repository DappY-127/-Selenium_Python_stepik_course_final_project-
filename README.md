# -Selenium_Python_stepik_course_final_project-
Final project on the course - 'https://stepik.org/course/575/info'

# Selenium Python Course Final Project

This repository contains the final project for the course "Automation Testing with Selenium and Python" on Stepik.org.

## Description

In this project, we create automated tests for a web application. We use Selenium to automate interactions with web application pages, and Python to write tests and run them.
The project implemented an automated test for the website (http://selenium1py.pythonanywhere.com/). The technologies used are Selenium, Python, PyTest, Page Object Pattern.

## Tests

We have implemented the following tests:

test_product_page.py contains a set of tests for the product page. They check the presence of elements on the page, the ability to add a product to the cart and display messages about successful product addition, the absence of messages about successful product addition, and the ability to go to the user authorization page from the product page.

1. test_guest_can_add_product_to_cart:

- checks the possibility of adding an item to the cart using the link with the promo parameter

- gets the name and price of the added product

- checks for messages about the successful addition of the product with the product name and displays the total cost of the products in the cart with the price of the added product.


test_main_page.py


## Installation and Usage

To run the project, you need to install Python and some dependencies. Make sure Python is installed on your computer. Then install the necessary dependencies using pip:

```sh
pip install -r requirements.txt
```

## Contributing

If you wish to contribute to this project, open a pull request. Make sure your contribution does not break existing tests and adds useful functionality.

## Author

The author of this project is Pavlo Mushtuk. If you have any questions or suggestions, you can contact me through my GitHub profile.

## License

This project is distributed under the MIT license. Learn more about the license in the LICENSE file in this repository.