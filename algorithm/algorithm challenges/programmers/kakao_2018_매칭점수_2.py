import re

def solution(word, pages):
    word = word.lower()

    '''
    db = {
        인덱스 : {
            'basic' : 0,
            'link' : 0,
            'pointers' : [이 html을 향하는 html들의 idx]
        }

    }

    '''
    db = {}
    for i in range(len(pages)):
        db[i] = {
            'url' : [],
            'basic': 0,
            'link' : 0,
            'pointers': []
        }

    urls = []
    for idx, page in enumerate(pages):

        # 1. basic points
        temp_html = ''
        for c in page:
            if not (c.islower() or c.isupper()):
                temp_html += ' '
            else:
                temp_html += c
        temp_html = temp_html.split(' ')
        for part in temp_html:
            if part.lower() == word:
                db[idx]['basic'] += 1
        
        # url and link
        temp_html = re.split('\"| ', page)
        for i, part in enumerate(temp_html):
            if part == 'content=':
                url = temp_html[i+1]
                if url[:8] == 'https://':
                    url = url[8:]
                db[idx]['url'].append(url)
                urls.append(url)
            
            if part == 'href=':
                link = temp_html[i+1]
                if link[:8] == 'https://':
                    link = link[8:]
                db[idx]['pointers'].append(link)
                db[idx]['link'] += 1

        
    # pprint(db)

    #calculate
    points = [0 for _ in range(len(urls))]  #len(urls)와 len(db)가 다름

    for key, val in db.items():
        # if val['url'] == None:
        #     continue

        points[key] += val['basic']

        for link in val['pointers']:
            if link in urls:
                target = urls.index(link)
                if val['link'] != 0:
                    points[target] += val['basic'] / val['link']

    # print(points)

    #find max
    max_val, max_idx = points[0], 0
    for idx, val in enumerate(points):
        if max_val < val:
            max_val = val
            max_idx = idx

    answer = max_idx
    # print(answer)
    return answer