gssetting
==

[![PyPI](https://badge.fury.io/py/gssetting.svg)](https://badge.fury.io/py/gssetting)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/deresmos/gssetting/blob/master/LICENSE)


About
===
gssetting is load setting value from Google Sheets.

Installation
==
To install gssetting, use pip.

```bash
pip install gssetting
```

Examples
==

## Google Sheets example.
| A| name | empty | value |
----|----|----|----
| B| test1 | none | value |
| C| test2 | ok | value ok |


## Sample code


```python
from dataclasses import dataclass

from gssetting import GoogleSpreadSheetSetting, GSSetting


@dataclass
class Setting(GSSetting):
    username: str
    value: str

    # Same header value of sheets
    headers = ["name", "value"]


if __name__ == "__main__":
    gs_setting = GoogleSpreadSheetSetting(
        "./service_account.json", "document_id"
    )
    settings = gs_setting.load("sheet_name", "A1:C3", Setting)
    print(settings)

    for setting in settings:
        print(setting.username.value)
```
