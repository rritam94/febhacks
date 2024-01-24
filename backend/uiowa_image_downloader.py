import requests
import shutil

urls = []
names = []
image_urls = []

request = requests.get("https://medicine.uiowa.edu/dermatology/education/clinical-skin-disease-images")
html = request.text

idx = html.find('<a href="//medicine.uiowa.edu/dermatology/')

while idx != -1:
    url = 'https://medicine.uiowa.edu/dermatology/'
    idx = html.find('<a href="//medicine.uiowa.edu/dermatology/')
    end_idx = idx + 42

    while(html[end_idx] != '"'):
        url += html[end_idx]
        end_idx += 1
    
    urls.append(url)
    names.append(url[39:])
    print(names[0])
    html = html[end_idx:]
    
for i in range(0, len(urls) - 1): # im dumb
    request = requests.get(urls[i])
    html = request.text
    
    url = 'https://medicine.uiowa.edu/dermatology/sites/medicine.uiowa.edu.dermatology/files/wysiwyg_uploads/'
    idx = html.find('typeof="foaf:Image" src="//medicine.uiowa.edu/dermatology/sites/medicine.uiowa.edu.dermatology/files/wysiwyg_uploads/')
    end_idx = idx + 117

    while(html[end_idx] != '"'):
        url += html[end_idx]
        end_idx += 1

    image_urls.append(url)

for i in range(0, len(image_urls)):
    url = image_urls[i]
    file_name = "medical-images/" + names[i] + ".jpg"
    

    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)

        print('Image sucessfully Downloaded: ',file_name)

    else:
        print('Image Couldn\'t be retrieved')
        