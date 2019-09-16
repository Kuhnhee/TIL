
import re

def solution(word, pages):
    score = []  # 인덱스(0), URL(1), 기본 점수(2), 링크(3), 링크 수(4)
    for j, k in enumerate(pages):
        k = k.replace('>','>\n')
        # print(k[k.index('<head>')])
        meta = re.findall('<meta.*', k[k.index('<head>')+6:k.index('</head>')]) #head 태그 내에서 meta태그 검색
        # print(meta)
        for i in meta:
            # print(i)
            if re.findall('"https://.*"',i):
                # print(re.findall('"https://.*"',i))
                url = re.findall('"https://.*"',i)[0][1:-1]
        link = [i[9:-1] for i in re.findall('<a href="https://.*"', k)]
        cnt = re.sub('[^a-zA-Z]', ' ', k).lower().split().count(word.lower())
        score.append([j, url, cnt, link, len(link)])

    res = []
    for x in score:
        link_score = sum([y[2] / y[4] for y in score if y[0] != x[0] and x[1] in y[3]])
        res.append([x[0], x[2] + link_score])
    res.sort(key=lambda x: x[1], reverse=True)

    return res[0][0]

if __name__ == "__main__":
    # solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    # solution("abc", ["abc@abcabc"])