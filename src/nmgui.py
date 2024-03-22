import gi
import subprocess
import threading
try:
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GLib
except ModuleNotFoundError:
    print("Error: Required module 'gi' not found. Please install it.")
    sys.exit(1)

class NMGui(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Network Manager")
        self.set_border_width(10)
        self.maximize()

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.add(scrolled_window)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
        scrolled_window.add(self.grid)

        self.label_nm = Gtk.Label(label="NMGui")
        self.grid.attach(self.label_nm, 0, 0, 3, 1)

        self.label = Gtk.Label(label="Network Connections")
        self.grid.attach(self.label, 0, 1, 3, 1)

        self.liststore = Gtk.ListStore(str, str)
        self.network_list = Gtk.TreeView(model=self.liststore)
        self.network_list.set_hexpand(True)

        renderer_text = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Connection", renderer_text, text=0)
        self.network_list.append_column(column)

        column = Gtk.TreeViewColumn("Type", renderer_text, text=1)
        self.network_list.append_column(column)

        self.grid.attach(self.network_list, 0, 2, 3, 1)

        self.refresh_button = Gtk.Button(label="Refresh")
        self.refresh_button.connect("clicked", self.refresh_clicked)
        self.grid.attach(self.refresh_button, 0, 3, 1, 1)

        self.connect_button = Gtk.Button(label="Connect")
        self.connect_button.connect("clicked", self.connect_clicked)
        self.grid.attach(self.connect_button, 1, 3, 1, 1)

        self.disconnect_button = Gtk.Button(label="Disconnect")
        self.disconnect_button.connect("clicked", self.disconnect_clicked)
        self.grid.attach(self.disconnect_button, 2, 3, 1, 1)

        self.autorefresh = True
        GLib.timeout_add_seconds(5, self.auto_refresh)

        self.refresh_clicked(None)

    def refresh_clicked(self, widget):
        self.liststore.clear()
        output = subprocess.check_output(["nmcli", "-t", "-f", "name,type", "connection", "show"]).decode("utf-8")
        connections = output.strip().split('\n')
        for connection in connections:
            name, type = connection.split(':')
            self.liststore.append([name, type])

    def connect_clicked(self, widget):
        selected_iter = self.network_list.get_selection().get_selected()[1]
        if selected_iter is not None:
            connection_name = self.liststore[selected_iter][0]
            threading.Thread(target=self.connect_network, args=(connection_name,)).start()

    def connect_network(self, connection_name):
        try:
            subprocess.check_call(["nmcli", "connection", "up", connection_name])
            GLib.idle_add(self.send_notify, f"Successfully connected to {connection_name}")
        except subprocess.CalledProcessError as e:
            GLib.idle_add(self.send_notify, f"Failed to connect to {connection_name}: {e}")

    def disconnect_clicked(self, widget):
        selected_iter = self.network_list.get_selection().get_selected()[1]
        if selected_iter is not None:
            connection_name = self.liststore[selected_iter][0]
            subprocess.call(["nmcli", "connection", "down", connection_name])
            self.send_notify(f"Disconnected from {connection_name}")

    def auto_refresh(self):
        if self.autorefresh:
            self.refresh_clicked(None)
            return True
        else:
            return False

    def send_notify(self, message):
        subprocess.call(["notify-send", "NMGUI", message])

win = NMGui()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
