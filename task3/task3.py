from sys import argv
import json

tests = argv[1]
values = argv[2]

with open(tests) as f_tests, open(values) as f_values, open('report.json', 'w') as f_report:
    tests_import = json.load(f_tests)
    values_import = json.load(f_values)

    for key_values in values_import["values"]:
        if key_values["id"] == tests_import["id"]:
            tests_import["value"] = key_values["value"]
        for key in tests_import["values"]:
            if key_values["id"] == key["id"]:
                key["value"] = key_values["value"]
    json.dump(tests_import, f_report)

    