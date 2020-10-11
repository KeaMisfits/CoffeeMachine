# CoffeeMachine
This is a guide how to use the code.

1. Make sure you have pandas and matplotlib modules installed for Python 3
      pip install pandas
      pip install matplotlib
2. To run our code you must compile "CoffeeMachine.py" with Python 3.8.4+.
    (May work with older versions of Python 3 too.)

This is a prototype version of the coffee machine that we are developing, thus
  some parts of the code are there only to make the prototype functional.
  Please refer to this note when testing out the code.
1. Student card id will be aquired automatically when scanning  the card, yet
    in the prototype version, you will have to input it manually

    You can either input any string to register a new user. The new user will
      not be a member, thus you will have to buy a membership.

    Or you can use one of the following pre-made users.

    STUDENT CARD ID     NAME          MEMBERSHIP EXPIRATION DATE   
    qwerty123           Thomas        2020-10-20
    abcde123            Jonas         2020-11-09
    zxcv123             Ben           2020-11-08
    ababa123            Emma          1990-01-01
    uiop123             John          2020-08-09
    abcabc123           Jason         1990-01-01

2. Coffee Machine will communicate with the bank to verify whether the credit
    card information is valid and accepted, however here, for testing purposes
    we made a few credit cards that the coffee machine will recognize.

    Use the following credit cards when buying.
    CARD Number               CVC
    1111-1111-1111-1111       111
    2222-2222-2222-2222       222
    3333-3333-3333-3333       333

Successful test scenario #1.
1. Entering an unrecognized student card id (ex. hello456), will allow to
    successfully create a new user.
2. Choosing 'menu' as delivery option, would print out 3 possible coffees
    and choosing one of the given coffees (ex. 'latte)' will proceed to payment
    step, also showing the price and order id.
3. Entering invalid credit card information (ex. 1234-1234-1234-aaaa, 555) will
    show a failure message and prompt to try again. Inputing 'yes' will allow to
    try again.
4. Entering a valid credit card information (ex. 2222-2222-2222-2222, 222) will
    show a coffee delivered message, including the coffee name (ex. Latte).

Successful test scenario #2.
1. Entering an unrecognized student card id (ex. python777), will allow to
    successfully create a new user.
2. Choosing 'membership' as delivery option, would prompt to input credit card
    information, also showing the price and order id.
3. Entering a valid credit card information (ex. 3333-3333-3333-3333, 333) will
    accept the payment and return to choose delivery screen. The membership now
    is extended for 30 days.
4. Choosing 'menu' as delivery option, would print out 3 possible coffees
    and choosing one of the given coffees (ex. 'capuchino') will immediatelly
    show a coffee delivered message, including the coffee name (ex. Capuchino).
    It will show it immediatelly since the user has a membership now.
5. Running the application on the same day again and entering the same student
    card id as in step 1 (ex. python777) will immediatelly show the delivery
    option menu, without requirement to create a new user.
6. Choosing 'menu' as delivery option, would print out 3 possible coffees
    and choosing one of the given coffees (ex. 'espresso)' will proceed to
    payment step, also showing the price and order id.
7. Entering a valid credit card information (ex. 1111-1111-1111-1111, 111) will
    show a coffee delivered message, including the coffee name (ex. Espresso).

Successful test scenario #3
1. Entering a recognized student card id (ex. qwerty123) will proceed to choose
    delivery option interface.
2. Selecting 'stats' as the delivery option will display a plot of the revenues
    earned lifetime.