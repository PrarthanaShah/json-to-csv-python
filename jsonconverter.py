import json
def convert_json_to_csv(json):
    csv =""
    length = len(json)

    if length >= 1:
        first_item = json[0]
        item_list = []
        for key in first_item.keys():
            item_list.append(str(key))
        csv = ','.join(item_list)
        csv += '\n'
        keys_length = len(item_list)
        for item in json:
            item_list = []
            for value in item.values():
                item_list.append(str(value))
            empty_columns = keys_length - len(item_list)
            for e in range(empty_columns):
                item_list.append((' '))
            csv += ','.join(item_list)

            csv += '\n'
    return csv
def savecsv(path,data):
    with open(path,'w') as f:
        f.writelines(data)
def readjson(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

if __name__ == '__main__':
    data=readjson('sample.json')
    csv = convert_json_to_csv(data)
    savecsv("sample.csv",csv)