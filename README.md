# Selenium Python Course Final Project

This repository contains the final project for the course "Automation Testing with Selenium and Python" on Stepik.org.

## Description

In this project, we create automated tests for a web application. We use Selenium to automate interactions with web application pages, and Python to write tests and run them.
The project implemented an automated test for the website (http://selenium1py.pythonanywhere.com/). The technologies used are Selenium, Python, PyTest, Page Object Pattern.

The `pages` folder in the repository contains files with page objects for the website. Each file in this folder contains a class representing the corresponding website page. For example, `base_page.py` contains the `BasePage` class which includes common methods for all pages. The `ProductPage` class contains methods for interacting with the product page, such as `add_to_cart()`, `get_product_name()`, `get_product_price()`, `should_be_success_message_with_product_name()`, and `should_be_cart_total_with_product_price()`. The `LoginPage` class contains methods for interacting with the login page, such as `should_be_login_page()`, `register_new_user()`, `should_be_authorized_user()`, etc. The `basket_page.py` file contains the `BasketPage` class with methods for interacting with the shopping cart page, such as `should_be_empty()`. 

In general, each class represents a corresponding website page and provides methods for interacting with it.

## Tests

We have implemented the following tests:

_test_product_page.py_ contains a set of tests for the product page. They check the presence of elements on the page, the ability to add a product to the cart and display messages about successful product addition, the absence of messages about successful product addition, and the ability to go to the user authorization page from the product page.

1. `test_guest_can_add_product_to_cart`:

    - checks the possibility of adding an item to the cart using the link with the promo parameter

    - gets the name and price of the added product

    - checks for messages about the successful addition of the product with the product name and displays the total cost of the products in the cart with the price of the added product.

2. `test_guest_cant_see_success_message_after_adding_product_to_basket`:  

    - checks if there are no notifications about the successful addition of an item to the cart on the product page.

3. `test_guest_cant_see_success_message`:

    - checks if there are no messages about the successful addition of a product on the product page.

4. `test_message_disappeared_after_adding_product_to_basket`:

    - checks that the message about the successful addition of the product has disappeared after adding the product to the cart.

5. `test_guest_should_see_login_link_on_product_page`:

    - checks for a link to the user authorization page on the product page.

6. `test_guest_can_go_to_login_page_from_product_page`:

    - checks if it is possible to go to the user authorization page from the product page.

7. `test_guest_cant_see_product_in_basket_opened_from_product_page`:

    - checks the display of an empty cart if you open it from the product page

The second part of the code contains the `TestUserAddToBasketFromProductPage` class, which contains two test cases for an authorized user:

1. `test_user_cant_see_success_message`:

    - checks that the authorized user does not see the message about the successful addition of the product to the cart.

2. `test_user_can_add_product_to_basket`: 

    - checks that an authorized user can successfully add a product to the cart and sees the corresponding message about the successful addition of the product to the cart.

In these tests, first, an instance of the product page is created, the page is opened, and the product is added to the cart. Then a math puzzle is solved and the product name and price are saved. Next, it is checked that the user sees a message about the successful addition of the product to the cart and that the product name is mentioned in this message. It is also checked that the user sees the correct total amount in the cart.

Such tests are important for verifying that the online store is working correctly with authorized users and maintaining their individual settings (such as currency, discounts, and bonuses). They help to identify possible problems and errors that arise in the interaction with the system with authorized users.

_test_main_page.py_ tests are defined in the `TestLoginFromMainPage` class, which has two methods for the first two scenarios. The third scenario is defined in a separate method outside the class. tests cover the following scenarios:

1. `test_guest_can_go_to_login_page`:

    - verifies that a guest user can go to the login page from the main page.

2. `test_guest_should_see_login_link`:

    - verifies that a guest user can see the login link on the main page.

3. `test_guest_cant_see_product_in_basket_opened_from_main_page`:

    - verifies that a guest user can see an empty basket when opening it from the main page.


## Installation and Usage

To run the project, you need to install Python and some dependencies. Make sure Python is installed on your computer. Then install the necessary dependencies using pip:

```sh
pip install -r requirements.txt
```

## Contributing

If you wish to contribute to this project, open a pull request. Make sure your contribution does not break existing tests and adds useful functionality.

## Author

The author of this project is Pavlo Mushtuk. If you have any questions or suggestions, you can contact me through my GitHub or [linkedIn](https://www.linkedin.com/in/paul-mushtuk/) profile.

## License

This project is distributed under the MIT license. Learn more about the license in the LICENSE file in this repository.