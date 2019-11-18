import graphics as gr

window = gr.GraphWin("Landscape", 640, 480)

sky = gr.Polygon(gr.Point(0, 0), gr.Point(0, 240), gr.Point(640, 240), gr.Point(640, 0))
sky.setFill(gr.color_rgb(0, 0, 200))
sky.draw(window)

land = gr.Polygon(gr.Point(0, 240), gr.Point(0, 480), gr.Point(640, 480), gr.Point(640, 240))
land.setFill(gr.color_rgb(80, 240, 20))
land.draw(window)


sun = gr.Circle(gr.Point(550, 70), 30)
sun.setFill(gr.color_rgb(255, 255, 0))
sun.draw(window)


house_body = gr.Polygon(gr.Point(100, 200), gr.Point(100, 400), gr.Point(300, 400), gr.Point(300, 200))
house_body.draw(window)
house_body.setFill(gr.color_rgb(192, 192, 192))


house_roof = gr.Polygon(gr.Point(80, 200), gr.Point(320, 200), gr.Point(200, 100))
house_roof.draw(window)
house_roof.setFill(gr.color_rgb(128, 64, 0))



window.getMouse()

window.close()
