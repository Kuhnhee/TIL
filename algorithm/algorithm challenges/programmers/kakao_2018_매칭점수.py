from pprint import pprint

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
            'url' : None,
            'basic': 0,
            'link' : 0,
            'pointers': []
        }

    urls = []
    for idx, page in enumerate(pages):

        #calculate basic points/ find urls/ find links
        link = ''
        url = ''
        buffer = ''
        link_searcher = False
        link_searcher_assist = False
        url_searcher = False
        url_searcher_assist = False
        for c in page:

            ###############################################

            if url_searcher and url_searcher_assist and c == '\"':
                url_searcher = False
                url = url[9:]
                db[idx]['url'] = url
                urls.append(url)

            if url_searcher:
                if c == '\"':
                    url_searcher_assist = True
                url += c

            ###############################################

            if link_searcher and link_searcher_assist and c == '\"':
                link_searcher, link_searcher_assist = False, False
                link = link[9:]
                db[idx]['link'] += 1
                db[idx]['pointers'].append(link)
                link = ''   #initialize link

            if link_searcher:
                if c =='\"':
                    link_searcher_assist = True
                link += c

            ###############################################

            if (not c.islower()) and (not c.isupper()):
                if buffer.lower() == word:
                    db[idx]['basic'] += 1

                if buffer == 'content':
                    url_searcher = True

                if buffer == 'href':
                    link_searcher = True

                buffer = ''
            else:
                buffer+=c

        if buffer == word:
            db[idx]['basic'] += 1
            buffer = ''


        # print(db[idx]['basic'])
        # print(db[idx]['url'])

    # pprint(db)
    
    #calculate
    points = [0 for _ in range(len(db))]

    for key, val in db.items():
        if val['url'] == None:
            continue

        points[key] += val['basic']

        for link in val['pointers']:
            if link in urls:
                target = urls.index(link)
                points[target] 
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

if __name__ == "__main__":
    # solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    solution("abc", ["abc@abcabc"])

