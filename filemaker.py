def create():
    f = open('img.ppm', 'w+')
    f.write('P3 500 500 255\n')
    f.close

    f = open('img.ppm', 'a+')
    for a in range(0,500):  
        for c in range(0,500):
            r = (a-c) % 64
            g = (a-c) % 128 
            b = (a-c) % 256
            f.write('%d %d %d\n' % (r, g, b))
    f.close

create()
