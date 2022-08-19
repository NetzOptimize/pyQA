
# Dynamic web Checker

Automate the web testing using simple functions!




## Deployment

To deploy this project run

```bash
  pytest
```

For windows

```bash
  python -m pytest
```


## Installation

Install the project by unzipping the file

## Demo

Running headed automated login test on two browser simultaneously.



### HTML REPORT






## Features

- write simple code 
- built in selenium modified functions
- parallel testing in multiple browsers

## Running Tests

To run tests, run the following command

```bash
  pytest
```
For windows

```bash
  python -m pytest
```

## Running Single Test

To run tests, run the following command

```bash
  pytest <filename>
```
For windows

```bash
  python -m pytest <filename>
```

## Functions

### display_url

Returns the url of the current website in the current selected tab

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.display_url()

```

### input

Takes value from user and inputs in the field specified

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.input("input", "xpath", "<path>", "type", "test@gmail.com")

```

### button

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.button("button", "xpath", "<path>", "click")

```

### doubledropdown

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.doubledropdown("button", "xpath", "<path>", "click", "xpath", "<path>", "click")

```

### returner

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.returner("return", "xpath", "<path>", "text")

```

### take_pic

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.take_pic()

```

### word_assert

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.word_assert("hello", "hello")

```

### goto

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.goto("<new-url>")

```

### count_div_el

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.count_div_el("xpath", "<path>")

```

### divcheck

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    c = run.count_div_el("xpath", "<path>")
    for a in range(c):
        run.divcheck("<path>", "click", a)

```

### divtext

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    c = run.divtext("<path>", "text")
    print(c)  # prints list

```

### divtextcheck

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.divtextcheck("<path>", "text", "hello")

```

### homescreen

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.homescreen()

```

### childscreen

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.childscreen()

```

### closewindow

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.closewindow()

```

### returndivtext

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    c = run.count_div_el("xpath", "<path>")
    for a in range(c):
        x = run.returndivtext("<path>", "text", a)
        print(x)

```

### cookie_click

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.cookie_click("xpath", "<path>")

```

### end

Does this

```python
from FUNCTIONS.helper import Checker


def test(setup):
    run = Checker("<url>", setup)
    run.end()

```







## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


## Tech Stack

**Languages:** Python

**Frameworks:** Selenium, Pytest

**Pytest-plugins:** pytest-html, pytest-selenium


## Roadmap

- Additional browser support

- Add more integrations

- Cloud support



## Appendix

Any additional information goes here


## Documentations

[Selenium python](https://selenium-python.readthedocs.io)

[pytest](https://docs.pytest.org/en/7.1.x/contents.html)

[pytest-html](https://pytest-html.readthedocs.io/en/latest/)



## Authors

- [@montekkundan](https://www.github.com/Montekkundan)


## Feedback

If you have any feedback, please reach out at fake@fake.com
