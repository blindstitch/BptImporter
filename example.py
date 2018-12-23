#!/usr/bin/env python3

import BptImporter

optins = BptImporter.BptImporter('name')
optins.importData('path/to/file.xlsx')
optins.processData()

df = optins.getData()

print(df)
