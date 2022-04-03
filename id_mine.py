# import necessary packages

import requests
import json


# url
url = 'https://api.hh.ru/'
url_vacancies = 'https://api.hh.ru/vacancies'


# some parameters, may change key word and area
params = {'text': 'name:Аналитик', 'area': 40} 

# request to count  
r = requests.get(url_vacancies, params=params)

# count ad
found = json.loads(r.text)['found'];
found


# download ids list of necessary vacancies
list_id = []
if found <= 100:
    params['per_page'] = found
    r = requests.get(url_vacancies, params=params)
    data = json.loads(r.text)['items']
    for vac in data:
        list_id.append(vac['id'])
else:
    i = 0;
    while i <= int(np.ceil(found/100)):   
        params['per_page'] = 100
        params['page'] = i
        r = requests.get(url_vacancies, params=params)
        if 200 != r.status_code:
            break
        data = json.loads(r.text)['items']
        for vac in data:
            list_id.append(vac['id'])
        i += 1
        
print('количество полученных айди', len(list_id))


# function to parce information from vacancy

def get_vacancy(id):

    url_vac = 'https://api.hh.ru/vacancies/%s'
    r = requests.get(url_vac % id)

    return json.loads(r.text)


# get information about necessary vacancies and make dataframe

df = []
a = 0
for i in list_id:
    vacancy = get_vacancy(i)
    dict_ = {'id' : vacancy['id'], 'name' : vacancy['name'], 'city' : vacancy['area']['name'], 
             'experience' : vacancy['experience']['name'], 'type' : vacancy['type']['name'],
             'address': vacancy['address'], 'published_at' : vacancy['published_at'],
             'archived' : vacancy['archived'], 'employer' : vacancy['employer']['name'],
             'contacts': vacancy['contacts'], 'schedule': vacancy['schedule']['id'], 
             'employer_trusted' : vacancy['employer']['trusted'],'professional_roles' : vacancy['professional_roles'][0]['name']}
    df_ = pd.DataFrame(dict_, index = [a])
    print(a) # были проблемы с ответами, они часто прерывались, поэтому я завела себе счетчик
    a += 1
    df.append(df_)
    
df_1 = pd.concat(df)
df_1    
