import re

#find <meta ~ />
#find <a ~ >
def re(start, end, page):
    result = []
    start_l, end_l = len(start), len(end)

    buffer = ''
    candidate = False
    for i in range(len(page)-1):

        # print(i, page[i:i+start_l], start)
        if candidate:
            if page[i:i+end_l] == end:
                buffer+=end
                result.append(buffer)
                buffer = ''
                candidate = False
                continue
            
            if start == '<meta':
                if page[i] == '>':
                    buffer = ''
                    candidate = False
                    continue

            buffer += page[i]
        else:
            if page[i:i+start_l] == start:
                candidate = True
                buffer += page[i]

    return result


def solution(word, pages):
    word = word.lower()
    page_list = []

    '''
    page = {
        'url' : None
        'idx' : 0,
        'basic' : 0,
        'link' : 0,
        'pointers' : [이 html을 향하는 html들의 idx]
    }

    '''
    for page in pages:

        page_dict = {
            'url' : None,
            'basic' : 0,
            'link' : 0,
            'pointers' : []
        }

        meta_tags = re('<meta', '/>', page)
        # print(meta_tags)
        link_tags = re('<a', '>', page)
        # print(link_tags)

        #find url
        url_content = meta_tags[0].split(' ')[2]
        startidx,endidx = -1,-1
        for idx,c in enumerate(url_content):
            if c=='"' and startidx == -1:
                startidx = idx
            if c=='"' and startidx != -1 and idx != startidx and endidx == -1:
                endidx = idx
        url = url_content[startidx:endidx+1]
        page_dict['url'] = url
        # print(url)


        #find link
        for link in link_tags:
            startidx,endidx = -1,-1
            for idx,c in enumerate(link):
                if c=='"' and startidx == -1:
                    startidx = idx
                if c=='"' and startidx != -1 and idx != startidx and endidx == -1:
                    endidx = idx
            link = link[startidx:endidx+1]
            # print(startidx, endidx)
            # print(link)
            page_dict['pointers'].append(link)
            page_dict['link'] += 1

    
        #basic points
        temp_html = ''
        for c in page:
            if not (c.islower() or c.isupper()):
                temp_html += ' '
            else:
                temp_html += c
        temp_html = temp_html.split(' ')
        for part in temp_html:
            if part.lower() == word:
                page_dict['basic'] += 1

        page_list.append(page_dict)

    #calculate
    points = [0 for i in range(len(page_list))]
    for idx,page in enumerate(page_list):
        points[idx] += page['basic']
        
        for link in page['pointers']:
            for target_idx, target in enumerate(page_list):
                if target['url'] == link:
                    points[target_idx] += page['basic'] / page['link']
    # print(points)

    answer = points.index(max(points))
    return answer

if __name__ == "__main__":
    # solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    # solution("abc", ["abc@abcabc"])


