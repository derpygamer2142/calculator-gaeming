import math

def norm(v):
    mag=math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return [v[0]/mag,v[1]/mag,v[2]/mag]

def mv(v,s):
    return [v[0]*s,v[1]*s,v[2]*s]

def sv(v,b):
    return [v[0]-b[0],v[1]-b[1],v[2]-b[2]]

def dot(a,b):
    return (a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])
def s(rp,sp,rad):
    return math.sqrt(((sp[0]-rp[0])**2)+((sp[1]-rp[1])**2)+((sp[2]-rp[2])**2))-rad

def srt(ro,rd,ce,ra): # https://iquilezles.org/articles/intersectors/
    oc = sv(ro,ce)
    b=dot(oc,rd)
    c=dot(oc,oc)-(ra**2)
    h=(b**2)-c
    if (h<0): return [-1.,-1.]
    h=math.sqrt(h)
    return [-b-h,-b+h]

def sp(ro,rv):
    dist=srt(ro,rv,[0,0,100],55)
    if (dist[1]<0): return [None]
    elif (dist[0]<0): return mv(rv,dist[1])
    else: return mv(rv,dist[0])

focalLength=120
res=8
renderDist=300
dim=[100,100]
epsilon=0.001
#densities=".:-=+*#%@"
densities=".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao#MW&8%B@$"
lv=norm([1,1,1])
for yi in range(-res,res):
    y=(yi/res)*dim[1]
    output=""
    for xi in range(-res,res):
        x=(xi/res)*dim[0]
        rv=norm([x,y,focalLength])
        rp=sp([0,0,0],rv)
        if (rp[0] != None):
            #hit
            n=norm(sv([0,0,100],rp))
            l=dot(n,lv)
            output+=densities[round((l+1)/2*(len(densities)-1))]
            #output+="x"
        else:
            output+="."
        output+=" "

    print(output)