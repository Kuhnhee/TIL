def solution(genres, plays):

    db = {}
    for i in range(len(genres)):

        if genres[i] not in db:
            db[genres[i]] = {'total': plays[i]}
            db[genres[i]][i] = plays[i]
        else:
            db[genres[i]][i] = plays[i]
            db[genres[i]]['total'] += plays[i]

    # pprint(db)

    answer = []
    vals = db.values()
    vals = list(vals)
    vals.sort(key=lambda x:x['total'], reverse=True)

    for genre in vals:
        genre.pop('total')
        
        temp = []
        for key,val in genre.items():
            temp.append([key, val])

        temp.sort(key = lambda x:(x[1],-x[0]), reverse=True)

        # print(temp)
        for idx,a in enumerate(temp):
            answer.append(a[0])
            if idx == 1:
                break


    return answer