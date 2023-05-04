import json 

def get_data():
    with open('../api/json/final-coverage.json', 'r') as file:
        final_coverage = json.load(file)
        for i in final_coverage:
            print(i)

get_data()