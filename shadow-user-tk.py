from tkinter import *
import subprocess, re
import ctypes

win = Tk()  # creating the main window and storing the window object in 'win'
win.title('Преглед на потребител')  # setting title of the window


def get_output_as_lines(params):
    output = subprocess.Popen(params, stdout=subprocess.PIPE, startupinfo=subprocess.STARTUPINFO(
        dwFlags=subprocess.STARTF_USESHOWWINDOW,
        wShowWindow=subprocess.SW_HIDE,
    )).communicate()[0]
    return output.decode('cp866').split('\n')


def get_active_sessions():
    active_sessions = []
    for user_data in get_output_as_lines(['C:\\Windows\\system32\\query.exe', 'session'])[1:-1]:
        if "services" in user_data or "console" in user_data in user_data:
            continue
        match = re.search(r"rdp-tcp#\d+\s+(?P<name>\w+)\s+(?P<sess_id>\d+)\s+Active", user_data)
        if not match:
            continue
        user_name,sess_id = match.group("name"), match.group("sess_id")
        full_name = "?"
        for line in get_output_as_lines(['C:\\Windows\\system32\\net.exe', 'user', user_name]):
            if 'Full Name' in line:
                full_name = line[29:]

        active_sessions.append({'id': sess_id, 'user': user_name, 'name': full_name})
    return active_sessions


def shadow_session(sess_id):
    print(sess_id)
    control = not view_only.get()
    params = ['C:\\Windows\\system32\\mstsc.exe', '/shadow:' + str(sess_id), '/noconsentprompt'] + (
        ['/control'] if control else [])
    subprocess.Popen(params, stdout=subprocess.PIPE)
    exit(0)


sessions = get_active_sessions()
view_only = BooleanVar(value=True)
c1 = Checkbutton(win, text='Само преглед', variable=view_only, onvalue=True, offvalue=False)
c1.pack()

for session in sessions:
    Button(win, command=lambda sess_id=session['id']: shadow_session(sess_id), text=session['name'], height=1,
           width=30).pack()

win.mainloop()
