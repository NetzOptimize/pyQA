
# Flowchart

```mermaid
flowchart TB
    helper.py-- Functions are called from each test-->folders
    locator.json-- For each test--->folders
    conftest.py-- For each test-->folders
    pytest.ini-->conftest.py
    folders-- Each test genearates and overwrites for the same day--->day-month-year.html
    day-month-year.log--->day-month-year.html
    folders-- Each test genearates and overwrites for the same day--->logs
    default_css--->day-month-year.html
    subgraph folders
        subgraph smoke
        test_check.py
        end
        subgraph tests
        test_finalassert.py
        end
    end

    subgraph reports
    day-month-year---assets
    assets---default_css
    day-month-year--->day-month-year.html
    end
    subgraph locators
    locator.json
    end
    subgraph FUNCTIONS
    helper.py
    end
    subgraph logs
    day-month-year.log
    end
    conftest.py
    pytest.ini{pytest.ini}
```

## Functions of important files


|             | Function                                                                                                                                       | Changes allowed                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| pytest.ini  | This file starts first and contains the<br/>configurations for the tests.                                                                      | testspaths can be changed<br/>addopts function can be modified as per the commands needed. |
| conftest.py | This file runs after `pytest.ini`, contains the logic to run tests in multiple browsers simultaneously, also Html file can be configured here. | New browser web drivers can be added,<br/>Html file can be configured as per convenience.  |
| helper.py   | All test cases use functions from this file.                                                                                                   | New browser action functions can be added.                                                 |



## Defaults

#### The default folders set in `pytest.ini` to run tests is:
 - #### smoke

*Default folders can be changed from `pytest.ini` file.*

#### `pytest.ini` addopts verbose printing for detailed output, and uses commands of pytest-parallel, pytest-instafail,pytest-excel to modify the results.


## How html file is created:

```mermaid
graph LR
A[test_example] -- Only errors --> B((Log file))
A --> C(html file)
B -- If errors --> C
C --> D{Updated html file with logs}
```

