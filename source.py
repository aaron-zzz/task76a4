def f_3fc2849(a,b,c,d,e,f):
    return (a*b-c*d*e-f)%10
def f_404f934(a,b,c):
    return (a*b*c+f_3fc2849(a,b,c,795,8,396))%10
def f_4829a46(a,b):
    return (a*b+f_404f934(a,b,245)+f_3fc2849(a,b,164,482,679,900))%10
def f_5e65c19(a,b,c):
    return (a-b-c+f_404f934(a,b,c))%10
def f_3e77575(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e*f-g+h+i+j+f_404f934(a,b,c)+f_404f934(a,b,c))%10
def f_11e6a4f(a,b,c,d,e,f):
    return (a-b-c-d-e+f+f_4829a46(a,b)+f_4829a46(a,b)+f_3fc2849(a,b,c,d,e,f))%10
def f_276f04f(a,b,c,d):
    return (a-b*c*d+f_3fc2849(a,b,c,d,520,699)+f_11e6a4f(a,b,c,d,959,507)+f_4829a46(a,b))%10
def f_44bbc00(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c+d+e-f*g-h-i+j+f_404f934(a,b,c)+f_11e6a4f(a,b,c,d,e,f)+f_276f04f(a,b,c,d))%10
def f_323e173(a,b,c,d,e,f,g,h):
    return (a*b-c*d+e*f-g+h+f_4829a46(a,b)+f_44bbc00(a,b,c,d,e,f,g,h,181,670)+f_276f04f(a,b,c,d))%10
def f_10a1d56(a):
    return (a+f_404f934(a,111,188))%10
def f_1537206(a,b,c,d,e,f):
    return (a+b+c-d*e+f+f_44bbc00(a,b,c,d,e,f,188,162,484,148))%10
def f_1543215(a,b,c):
    return (a*b*c+f_10a1d56(a)+f_44bbc00(a,b,c,818,340,752,392,516,415,260)+f_11e6a4f(a,b,c,238,530,556))%10
def f_70450f(a,b):
    return (a-b+f_4829a46(a,b))%10
def f_21e3b2e(a,b,c,d,e,f,g,h):
    return (a*b-c-d+e*f-g*h+f_276f04f(a,b,c,d)+f_11e6a4f(a,b,c,d,e,f)+f_5e65c19(a,b,c))%10
def f_3179eb1(a,b,c,d,e,f,g,h,i):
    return (a+b+c*d*e+f-g+h+i+f_4829a46(a,b)+f_404f934(a,b,c))%10
def f_5d6c325(a,b,c):
    return (a*b-c+f_3e77575(a,b,c,315,576,486,967,184,2,338)+f_70450f(a,b)+f_323e173(a,b,c,475,446,859,898,485))%10
def f_3baeede(a,b,c,d,e,f,g,h,i):
    return (a*b*c-d+e-f+g+h+i+f_3179eb1(a,b,c,d,e,f,g,h,i)+f_44bbc00(a,b,c,d,e,f,g,h,i,335)+f_3fc2849(a,b,c,d,e,f))%10
def f_60d002(a,b,c):
    return (a+b+c+f_11e6a4f(a,b,c,505,283,95)+f_3e77575(a,b,c,231,536,582,911,319,606,57))%10
def f_982326(a,b):
    return (a-b+f_1543215(a,b,550)+f_3e77575(a,b,48,38,333,831,333,905,226,411))%10
def f_516909d(a,b,c,d):
    return (a*b*c*d+f_276f04f(a,b,c,d)+f_21e3b2e(a,b,c,d,456,891,598,573)+f_5e65c19(a,b,c))%10
def f_434092a(a,b,c,d,e,f,g,h,i,j):
    return (a-b*c+d-e+f+g*h*i+j+f_5e65c19(a,b,c)+f_516909d(a,b,c,d)+f_5d6c325(a,b,c))%10
def f_95c5a4(a,b):
    return (a*b+f_434092a(a,b,565,793,600,255,136,291,472,773)+f_11e6a4f(a,b,155,641,756,593))%10
