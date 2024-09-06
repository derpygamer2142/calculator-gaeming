# import ti_draw # type: ignore

# ti_draw.clear()
# ti_draw.set_color(0,0,0)
# ti_draw.set_pen("thick","solid")
# ti_draw.set_window(-100,100,-100,100)
# ti_draw.fill_rect(-15,-15,30,30)
# ti_draw.show_draw()
import ti_image # type: ignore
def tx(x): return ((x+100)/200)*319
def ty(y): return ((y+100)/200)*209
ti_image.load_image("DOG")
ti_image.show_image(tx(-50),ty(-50))
ti_image.show_screen()