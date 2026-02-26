#!/usr/bin/env python3

import os
import subprocess
import threading

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw, GLib


# main window
class ArtsCrawlerWindow(Adw.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_default_size(520, 320)

        # root vertical layout
        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(root)

        # header bar (do NOT call set_titlebar on AdwApplicationWindow)
        header = Adw.HeaderBar()
        header.set_title_widget(Gtk.Label(label="Arts Image Downloader"))
        root.append(header)

        # main content box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        box.set_margin_top(24)
        box.set_margin_bottom(24)
        box.set_margin_start(24)
        box.set_margin_end(24)
        root.append(box)

        # title label
        title = Gtk.Label(label="Download from Google Arts & Culture")
        title.add_css_class("title-3")
        box.append(title)

        # url entry
        self.url_entry = Gtk.Entry()
        self.url_entry.set_placeholder_text("paste image url here")
        box.append(self.url_entry)

        # download button
        self.download_btn = Gtk.Button(label="Download")
        self.download_btn.add_css_class("suggested-action")
        self.download_btn.connect("clicked", self.on_download_clicked)
        box.append(self.download_btn)

        # progress bar
        self.progress = Gtk.ProgressBar()
        self.progress.set_show_text(True)
        self.progress.set_text("")
        box.append(self.progress)

        # open output button
        self.open_btn = Gtk.Button(label="Open Output")
        self.open_btn.connect("clicked", self.on_open_output)
        box.append(self.open_btn)

        # status label
        self.status = Gtk.Label(label="")
        self.status.set_wrap(True)
        box.append(self.status)

    # user pressed download
    def on_download_clicked(self, button):
        url = self.url_entry.get_text().strip()

        if not url:
            self.status.set_text("please enter a url")
            return

        # disable button while running
        self.download_btn.set_sensitive(False)
        self.status.set_text("starting download...")

        # start pulsing progress
        self.progress.set_fraction(0.0)
        self.progress.set_text("working...")
        self.pulse_id = GLib.timeout_add(120, self._pulse_progress)

        # run crawler in background thread
        thread = threading.Thread(target=self._run_crawler, args=(url,))
        thread.daemon = True
        thread.start()

    # pulse animation while working
    def _pulse_progress(self):
        self.progress.pulse()
        return True

    # run backend script
    def _run_crawler(self, url):
        try:
            # path when running from source tree
            local_path = os.path.join(os.path.dirname(__file__), "crawler.py")

            # path when installed via package
            system_path = "/usr/share/arts-crawler/crawler.py"

            if os.path.exists(local_path):
                crawler_path = local_path
            else:
                crawler_path = system_path

            cmd = [
                "python3",
                crawler_path,
                "--url",
                url,
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )

            GLib.idle_add(self._on_download_finished, result)

        except Exception as e:
            GLib.idle_add(self._on_download_error, str(e))

    # success or failure handler
    def _on_download_finished(self, result):
        if hasattr(self, "pulse_id"):
            GLib.source_remove(self.pulse_id)

        self.progress.set_fraction(1.0)
        self.download_btn.set_sensitive(True)

        if result.returncode == 0:
            self.progress.set_text("done")
            self.status.set_text("download complete")
        else:
            self.progress.set_text("failed")
            err = result.stderr.strip() or "download failed"
            self.status.set_text(err)

    # unexpected error
    def _on_download_error(self, message):
        if hasattr(self, "pulse_id"):
            GLib.source_remove(self.pulse_id)

        self.progress.set_text("error")
        self.download_btn.set_sensitive(True)
        self.status.set_text(message)

    # open output folder
    def on_open_output(self, button):
        local_out = os.path.join(os.path.dirname(__file__), "output")
        system_out = "/usr/share/arts-crawler/output"

        if os.path.exists(local_out):
            path = local_out
        else:
            path = system_out

        subprocess.Popen(["xdg-open", path])


# app class
class ArtsCrawlerApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="org.example.ArtsCrawler")

    def do_activate(self):
        win = ArtsCrawlerWindow(self)
        win.present()


def main():
    app = ArtsCrawlerApp()
    app.run()


if __name__ == "__main__":
    main()


