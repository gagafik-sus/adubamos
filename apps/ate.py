import os
import curses
import locale

locale.setlocale(locale.LC_ALL, "")

TITLE = "adubam text editor v0.1"
LICENSE_TEXT = "MIT License Copyright 2026 @adubam"


def load_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = f.read().splitlines()
        return data if data else [""]
    return [""]


def save_file(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def safe_addstr(stdscr, y, x, text):
    h, w = stdscr.getmaxyx()
    if y < 0 or y >= h or x >= w:
        return
    try:
        stdscr.addstr(y, x, text[:max(0, w - x - 1)])
    except:
        pass


def make_header(width, filename):
    full_left = f"{TITLE}█file {filename}"
    short_left = f"file {filename}"

    if width >= len(full_left) + len(LICENSE_TEXT) + 4:
        fill = "█" * max(0, width - len(full_left) - len(LICENSE_TEXT) - 1)
        return (full_left + fill + LICENSE_TEXT)[:width - 1]

    if width >= len(short_left) + len(LICENSE_TEXT) + 4:
        fill = "█" * max(0, width - len(short_left) - len(LICENSE_TEXT) - 1)
        return (short_left + fill + LICENSE_TEXT)[:width - 1]

    if width >= len(short_left) + 2:
        return short_left[:width - 1]

    return "f"[:width - 1]


def make_footer(width, status):
    if width >= 70:
        footer = "^E-exit # ^S-save # ^X-save+exit # ^C-copy line # ^V-paste line"
    elif width >= 36:
        footer = "^E-exit ^S-save ^X-save+exit"
    elif width >= 18:
        footer = "^E ^S ^X"
    else:
        footer = ""

    if status:
        if footer:
            footer += " | " + status
        else:
            footer = status

    return footer[:max(0, width - 1)]


def draw_editor(stdscr, filename, lines, cx, cy, scroll_y, scroll_x, status):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    safe_addstr(stdscr, 0, 0, make_header(w, filename))

    if h >= 2:
        safe_addstr(stdscr, 1, 0, "▒" * max(0, w - 1))

    editor_top = 2
    editor_bottom = h - 3
    visible_height = max(1, editor_bottom - editor_top + 1)

    if h >= 5:
        for i in range(visible_height):
            line_index = scroll_y + i
            y = editor_top + i
            if line_index < len(lines):
                line = lines[line_index]
                visible = line[scroll_x:scroll_x + max(1, w - 1)]
                safe_addstr(stdscr, y, 0, visible)

        safe_addstr(stdscr, h - 2, 0, "▒" * max(0, w - 1))
        safe_addstr(stdscr, h - 1, 0, make_footer(w, status))

        screen_y = editor_top + (cy - scroll_y)
        screen_x = cx - scroll_x

        if editor_top <= screen_y <= editor_bottom and 0 <= screen_x < w - 1:
            try:
                stdscr.move(screen_y, screen_x)
            except:
                pass
    else:
        mini = f"{cy + 1}:{cx + 1}"
        if status:
            mini += " " + status
        if h >= 2:
            safe_addstr(stdscr, h - 1, 0, mini[:max(0, w - 1)])

    stdscr.refresh()


def editor(stdscr, filename):
    curses.raw()
    curses.noecho()
    stdscr.keypad(True)

    lines = load_file(filename)
    cx = 0
    cy = 0
    scroll_y = 0
    scroll_x = 0
    clipboard = ""
    status = "opened"

    while True:
        h, w = stdscr.getmaxyx()
        editor_top = 2
        editor_bottom = h - 3
        visible_height = max(1, editor_bottom - editor_top + 1)
        visible_width = max(1, w - 1)

        cx = min(cx, len(lines[cy]))

        if cy < scroll_y:
            scroll_y = cy
        elif cy >= scroll_y + visible_height:
            scroll_y = cy - visible_height + 1

        if cx < scroll_x:
            scroll_x = cx
        elif cx >= scroll_x + visible_width:
            scroll_x = cx - visible_width + 1

        draw_editor(stdscr, filename, lines, cx, cy, scroll_y, scroll_x, status)
        status = ""

        try:
            ch = stdscr.get_wch()
        except:
            continue

        if ch in ("\x05", 5):
            break

        elif ch in ("\x13", 19):
            try:
                save_file(filename, lines)
                status = "saved"
            except Exception as e:
                status = f"save error: {e}"

        elif ch in ("\x18", 24):
            try:
                save_file(filename, lines)
                status = "saved"
            except Exception as e:
                status = f"save error: {e}"
            break

        elif ch in ("\x03", 3):
            clipboard = lines[cy]
            status = "copied line"

        elif ch in ("\x16", 22):
            lines.insert(cy + 1, clipboard)
            cy += 1
            cx = min(cx, len(lines[cy]))
            status = "pasted line"

        elif ch in (curses.KEY_BACKSPACE, "\x7f", "\b", 127, 8):
            if cx > 0:
                lines[cy] = lines[cy][:cx - 1] + lines[cy][cx:]
                cx -= 1
            elif cy > 0:
                prev_len = len(lines[cy - 1])
                lines[cy - 1] += lines[cy]
                del lines[cy]
                cy -= 1
                cx = prev_len

        elif ch in ("\n", "\r", curses.KEY_ENTER, 10, 13):
            current = lines[cy]
            left = current[:cx]
            right = current[cx:]
            lines[cy] = left
            lines.insert(cy + 1, right)
            cy += 1
            cx = 0

        elif ch == curses.KEY_LEFT:
            if cx > 0:
                cx -= 1
            elif cy > 0:
                cy -= 1
                cx = len(lines[cy])

        elif ch == curses.KEY_RIGHT:
            if cx < len(lines[cy]):
                cx += 1
            elif cy < len(lines) - 1:
                cy += 1
                cx = 0

        elif ch == curses.KEY_UP:
            if cy > 0:
                cy -= 1
                cx = min(cx, len(lines[cy]))

        elif ch == curses.KEY_DOWN:
            if cy < len(lines) - 1:
                cy += 1
                cx = min(cx, len(lines[cy]))

        elif ch == curses.KEY_HOME:
            cx = 0

        elif ch == curses.KEY_END:
            cx = len(lines[cy])

        elif ch == curses.KEY_PPAGE:
            cy = max(0, cy - visible_height)
            cx = min(cx, len(lines[cy]))

        elif ch == curses.KEY_NPAGE:
            cy = min(len(lines) - 1, cy + visible_height)
            cx = min(cx, len(lines[cy]))

        elif ch in ("\t", 9):
            lines[cy] = lines[cy][:cx] + "    " + lines[cy][cx:]
            cx += 4

        elif isinstance(ch, str) and ch.isprintable():
            lines[cy] = lines[cy][:cx] + ch + lines[cy][cx:]
            cx += 1


if not args:
    print("usage: ate <file>")
else:
    filename = args[0]

    try:
        open(filename, "a", encoding="utf-8").close()
    except Exception as e:
        print("error:", e)
    else:
        curses.wrapper(lambda stdscr: editor(stdscr, filename))
