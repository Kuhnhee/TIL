# SSAFY python basic (190719)

### gitlab

우측상단 `+` -> new project (repository 개념)

project name : LEE_KUHN_HEE

```shell
cd hw_ws
git init
git add .
git commit -m "first commit"
git remote add origin https://lab.ssafy.com/sheva0902/lee_kuhn_hee.git
git remote -v #확인
git push -u origin master #사용자 이름:sheva0902 / 비번: gitlab 비번
```

---

### 최대공약수, 최소공배수 구하기

GCD를 구할 때에는 유클리드 호제법을 사용한다.

```python
# Non recursive way
def gcdlcm(x, y):
    m, n = max(x,y), min(x,y)
    while n>0:
        m, n = n, m%n
    return [m, int(a*b/m)]

# Recursive solution for gcd
def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n%m)
def gcdlcm2(n,m):
    g = gcd(n,m)
    l = (n*m)//g
    return [g, l]
```

