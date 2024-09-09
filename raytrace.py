import math, ti_draw # type: ignore

def norm(v):
    mag=math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return [v[0]/mag,v[1]/mag,v[2]/mag]

def mv(v,s):
    return [v[0]*s,v[1]*s,v[2]*s]

def sv(v,b):
    return [v[0]-b[0],v[1]-b[1],v[2]-b[2]]

def av(v,b):
    return [v[0]+b[0],v[1]+b[1],v[2]+b[2]]

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
    dist=srt(ro,rv,[0,0,100],65)
    if (dist[1]<0): return [None]
    elif (dist[0]<0): return mv(rv,dist[1])
    else: return mv(rv,dist[0])

def mx(x): return x-160
def my(y): return y-105




focalLength=120
res=int(input("Resolution? "))
renderDist=300
dim=[319,209] 

epsilon=0.001
#densities=".:-=+*#%@"
densities=".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao#MW&8%B@$"
lv=norm([1,1,1])
ti_draw.clear()

for yi in range(0,dim[1]+1,res):
    y=my(yi)
    #output=""
    for xi in range(0,dim[0]+1,res):
        x=mx(xi)
        rv=norm([x,y,focalLength])
        rp=sp([0,0,0],rv)
        if (rp[0] != None):
            #hit
            n=norm(sv([0,0,100],rp))
            half=norm(av(lv,rv))
            specular=math.pow(max(dot(half,n),0),16)
            l=max(max(dot(n,lv),0)+specular,0)#(dot(n,lv)+1)/2  
            del n, specular, half
            try:
                ti_draw.set_color(math.floor(l*254),math.floor(l*254),math.floor(l*254))
            except:
                raise Exception(str(math.floor(l*254)))
            
            #output+=densities[round((l+1)/2*(len(densities)-1))]
            #output+="x"
        else:
            # output+="."
            ti_draw.set_color(0,0,0)
        ti_draw.fill_rect(xi,yi,res+1,res+1)
        del x, rv, rp
        # output+=" "

    #print(output)

ti_draw.show_draw()
