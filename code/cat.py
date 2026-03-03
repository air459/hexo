import sys
from Xlib import display, X
from Xlib.protocol import rq


def is_xfce4_terminal_fullscreen_xlib():
    d = display.Display()
    root = d.screen().root

    win_list = []

    def traverse_windows(win):
        attrs = win.get_wm_class()
        if attrs and attrs[1] == "Xfce4-terminal":
            win_list.append(win)
        for child in win.query_tree().children:
            traverse_windows(child)

    traverse_windows(root)

    if not win_list:
        return False

    net_wm_state = d.intern_atom("_NET_WM_STATE")
    net_wm_state_fullscreen = d.intern_atom("_NET_WM_STATE_FULLSCREEN")

    win = win_list[0]
    prop = win.get_property(net_wm_state, X.AnyPropertyType, 0, 1024)
    if not prop or not prop.value:
        return False

    return net_wm_state_fullscreen in prop.value


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "!":
        print(is_xfce4_terminal_fullscreen_xlib())
    else:
        print("Xfce4-terminal " + str(is_xfce4_terminal_fullscreen_xlib()))
