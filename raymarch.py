import math
def s(rp,sp,rad):
    return math.sqrt(((sp[0]-rp[0])**2)+((sp[1]-rp[1])**2)+((sp[2]-rp[2])**2))-rad

def norm(v):
    mag=math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return [v[0]/mag,v[1]/mag,v[2]/mag]

def mv(v,s):
    return [v[0]*s,v[1]*s,v[2]*s]

def sv(v,b):
    return [v[0]-b[0],v[1]-b[1],v[2]-b[2]]

def dot(a,b):
    return (a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])

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
        rayLen=0
        dist=99999
        while (dist>epsilon) and (rayLen<renderDist):
            dist=min(s(mv(rv,rayLen),[0,0,100],55),dist)
            rayLen+=dist
        if dist<=epsilon:
            n=norm(sv([0,0,100],mv(rv,rayLen)))
            l=dot(n,lv)
            #print((l+1)/2)
            output+=densities[round((l+1)/2*(len(densities)-1))]
            
        else:
            output+="."
    print(output)