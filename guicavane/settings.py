#!/usr/bin/env python
# encoding: utf-8

"""
Settings. Manages the gui of the settings.
"""

import gtk
from constants import SETTINGS_GUI_FILE


class Settings(object):
    """
    Settings interface manager.
    """

    def __init__(self, config):
        """
        Creates the window and initializes the attributes.
        """

        # Gtk builder
        self.builder = gtk.Builder()
        self.builder.add_from_file(SETTINGS_GUI_FILE)
        self.builder.connect_signals(self)

        # Config
        self.config = config

        # Widgets
        self.main_dialog = self.builder.get_object("settingsDialog")
        self.player_button = self.builder.get_object("playerLocationButton")
        self.player_arguments = self.builder.get_object("playerArgumentsEntry")
        self.mega_user_entry = self.builder.get_object("megauploadUserEntry")
        self.mega_pass_entry = self.builder.get_object("megauploadPassEntry")
        self.cuevana_user_entry = self.builder.get_object("cuevanaUserEntry")
        self.cuevana_pass_entry = self.builder.get_object("cuevanaPassEntry")
        self.cache_dir_button = self.builder.get_object("cachedirButton")
        self.automatic_marks_button = self.builder.get_object("automaticMarks")
        self.cached_percentage = self.builder.get_object("cachePercentage")
        self.cache_on_movies = self.builder.get_object("cacheOnMovies")
        self.filename_template = self.builder.get_object("filenameTemplate")

        for i in range(0, 100, 10):
            self.cached_percentage.add_mark(i, gtk.POS_TOP, "")

    def show(self):
        """
        Shows the window with the values correctly asigned.
        """

        # Get the config values
        player_location = self.config.get_key("player_location")
        player_arguments = self.config.get_key("player_arguments")
        mega_user = self.config.get_key("mega_user")
        mega_pass = self.config.get_key("mega_pass")
        cuevana_user = self.config.get_key("cuevana_user")
        cuevana_pass = self.config.get_key("cuevana_pass")
        cache_dir = self.config.get_key("cache_dir")
        automatic_marks = self.config.get_key("automatic_marks")
        cached_percentage = self.config.get_key("cached_percentage")
        cache_on_movies = self.config.get_key("cached_percentage_on_movies")
        filename_template = self.config.get_key("filename_template")

        # Set the values
        self.player_button.set_filename(player_location)
        self.player_arguments.set_text(player_arguments)
        self.mega_user_entry.set_text(mega_user)
        self.mega_pass_entry.set_text(mega_pass)
        self.cuevana_user_entry.set_text(cuevana_user)
        self.cuevana_pass_entry.set_text(cuevana_pass)
        self.cache_dir_button.set_filename(cache_dir)
        self.automatic_marks_button.set_active(automatic_marks)
        self.cached_percentage.set_value(cached_percentage)
        self.cache_on_movies.set_active(cache_on_movies)
        self.filename_template.set_text(filename_template)

        # Show the dialog and hide on close
        self.main_dialog.run()
        self.main_dialog.hide()

    def _on_save_settings(self, *args):
        """
        Saves the settings to the disk.
        """

        # Get the values
        player_location = self.player_button.get_filename()
        player_arguments = self.player_arguments.get_text()
        mega_user = self.mega_user_entry.get_text()
        mega_pass = self.mega_pass_entry.get_text()
        cuevana_user = self.cuevana_user_entry.get_text()
        cuevana_pass = self.cuevana_pass_entry.get_text()
        cache_dir = self.cache_dir_button.get_filename()
        automatic_marks = self.automatic_marks_button.get_active()
        cached_percentage = self.cached_percentage.get_value()
        cache_on_movies = self.cache_on_movies.get_active()
        filename_template = self.filename_template.get_text()

        # Save the new values to the config
        self.config.set_key("player_location", player_location)
        self.config.set_key("mega_user", mega_user)
        self.config.set_key("mega_pass", mega_pass)
        self.config.set_key("cuevana_user", cuevana_user)
        self.config.set_key("cuevana_pass", cuevana_pass)
        self.config.set_key("cache_dir", cache_dir)
        self.config.set_key("automatic_marks", automatic_marks)
        self.config.set_key("cached_percentage", cached_percentage)
        self.config.set_key("player_arguments", player_arguments)
        self.config.set_key("cached_percentage_on_movies", cache_on_movies)
        self.config.set_key("filename_template", filename_template)
        self.config.save()

        # Hide the dialog
        self.main_dialog.hide()
