square_size = 500
square_count = 10
square_rows = 4

w = square_size/2 * (square_count)
h = square_size/2 * (square_rows)

colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]

def draw_polaroid():
    # Draw Shadow
    noStroke()
    fill(30, 30, 30, 6)
    for i in range(30):
        rect(-square_size/2 + i*2 - square_size/90, -square_size/2 + i*2 - square_size/90, square_size/2 - i*4 + square_size/30, square_size/2 - i*4 + square_size/30)

    # Frame
    fill(220, 220, 220)
    rect(-square_size/2, -square_size/2, square_size/2, square_size/2 )
    
    # Color
    c = colors[int(random(len(colors)))]
    fill(c[0], c[1], c[2], 255)
    # fill(random(50, 100), random(50, 180), random(50, 180))
    rect(-square_size/2 + square_size/50, -square_size/2 + square_size/50, square_size/2 - square_size/25, square_size/2 - square_size/10)
    
    
def setup():
    size(w, h)
    background(200, 200, 200)
    
    # Add texture to background
    noStroke()
    fill(255, 255, 255, 4)
    for i in range(200000):
        circle(random(w), random(h), random(5)) 
    
    pixelDensity(2)
    
    translate(square_size/2, square_size/2)
    for i in range(square_rows):
        for j in range(square_count):
            if (random(1) < .8):
                pushMatrix()
                translate(j * square_size/2, i * square_size/2)
                rotate(random(-.1, .1))
                draw_polaroid()
                popMatrix()

    save("Examples/Pol.png")
