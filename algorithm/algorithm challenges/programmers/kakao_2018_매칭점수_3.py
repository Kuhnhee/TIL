import re

def solution(word, pages):
    answer = 0
    meta_parser = re.compile('<meta(.+?)/>')
    print(meta_parser)
    a_parser = re.compile('<a(.+?)>')
    page_infos = []
    for page in pages:
        page_dict = dict()
        a_tags = a_parser.findall(page)
        print(a_tags)
        outer_url = []
        for a_tag in a_tags:
            first_idx = end_idx = -1
            for idx, char in enumerate(a_tag):
                if char == '"':
                    if first_idx == -1:
                        first_idx = idx
                    elif end_idx == -1:
                        end_idx = idx
            outer_url.append(a_tag[first_idx+1:end_idx])
        meta_tag = meta_parser.search(page).group()
        content_prop = meta_tag.split(' ')[2]
        first_idx = end_idx = -1
        for idx, char in enumerate(content_prop):
            if char == '"':
                if first_idx == -1:
                    first_idx = idx
                elif end_idx == -1:
                    end_idx = idx
        url = content_prop[first_idx+1: end_idx]
        page_dict['outer_url_list'] = outer_url
        page_dict['url'] = url
        page_dict['keyword_point'] = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
        page_dict['link_point'] = 0
        page_infos.append(page_dict)
    for page_info in page_infos:
        for outer_url in page_info['outer_url_list']:
            for outer_url_page_candidate in page_infos:
                if outer_url == outer_url_page_candidate['url']:
                    outer_url_page_candidate['link_point'] += page_info['keyword_point']/len(page_info['outer_url_list'])
    point_lst = [page_info['keyword_point'] + page_info['link_point'] for page_info in page_infos]
    # print(point_lst)
    return point_lst.index(max(point_lst))

if __name__ == "__main__":
    solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    # solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    # solution("abc", ["abc@abcabc"])

