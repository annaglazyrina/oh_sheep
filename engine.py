import libtcodpy as libtcod


def main():
    screen_width = 80
    screen_height = 50

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'Oh, Sheep!', False)

    con = libtcod.console_new(screen_width, screen_height)
    panel = libtcod.console_new(screen_width, panel_height)

if __name__ == '__main__':
    main()
