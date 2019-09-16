
#cache = [가장 오래된 참조영역 ~~~~~ 가장 최근 참조영역]

def solution(cacheSize, cities):
    cache = []
    time = 0

    for city in cities:
        city = city.lower() #소문자로 통일

        if cacheSize>0:
            #cache hit
            if city in cache:
                idx = cache.index(city)
                elem = cache.pop(idx)
                cache.append(elem)
                time += 1

            #cache miss
            else: #pop most Least Recently Used
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time+=5
        else:
            time+=5

    answer = time
    return answer