# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING doctorName
#  2. INTEGER diagnosisId
# API URL: https://jsonmock.hackerrank.com/api/medical_records?page={page_no}
#
# Goal is to return the max and min temperature for each record matching the 
# given doctorName and diagnosisId

import requests

def bodyTemperature(doctorName, diagnosisId):
    path = f'https://jsonmock.hackerrank.com/api/medical_records'
    r = requests.get(path)
    response = r.json()
    numPages = response['total_pages']
    temps = []
    for i in range(numPages):
        path = f'https://jsonmock.hackerrank.com/api/medical_records?page={i}'
        r = requests.get(path)
        response = r.json()
        data = response['data']
        for record in data:
            if int(record['diagnosis']['id']) == int(diagnosisId) and record['doctor']['name'] == doctorName:
                temps.append(int(record['vitals']['bodyTemperature']))
    if temps: 
        return(min(temps), max(temps))
    return 'No matches found for the given criteria'

print(bodyTemperature('Dr Arnold Bullock', 2))