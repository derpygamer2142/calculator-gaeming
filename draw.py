# import ti_draw # type: ignore

# ti_draw.clear()
# ti_draw.set_color(0,0,0)
# ti_draw.set_pen("thick","solid")
# ti_draw.set_window(-100,100,-100,100)
# ti_draw.fill_rect(-15,-15,30,30)
# ti_draw.show_draw()
import ti_image # type: ignore
def tx(x): return x+160
def ty(y): return 105-y
ti_image.clear_image()
ti_image.set_pixel(tx(0),ty(0),(255,0,0))
ti_image.set_pixel(tx(-1),ty(0),(255,0,0))
ti_image.set_pixel(tx(1),ty(0),(255,0,0))
ti_image.set_pixel(tx(0),ty(-1),(255,0,0))
ti_image.set_pixel(tx(0),ty(1),(255,0,0))
ti_image.show_screen()