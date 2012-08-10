#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) Mikael Hartzell 2012
#
# This program is distributed under the GNU General Public License, version 3 (GPLv3)
#
# Check the license here: http://www.gnu.org/licenses/gpl.html
# Basically this license gives you full freedom to do what ever you wan't with this program. You are free to use, modify, distribute it any way you like.
# The only restriction is that if you make derivate works of this program AND distribute those, the derivate works must also be licensed under GPL 3.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#

import sys
import os
import subprocess
import pickle
import tkinter
import tkinter.ttk
import tkinter.filedialog
import time
import smtplib
import email
import email.mime
import email.mime.text
import email.mime.multipart
import tempfile

version = '039'

###################################
# Function definitions start here #
###################################

def call_first_frame_on_top():
	# This function can be called only from the second window.
	# Hide the second window and show the first window.
	second_frame.grid_forget()
	first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

	## Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(first_frame.winfo_reqwidth()+40) +'x'+ str(first_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
def call_second_frame_on_top():
	# This function can be called from the first and third windows.
	# Hide the first and third windows and show the second window.
	first_frame.grid_forget()
	third_frame.grid_forget()
	second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(second_frame.winfo_reqwidth()+40) +'x'+ str(second_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
def call_third_frame_on_top():
	
	# If the user comes back to this window and there is an error message displayed on the window from the last time user was here, then remove that error message.
	email_sending_message_1.set('')
	email_sending_message_2.set('')
	third_window_label_15['foreground'] = 'black'
	third_window_label_17['foreground'] = 'black'
			
	# This function can be called from two possible windows depending on did the user come here by clicking Next or Back buttons.
	# Hide the the frames for other windows and raise the one we want.
	second_frame.grid_forget()
	fourth_frame.grid_forget()
	third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(third_frame.winfo_reqwidth()+40) +'x'+ str(third_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

def call_fourth_frame_on_top():
	
	# If user clicked 'Send error messages by email' to True, then test if he has filled all needed email details and only allow him to advance to the next window is all settings are ok.
	if send_error_messages_by_email.get() == True:
		put_email_details_in_a_dictionary()
		email_settings_are_complete, error_message = test_if_email_settings_are_complete()
		if email_settings_are_complete == False:
			email_sending_message_1.set('Email settings are incomplete:')
			email_sending_message_2.set(error_message)
			third_window_label_15['foreground'] = 'red'
			third_window_label_17['foreground'] = 'red'
			return
	
	# This function can be called from two possible windows depending on did the user come here by clicking Next or Back buttons.
	# Hide the the frames for other windows and raise the one we want.
	third_frame.grid_forget()
	fifth_frame.grid_forget()
	fourth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(fourth_frame.winfo_reqwidth()+40) +'x'+ str(fourth_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

def call_fifth_frame_on_top():
	# This function can be called from two possible windows depending on did the user come here by clicking Next or Back buttons.
	# Hide the the frames for other windows and raise the one we want.
	fourth_frame.grid_forget()
	sixth_frame.grid_forget()
	fifth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(fifth_frame.winfo_reqwidth()+40) +'x'+ str(fifth_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

def call_sixth_frame_on_top():
	
	# The user may have navigated back and forth between windows and the sixth window may be incorrectly sized by an previous error message.
	# Remove the error message and update window dimensions.
	root_password_was_not_accepted_message.set('') # Remove a possible error message from the screen that remained when the user previously visited this window.
	sixth_frame.update() # Update the frame dimesions.	
	
	# If the user comes back here from window 7, empty window 7 error messages, the user will propably go back to window seven from here.
	seventh_window_label_16['foreground'] = 'dark green'
	seventh_window_label_17['foreground'] = 'dark green'
	seventh_window_message_1.set('')
	seventh_window_message_2.set('')
	
	# This function can be called from two possible windows depending on did the user come here by clicking Next or Back buttons.
	# Hide the the frames for other windows and raise the one we want.
	
	# Read samba configuration from the fifth window text label and assign configuration to a list.
	set_samba_configuration()
	fifth_frame.grid_forget()
	seventh_frame.grid_forget()
	root_password_entrybox.focus() # Set keyboard focus to the entrybox.
	sixth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(sixth_frame.winfo_reqwidth()+40) +'x'+ str(sixth_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

def call_seventh_frame_on_top():
	
	# This function can be called from two possible windows depending on did the user come here by clicking Next or Back buttons.
	# Hide the the frames for other windows and raise the one we want.
	sixth_frame.grid_forget()
	eigth_frame.grid_forget()
	ninth_frame.grid_forget()
	set_seventh_window_label_texts_and_colors()
	seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
	seventh_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

def call_eigth_frame_on_top():
	# This function can only be called from the seventh window.
	# Hide the seventh window and show the eigth window.
	seventh_frame.grid_forget()
	eigth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(eigth_frame.winfo_reqwidth()+40) +'x'+ str(eigth_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
def call_ninth_frame_on_top():
	# This function can only be called from the seventh window.
	# Hide the seventh window and show the ninth window.
	seventh_frame.grid_forget()
	ninth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(ninth_frame.winfo_reqwidth()+40) +'x'+ str(ninth_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

def quit_program():
	root_window.destroy()

def add_email_addresses_to_list(*args):
	global message_recipients
	message_recipients = []
	counter = 0
	email_addresses_list = email_addresses_string.get().split(',') # Spit user given input to a list using comma as the separator.
	for item in email_addresses_list: # Strip each item of possible extra whitespace and store each item in a new list.
		counter = counter + 1
		if counter > 5:
			break
		if not len(item) == 0: # If item lenght is 0, then the item is not valid, skip it.
			message_recipients.append(item.strip())
	# Assign each item (email address) to a separate variable thet is only used to display the item on the GUI.
	if len(message_recipients) > 0:
		email_address_1.set(message_recipients[0])
	else:
		email_address_1.set('')
	if len(message_recipients) > 1:
		email_address_2.set(message_recipients[1])
	else:
		email_address_2.set('')
	if len(message_recipients) > 2:
		email_address_3.set(message_recipients[2])
	else:
		email_address_3.set('')
	if len(message_recipients) > 3:
		email_address_4.set(message_recipients[3])
	else:
		email_address_4.set('')
	if len(message_recipients) > 4:
		email_address_5.set(message_recipients[4])
	else:
		email_address_5.set('')
		
	if debug == True:
		print()
		print('message_recipients =', message_recipients)

def enable_email_settings():
	if send_error_messages_by_email.get() == True:
		use_tls_true_button.state(['!disabled'])
		use_tls_false_button.state(['!disabled'])
		smtp_server_requires_authentication_true_button.state(['!disabled'])
		smtp_server_requires_authentications_false_button.state(['!disabled'])
		smtp_server_name_combobox.state(['!disabled'])
		smtp_server_port_combobox.state(['!disabled'])
		smtp_username_entrybox.state(['!disabled'])
		smtp_password_entrybox.state(['!disabled'])
		email_sending_interval_combobox.state(['!disabled'])
		email_address_entrybox.state(['!disabled'])
		heartbeat_true_button.state(['!disabled'])
		heartbeat_false_button.state(['!disabled'])
		heartbeat.set(True)
		third_window_send_button['state'] = 'normal'
	else:
		use_tls_true_button.state(['disabled'])
		use_tls_false_button.state(['disabled'])
		smtp_server_requires_authentication_true_button.state(['disabled'])
		smtp_server_requires_authentications_false_button.state(['disabled'])
		smtp_server_name_combobox.state(['disabled'])
		smtp_server_port_combobox.state(['disabled'])
		smtp_username_entrybox.state(['disabled'])
		smtp_password_entrybox.state(['disabled'])
		email_sending_interval_combobox.state(['disabled'])
		email_address_entrybox.state(['disabled'])
		heartbeat_true_button.state(['disabled'])
		heartbeat_false_button.state(['disabled'])
		heartbeat.set(False)
		third_window_send_button['state'] = 'disabled'
		
	if debug == True:
		true_false_string = [False, True]
		print()
		print('send_error_messages_by_email =', true_false_string[send_error_messages_by_email.get()])
		print('heartbeat =', true_false_string[heartbeat.get()])

def convert_file_expiry_time_to_seconds(*args):
	global file_expiry_time
	file_expiry_time = int(file_expiry_time_in_minutes.get()) * 60
	if debug == True:
		print()
		print('file_expiry_time (seconds) =', file_expiry_time)

def get_target_directory():
	global target_path
	target_path_from_user = tkinter.filedialog.askdirectory(mustexist=True, initialdir=target_path.get())
	target_path.set(target_path_from_user)
	
	# User given target path has changed, we need to redefine all pathnames under target dir.
	set_directory_names_according_to_language()
	
	# If the path that the user selected is long, it has changed the dimensions of our frames and root window geometry is wrong.
	# We need to find out the new dinemsions of our frames and resize the root window if needed.
	second_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(second_frame.winfo_reqwidth()+40) +'x'+ str(second_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
def set_directory_names_according_to_language():
	
	global english
	global finnish
	
	path = target_path.get()
	
	if path == os.sep:
		path = ''
		
	directory_for_temporary_files.set(os.path.normpath(path + os.sep + '00-Loudness_Calculation_Temporary_Files'))
	
	if language.get() == 'english':
		hotfolder_name_to_use = 'LoudnessCorrection'
		english = 1
		finnish = 0
		hotfolder_path.set(os.path.normpath(path + os.sep + hotfolder_name_to_use))
		directory_for_results.set(hotfolder_path.get() + os.sep + '00-Corrected_Files')
		web_page_path.set(hotfolder_path.get() + os.sep + '00-Calculation_Queue_Information')
		web_page_name.set('00-Calculation_Queue_Information.html')
		# For display the directory names were saved in a truncated form, update names.
		hotfolder_path_truncated_for_display.set('Target Directory '  + os.sep + ' ' + hotfolder_name_to_use)
		directory_for_results_truncated_for_display.set('Target Directory ' + os.sep + ' ' + hotfolder_name_to_use + ' ' + os.sep + ' 00-Corrected_Files')
		web_page_path_truncated_for_display.set('Target Directory ' + os.sep + ' ' + hotfolder_name_to_use + ' ' + os.sep + ' 00-Calculation_Queue_Information')
	else:
		hotfolder_name_to_use = 'AanekkyysKorjaus'
		english = 0
		finnish = 1
		hotfolder_path.set(os.path.normpath(path + os.sep + hotfolder_name_to_use))
		directory_for_results.set(hotfolder_path.get() + os.sep + '00-Korjatut_Tiedostot')
		web_page_path.set(hotfolder_path.get() + os.sep + '00-Laskentajonon_Tiedot')
		web_page_name.set('00-Laskentajonon_Tiedot.html')
		# For display the directory names were saved in a truncated form, update names.
		hotfolder_path_truncated_for_display.set('Target Directory '  + os.sep + ' ' + hotfolder_name_to_use)
		directory_for_results_truncated_for_display.set('Target Directory ' + os.sep + ' ' + hotfolder_name_to_use + ' ' + os.sep + ' 00-Korjatut_Tiedostot')
		web_page_path_truncated_for_display.set('Target Directory ' + os.sep + ' ' + hotfolder_name_to_use + ' ' + os.sep + ' 00-Laskentajonon_Tiedot')
	
	directory_for_temporary_files_truncated_for_display.set('Target Directory ' + os.sep + ' 00-Loudness_Calculation_Temporary_Files')
	directory_for_error_logs.set(path + os.sep + '00-Error_Logs')
	directory_for_error_logs_truncated_for_display.set('Target Directory ' + os.sep + ' 00-Error_Logs')
	
	# Samba configuration needs to be updated also, since the path to HotFolder has changed.
	samba_configuration_file_content = ['# Samba Configuration File', \
	'', \
	'[global]', \
	'workgroup = WORKGROUP', \
	'server string = %h server (Samba, ' + hotfolder_name_to_use + ')', \
	'force create mode = 0777', \
	'unix extensions = no', \
	'log file = /var/log/samba/log.%m', \
	'max log size = 1000', \
	'syslog = 0', \
	'panic action = /usr/share/samba/panic-action %d', \
	'security = share', \
	'socket options = TCP_NODELAY', \
	'', \
	'[' + hotfolder_name_to_use + ']', \
	'comment = ' + hotfolder_name_to_use, \
	'read only = no', \
	'locking = no', \
	'path = ' + hotfolder_path.get(), \
	'guest ok = yes', \
	'browseable = yes']
	
	samba_configuration_file_content_as_a_string = '\n'.join(samba_configuration_file_content)
	
	samba_config_text_widget.delete('1.0', 'end')
	samba_config_text_widget.insert('1.0', samba_configuration_file_content_as_a_string)
	samba_config_text_widget.edit_modified(False)
	
	if debug == True:
		print()
		print('hotfolder_path =', hotfolder_path.get())
		print('directory_for_results =', directory_for_results.get())
		print('web_page_path =', web_page_path.get())
		print('directory_for_temporary_files =', directory_for_temporary_files.get())
		print('english =', english)
		print('finnish =', finnish)
		
def print_number_of_processors_cores_to_use(*args):
	if debug == True:
		print()
		print('number_of_processor_cores =', number_of_processor_cores.get())

def print_use_tls(*args):
	if debug == True:
		true_false_string = [False, True]
		print()
		print('use_tls =', true_false_string[use_tls.get()])
		
def print_smtp_server_requires_authentication(*args):
	if debug == True:
		true_false_string = [False, True]
		print()
		print('smtp_server_requires_authentication =', true_false_string[smtp_server_requires_authentication.get()])

def define_smtp_server_name(*args):
	smtp_server_name = smtp_server_name_combobox.get()
	if debug == True:
		print()
		print('smtp_server_name =', smtp_server_name)
		
def define_smtp_server_port(*args):
	smtp_server_port = smtp_server_port_combobox.get()
	if debug == True:
		print()
		print('smtp_server_port =', smtp_server_port)
		
def print_smtp_username(*args):
	if debug == True:
		print()
		print('smtp_username =', smtp_username.get())
		
def print_smtp_password(*args):
	if debug == True:
		print()
		print('smtp_password =', smtp_password.get())

def convert_email_sending_interval_to_seconds(*args):
	global email_sending_interval
	email_sending_interval = int(email_sending_interval_in_minutes.get()) * 60
	if debug == True:
		print()
		print('email_sending_interval =', email_sending_interval)

def print_heartbeat(*args):
	if debug == True:
		true_false_string = [False, True]
		print()
		print('heartbeat =', true_false_string[heartbeat.get()])

def send_test_email(*args):
	
	global message_text_string
	global email_sending_details
	global all_ip_addresses_of_the_machine
	
	message_text_string = ''
	put_email_details_in_a_dictionary()
	email_settings_are_complete, error_message = test_if_email_settings_are_complete()
	if email_settings_are_complete == False:
		email_sending_message_1.set('Email settings are incomplete:')
		email_sending_message_2.set(error_message)
		third_window_label_15['foreground'] = 'red'
		third_window_label_17['foreground'] = 'red'
		return
	if email_settings_are_complete == True:
		current_time = parse_time(time.time())
		message_text_string = '\nThis is a LoudnessCorrection test message sent ' + current_time + '.\n\nIP-Addresses of this machine are: ' + ' '.join(all_ip_addresses_of_the_machine) + '\n\n'
		email_sending_message_1.set('')
		email_sending_message_2.set('')
		third_window_label_15['foreground'] = 'black'
		third_window_label_17['foreground'] = 'black'
	
	connect_to_smtp_server()
	if email_sending_message_1.get() == 'Error sending email !!!!!!!':
		third_window_label_15['foreground'] = 'red'
		third_window_label_17['foreground'] = 'red'
	else:
		email_sending_message_1.set('Email sent successfully with the following content:')
		email_sending_message_2.set(message_text_string.strip('\n'))
		third_window_label_15['foreground'] = 'dark green'
		third_window_label_17['foreground'] = 'dark green'
	
	# The user may have misspelled some items and the error messages may have changed the dimensions of our frames and root window geometry is wrong.
	# We need to find out the new dinemsions of our frame and resize the root window if needed.
	# This also needs to be done when email sending is successful after an previous failed attempt.
	
	third_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(third_frame.winfo_reqwidth()+40) +'x'+ str(third_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
		
	if debug == True:
		print()
		print('email_sending_details =', email_sending_details)
		print('message_text_string =', message_text_string.strip('\n'))

def parse_time(time_int):
	
	# Parse time and expand one digit values to two (7 becomes 07).
	year = str(time.localtime(time_int).tm_year)
	month = str(time.localtime(time_int).tm_mon)
	day = str(time.localtime(time_int).tm_mday)
	hours = str(time.localtime(time_int).tm_hour)
	minutes = str(time.localtime(time_int).tm_min)
	seconds = str(time.localtime(time_int).tm_sec)
	# The length of each time string is either 1 or 2. Subtract the string length from number 2 and use the result to count how many zeroes needs to be before the time string.
	month = str('0' *( 2 - len(str(month))) + str(month))
	day = str('0' * (2 - len(str(day))) + str(day))
	hours = str('0' * (2 - len(str(hours))) + str(hours))
	minutes = str('0' *( 2 - len(str(minutes))) + str(minutes))
	seconds = str('0' * (2 - len(str(seconds))) + str(seconds))
	
	time_string= year + '.' + month + '.' + day + ' at ' + hours + ':' + minutes + ':' + seconds
	
	return(time_string)
	
def put_email_details_in_a_dictionary():
	
	true_false_string = [False, True]
	global email_sending_details
	global where_to_send_error_messages
	
	email_sending_details['send_error_messages_by_email'] = true_false_string[send_error_messages_by_email.get()]
	email_sending_details['use_tls'] = true_false_string[use_tls.get()]
	email_sending_details['smtp_server_requires_authentication'] = true_false_string[smtp_server_requires_authentication.get()]
	email_sending_details['smtp_server_name'] = smtp_server_name.get()
	email_sending_details['smtp_server_port'] = smtp_server_port.get()
	email_sending_details['smtp_username'] = smtp_username.get()
	email_sending_details['smtp_password'] = smtp_password.get()
	email_sending_details['message_recipients'] = message_recipients
	email_sending_details['email_sending_interval'] = email_sending_interval
	email_sending_details['message_title'] = 'LoudnessCorrection Error Message' # The title of the email message.
	
	if (true_false_string[send_error_messages_by_email.get()] == True) and ('email' not in where_to_send_error_messages):
		where_to_send_error_messages.append('email')
	
def test_if_email_settings_are_complete():
	error_message = ''
	email_settings_are_complete = True
	
	if email_sending_details['smtp_server_name'] == '':
		email_settings_are_complete = False
		error_message = 'ERROR !!!!!!! Smtp server name has not been defined.'
	if email_sending_details['smtp_server_port'] == '':
		email_settings_are_complete = False
		error_message = 'ERROR !!!!!!! Smtp server port has not been defined.'
	if email_sending_details['smtp_username'] == '':
		email_settings_are_complete = False
		error_message = 'ERROR !!!!!!! Smtp user name (email sender) has not been defined.'
	if (email_sending_details['smtp_server_requires_authentication'] == True) and (email_sending_details['smtp_password'] == ''):
		email_settings_are_complete = False
		error_message = 'ERROR !!!!!!! Password has not been defined.'
	if email_sending_details['message_recipients'] == []:
		email_settings_are_complete = False
		error_message = 'ERROR !!!!!!! Email recipients have not been defined. (Remember to press ENTER)'
	return(email_settings_are_complete, error_message)

def connect_to_smtp_server():
   
	global message_text_string
	global email_sending_details
	
	message_recipients = email_sending_details['message_recipients']
	message_title = 'LoudnessCorrection Test Message'
	message_attachment_path =''
	smtp_server_name = email_sending_details['smtp_server_name']
	smtp_server_port = email_sending_details['smtp_server_port']
	use_tls = email_sending_details['use_tls']
	smtp_server_requires_authentication = email_sending_details['smtp_server_requires_authentication']
	smtp_username = email_sending_details['smtp_username']
	smtp_password = email_sending_details['smtp_password']
	
	# Compile the start of the email message.
	email_message_content = email.mime.multipart.MIMEMultipart()
	email_message_content['From'] = smtp_username
	email_message_content['To'] = ', '.join(message_recipients)
	email_message_content['Subject'] = message_title
   
	# Append the user given lines of text to the email message.
	email_message_content.attach(email.mime.text.MIMEText(message_text_string.encode('utf-8'), _charset='utf-8'))
   
	# Read attachment file, encode it and append it to the email message.
	if message_attachment_path != '': # If no attachment path is defined, do nothing.
		email_attachment_content = email.mime.base.MIMEBase('application', 'octet-stream')
		email_attachment_content.set_payload(open(message_attachment_path, 'rb').read())
		email.encoders.encode_base64(email_attachment_content)
		email_attachment_content.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(message_attachment_path))
		email_message_content.attach(email_attachment_content)
   
	# Email message is ready, before sending it, it must be compiled  into a long string of characters.
	email_message_content_string = email_message_content.as_string()

	# Start communication with the smtp-server.
	try:
		mailServer = smtplib.SMTP(smtp_server_name, smtp_server_port, 'localhost', 15) # Timeout is set to 15 seconds.
		mailServer.ehlo()
		  
		# Check if message size is below the max limit the smpt server announced.
		message_size_is_within_limits = True # Set the default that is used if smtp-server does not annouce max message size.
		if 'size' in mailServer.esmtp_features:
			server_max_message_size = int(mailServer.esmtp_features['size']) # Get smtp server announced max message size
			message_size = len(email_message_content_string) # Get our message size
			if message_size > server_max_message_size: # Message is too large for the smtp server to accept, abort sending.
				message_size_is_within_limits = False
				email_sending_message_1.set('Error sending email !!!!!!!')
				email_sending_message_2.set('Message_size (', str(message_size), ') is larger than the max supported size (', str(server_max_message_size), ') of server:', smtp_server_name, 'Sending aborted.')
				return()
		if message_size_is_within_limits == True:
			# Uncomment the following line if you want to see printed out the final message that is sent to the smtp server
			# print('email_message_content_string =', email_message_content_string)
			if use_tls == True:
				mailServer.starttls()
				mailServer.ehlo() # After starting tls, ehlo must be done again.
			if smtp_server_requires_authentication == True:
				mailServer.login(smtp_username, smtp_password)
			mailServer.sendmail(smtp_username, message_recipients, email_message_content_string)
		mailServer.close()
		
	except smtplib.socket.timeout as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, Timeout error: ' + str(reason_for_error))
		return
	except smtplib.socket.error as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, Socket error: ' + str(reason_for_error))
		return
	except smtplib.SMTPRecipientsRefused as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, All recipients were refused: ' + str(reason_for_error))
		return
	except smtplib.SMTPHeloError as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, The server didn’t reply properly to the HELO greeting: ' + str(reason_for_error))
		return
	except smtplib.SMTPSenderRefused as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, The server didn’t accept the sender address: ' + str(reason_for_error))
		return
	except smtplib.SMTPDataError as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, The server replied with an unexpected error code or The SMTP server refused to accept the message data: ' + str(reason_for_error))
		return
	except smtplib.SMTPException as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, The server does not support the STARTTLS extension or No suitable authentication method was found: ' + str(reason_for_error))
		return
	except smtplib.SMTPAuthenticationError as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, The server didn’t accept the username/password combination: ' + str(reason_for_error))
		return
	except smtplib.SMTPConnectError as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, Error occurred during establishment of a connection with the server: ' + str(reason_for_error))
		return
	except RuntimeError as reason_for_error:
		email_sending_message_1.set('Error sending email !!!!!!!')
		email_sending_message_2.set('Error, SSL/TLS support is not available to your Python interpreter: ' + str(reason_for_error))
		return

	email_sending_message_1.set('')
	email_sending_message_2.set('')
	
def print_write_html_progress_report(*args):
	if debug == True:
		true_false_string = [False, True]
		print()
		print('write_html_progress_report =', true_false_string[write_html_progress_report.get()])

def print_create_a_ram_disk_for_html_report_and_toggle_next_button_state(*args):
	global list_of_ram_devices
	global list_of_normal_users_accounts
	
	if (len(list_of_ram_devices) == 0) and (create_a_ram_disk_for_html_report.get() == True):
		fourth_window_next_button['state'] = 'disabled'
	else:
		if len(list_of_normal_users_accounts) > 0:
			fourth_window_next_button['state'] = 'normal'
		
	if debug == True:
		true_false_string = [False, True]
		print()
		print('create_a_ram_disk_for_html_report =', true_false_string[create_a_ram_disk_for_html_report.get()])
		
def get_list_of_normal_user_accounts_from_os():
	
	# This subroutine gets the list of normal user accounts from the os.
	os_passwordfile_path = '/etc/passwd'
	one_line_of_textfile_as_list = []
	global list_of_normal_users_accounts
	error_happened = False
	error_message = ''

	try:
		with open(os_passwordfile_path, 'r') as passwordfile_handler:
			
			while True:
				one_line_of_textfile = passwordfile_handler.readline()
				if len(one_line_of_textfile) == 0: # Zero length indicates EOF
					break
				one_line_of_textfile_as_list = one_line_of_textfile.split(':')
				if (int(one_line_of_textfile_as_list[2]) >= 1000) and (one_line_of_textfile_as_list[0] != 'nobody'):
					list_of_normal_users_accounts.append(one_line_of_textfile_as_list[0])
					
	except IOError as reason_for_error:
		error_happened = True
		error_message = 'Error reading file /etc/passwd: ' + str(reason_for_error)
	except OSError as reason_for_error:
		error_happened = True
		error_message = 'Error reading /etc/passwd: ' + str(reason_for_error)
	except EOFError as reason_for_error:
		error_happened = True
		error_message = 'Error reading /etc/passwd: ' + str(reason_for_error)

	if len(list_of_normal_users_accounts) == 0:
		error_happened = True
		error_message = 'Unknown error, could not get the list of normal user accounts from the os'
		
	return(error_happened, error_message, list_of_normal_users_accounts)
	
def get_list_of_ram_devices_from_os():
	
	# This program gets the list of ram disks from the os and prints it.
	global list_of_ram_devices
	error_happened = False
	error_message = ''

	try:
		# Get directory listing for HotFolder. The 'break' statement stops the for - statement from recursing into subdirectories.
		for path, list_of_directories, list_of_files in os.walk('/dev/'):
			break
			
	except IOError as reason_for_error:
		error_happened = True
		list_of_ram_devices = ['Error !!!!!!!']
		error_message = 'Error getting list of os ram devices: ' + str(reason_for_error)
	except OSError as reason_for_error:
		error_happened = True
		list_of_ram_devices = ['Error !!!!!!!']
		error_message = 'Error getting list of os ram devices: ' + str(reason_for_error)

	if error_happened == False:
		for item in list_of_files:
			if ('ram' in item) and (int(item.strip('ram')) < 10) and (item != 'ram0'):
				list_of_ram_devices.append('/dev/' + item)

		list_of_ram_devices.sort()
	
	if len(list_of_ram_devices) == 0:
		error_happened = True
		error_message = 'Unknown error getting the list of ram devices from the os'
		
	return(error_happened, error_message, list_of_ram_devices)
	
def print_ram_device_name(*args):
	if debug == True:
		print()
		print('ram_device_name =', ram_device_name.get())
		
	return 'break'

def print_user_account(*args):
	if debug == True:
		print()
		print('user_account =', user_account.get())

def undo_text_in_text_widget(*args):
	# Test if there are any undo history left in the undo buffer.
	# If there is do an undo, otherwise prevent it,
	# Undoing beyond the last event would empty our text widget completely.
	if samba_config_text_widget.edit_modified() == 1:
		samba_config_text_widget.edit_undo()
		
	# The Ctrl+z is also bound to <Undo> event in the tkiner system level.
	# User bound Ctrl+z events are run first and after that the system level bind is run.
	# As I have defined Ctrl+z binding in my text widget, this routine is run first.
	# The following return 'break' prevents Tkinter from running any other Ctrl+z bindings.
	# Without this return 'break' line an Ctrl+z would undo text in the text widget until the widget would be completely empty.
	return 'break'

def set_samba_configuration(*args):
	global samba_configuration_file_content
	samba_configuration_file_content = samba_config_text_widget.get('1.0', 'end').split('\n')
		
	if debug == True:
		print()
		for item in samba_configuration_file_content:
			 print (item)

def print_root_password(*args):
	if debug == True:
		print()
		print('root_password =', root_password.get())

def print_use_samba_variable_and_toggle_text_widget(*args):
	
	true_false_string = [False, True]
	
	if use_samba.get() == True:
		samba_config_text_widget['state'] = 'normal'
		samba_config_text_widget['background'] = 'white'
		samba_config_text_widget['foreground'] = 'black'
		first_window_undo_button['state'] = 'normal'
	else:
		samba_config_text_widget['state'] = 'disabled'
		samba_config_text_widget['background'] = 'light gray'
		samba_config_text_widget['foreground'] = 'gray'
		first_window_undo_button['state'] = 'disabled'
	samba_config_text_widget.update()
	if debug == True:
		print()
		print('use_samba =', true_false_string[use_samba.get()])
		
def install_init_scripts_and_config_files(*args):
	
	# Create init scripts and gather all varible values that the LoudnessCorrection scripts need and save config data to file '/etc/Loudness_Correction_Settings.pickle'.
	# Copy LoudessCorrection.py and HeartBeat_Checker.py to /usr/bin
	# Write possible samba configuration file to /etc/samba/smb.conf
	# Write an init script that:
	#----------------------------
	# Creates an ram disk if user requested it.
	# Creates the needed directory structure in the HotFolder
	# Changes directory permissions so that users that use the server through network can not delete important files and directories
	# Starts up LoudnessCorrection.py and possibly HeartBeat_Checker.py
	
	global loudness_correction_init_script_content
	global ram_disk_mount_commands
	global python3_path
	global samba_configuration_file_content
	global configfile_path
	
	#############################################################################################
	# Create the init script that is going to start LoudnessCorrection when the computer starts #
	#############################################################################################
	
	# Gather init script commands in a list.
	loudness_correction_init_script_content_part_1 = ['#!/bin/sh', \
	'', \
	'USERNAME="' + user_account.get() + '"', \
	'TARGET_PATH="' + target_path.get() + '"', \
	'HOTFOLDER_NAME="' + os.path.basename(hotfolder_path.get()) + '"', \
	'WEB_PAGE_PATH="' + os.path.basename(web_page_path.get()) + '"', \
	'DIRECTORY_FOR_RESULTS="' + directory_for_results.get() + '"', \
	'PYTHON3_PATH="' + python3_path + '"', \
	'LOUDNESSCORRECTION_SCRIPT_PATH="/usr/bin/LoudnessCorrection.py"', \
	'HEARTBEAT_PATH="/usr/bin/HeartBeat_Checker.py"', \
	'RAM_DEVICE_NAME="'+ ram_device_name.get() + '"', \
	'CONFIGFILE_PATH="' + configfile_path + '"', \
	'', \
	'#############################################################################################', \
	'# Send output to logfile.', \
	'#############################################################################################', \
	'', \
	'exec >> /var/log/LoudnessCorrection.log 2>&1', \
	"# set -x   # Uncomment this if you wan't every command in this script written to the logfile.", \
	'', \
	'case "$1" in', \
	'', \
	'	start)', \
	'', \
	'		#############################################################################################', \
	'		# Wait for the os startup process to finish, so that all services are available', \
	'		#############################################################################################', \
	'', \
	'		sleep 90', \
	'', \
	'		#############################################################################################', \
	'		# Create directories needed by the LoudnessCorrection.py - script.', \
	'		#############################################################################################', \
	'', \
	'		mkdir -p "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH/"', \
	'		mkdir -p "$DIRECTORY_FOR_RESULTS"', \
	'		mkdir -p "$TARGET_PATH/00-Error_Logs"', \
	'		mkdir -p "$TARGET_PATH/00-Loudness_Calculation_Temporary_Files"', \
	'']
	
	ram_disk_mount_commands = ['		#############################################################################################', \
	'		# Create a Ram-Disk and mount it. LoudnessCorrecion.py writes the html-page on the ram disk,', \
	'		# because it speeds up html updating when the machine is under heavy load.', \
	'		#############################################################################################', \
	'', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'		chmod -R 1755 "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'', \
	'		mke2fs -q -m 0 $RAM_DEVICE_NAME 1024', \
	'		mount $RAM_DEVICE_NAME "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'']
	
	loudness_correction_init_script_content_part_2_with_heartbeat = [
	'		#############################################################################################', \
	'		# Change directory ownerships and permissions so that network users can not delete important', \
	'		# files and directories.', \
	'		#############################################################################################', \
	'', \
	'		mkdir -p "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH/.temporary_files"', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'		chmod -R 1755 "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'', \
	'		chown $USERNAME:$USERNAME "$TARGET_PATH"', \
	'		chmod 1777 "$TARGET_PATH"', \
	'', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/00-Error_Logs"', \
	'		chmod 1744 "$TARGET_PATH/00-Error_Logs"', \
	'', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/00-Loudness_Calculation_Temporary_Files"', \
	'		chmod 1744 "$TARGET_PATH/00-Loudness_Calculation_Temporary_Files"', \
	'', \
	'		chown $USERNAME:$USERNAME "$TARGET_PATH/$HOTFOLDER_NAME"', \
	'		chmod 1777 "$TARGET_PATH/$HOTFOLDER_NAME"', \
	'', \
	'		chown $USERNAME:$USERNAME "$DIRECTORY_FOR_RESULTS"', \
	'		chmod 1777 "$DIRECTORY_FOR_RESULTS"', \
	'', \
	'		#############################################################################################', \
	'		# Run LoudnessCorrection and HeartBeat - scripts as a normal user without root privileges.', \
	'		# Wait for the LoudnessCorrection process to get going before starting HeartBeat monitoring.', \
	'		#############################################################################################', \
	'', \
	'		su $USERNAME -c "$PYTHON3_PATH $LOUDNESSCORRECTION_SCRIPT_PATH -configfile $CONFIGFILE_PATH &"', \
	'', \
	'		echo `date`": LoudnessCorrection Started, Pid: "`pgrep -f "$PYTHON3_PATH $LOUDNESSCORRECTION_SCRIPT_PATH -configfile $CONFIGFILE_PATH"`', \
	'', \
	'		sleep 60', \
	'', \
	'		su $USERNAME -c "$PYTHON3_PATH $HEARTBEAT_PATH -configfile $CONFIGFILE_PATH &"', \
	'', \
	'		echo `date`": HeartBeat_Checker Started, Pid: "`pgrep -f "$PYTHON3_PATH $HEARTBEAT_PATH -configfile $CONFIGFILE_PATH"`', \
	'', \
	'	;;', \
	'', \
	'	stop)', \
	'', \
	'		echo `date`": Shutting down LoudnessCorrection and HeartBeat_Checker"', \
	'		kill -HUP `pgrep -f "$PYTHON3_PATH $LOUDNESSCORRECTION_SCRIPT_PATH -configfile $CONFIGFILE_PATH"`', \
	'		kill -HUP `pgrep -f "$PYTHON3_PATH $HEARTBEAT_PATH -configfile $CONFIGFILE_PATH"`', \
	'', \
	'	;;', \
	'', \
	'', \
	'	*)', \
	'		echo "Usage: $0 {start|stop|restart|status}"', \
	'		exit 1', \
	'	esac']

	loudness_correction_init_script_content_part_2_without_heartbeat = ['		#############################################################################################', \
	'		# Change directory ownerships and permissions so that network users can not delete important', \
	'		# files and directories.', \
	'		#############################################################################################', \
	'', \
	'		mkdir -p "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH/.temporary_files"', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'		chmod -R 1755 "$TARGET_PATH/$HOTFOLDER_NAME/$WEB_PAGE_PATH"', \
	'', \
	'		chown $USERNAME:$USERNAME "$TARGET_PATH"', \
	'		chmod 1777 "$TARGET_PATH"', \
	'', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/00-Error_Logs"', \
	'		chmod 1744 "$TARGET_PATH/00-Error_Logs"', \
	'', \
	'		chown -R $USERNAME:$USERNAME "$TARGET_PATH/00-Loudness_Calculation_Temporary_Files"', \
	'		chmod 1744 "$TARGET_PATH/00-Loudness_Calculation_Temporary_Files"', \
	'', \
	'		chown $USERNAME:$USERNAME "$TARGET_PATH/$HOTFOLDER_NAME"', \
	'		chmod 1777 "$TARGET_PATH/$HOTFOLDER_NAME"', \
	'', \
	'		chown $USERNAME:$USERNAME "$DIRECTORY_FOR_RESULTS"', \
	'		chmod 1777 "$DIRECTORY_FOR_RESULTS"', \
	'', \
	'		#############################################################################################', \
	'		# Run LoudnessCorrection and HeartBeat - scripts as a normal user without root privileges.', \
	'		# Wait for the LoudnessCorrection process to get going before starting HeartBeat monitoring.', \
	'		#############################################################################################', \
	'', \
	'		su $USERNAME -c "$PYTHON3_PATH $LOUDNESSCORRECTION_SCRIPT_PATH -configfile $CONFIGFILE_PATH &"', \
	'', \
	'		echo `date`": LoudnessCorrection Started, Pid: "`pgrep -f "$PYTHON3_PATH $LOUDNESSCORRECTION_SCRIPT_PATH -configfile $CONFIGFILE_PATH"`', \
	'', \
	'	;;', \
	'', \
	'	stop)', \
	'', \
	'		echo `date`": Shutting down LoudnessCorrection and HeartBeat_Checker"', \
	'		kill -HUP `pgrep -f "$PYTHON3_PATH $LOUDNESSCORRECTION_SCRIPT_PATH -configfile $CONFIGFILE_PATH"`', \
	'', \
	'	;;', \
	'', \
	'', \
	'	*)', \
	'		echo "Usage: $0 {start|stop|restart|status}"', \
	'		exit 1', \
	'	esac']

	# Compile init script to one list from separate lists.
	# Add first part of the init script commands.
	loudness_correction_init_script_content = loudness_correction_init_script_content_part_1
	# If the user wants us to create a ram - disk, then add code in the init script to do it.
	if create_a_ram_disk_for_html_report.get() == True:
		loudness_correction_init_script_content.extend(ram_disk_mount_commands)
	# Add last part of the init script commands with or without HeartBeat_Checker commands depending whether user requested HeartBeat Checker or not.
	if heartbeat.get() == True:
		loudness_correction_init_script_content.extend(loudness_correction_init_script_content_part_2_with_heartbeat)
	else:
		loudness_correction_init_script_content.extend(loudness_correction_init_script_content_part_2_without_heartbeat)

	if debug == True:
		for line in loudness_correction_init_script_content:
			print(line)
	
	########################################################################################################################################
	# Put all variables that LoudnessCorrecion - sripts need to run into a dictionary, that is going to be saved on disk as the configfile #
	########################################################################################################################################

	true_false_string = [False, True]
	global english
	global finnish
	global delay_between_directory_reads
	global file_expiry_time
	global natively_supported_file_formats
	global loudness_path
	global ffmpeg_output_format
	global silent
	global html_progress_report_write_interval
	global send_error_messages_to_logfile
	global heartbeat_file_name
	global heartbeat_write_interval
	global email_sending_details
	global version
	global sox_path
	global ffmpeg_path
	global gnuplot_path
	global all_ip_addresses_of_the_machine
	global peak_measurement_method
	
	put_email_details_in_a_dictionary()

	all_settings_dict = { 'language' : language.get(), 'english' : english, 'finnish' : finnish, 'target_path' : target_path.get(), 'hotfolder_path' : hotfolder_path.get(), \
	'directory_for_temporary_files' : directory_for_temporary_files.get(), 'directory_for_results' : directory_for_results.get(), 'delay_between_directory_reads' : int(delay_between_directory_reads), \
	'number_of_processor_cores' : int(number_of_processor_cores.get()), 'file_expiry_time' : int(file_expiry_time), 'natively_supported_file_formats' : natively_supported_file_formats, \
	'libebur128_path' : loudness_path, 'ffmpeg_output_format' : ffmpeg_output_format, 'silent' : silent, 'write_html_progress_report' : true_false_string[write_html_progress_report.get()], \
	'html_progress_report_write_interval' : int(html_progress_report_write_interval), 'web_page_name' : web_page_name.get(), 'web_page_path' : web_page_path.get(), \
	'directory_for_error_logs' : directory_for_error_logs.get(), 'send_error_messages_to_logfile' : send_error_messages_to_logfile, 'heartbeat' : true_false_string[heartbeat.get()], \
	'heartbeat_file_name' : heartbeat_file_name, 'heartbeat_write_interval' : int(heartbeat_write_interval), 'email_sending_details' : email_sending_details, \
	'send_error_messages_by_email' : true_false_string[send_error_messages_by_email.get()], 'where_to_send_error_messages' : where_to_send_error_messages, \
	'config_file_created_by_installer_version' : version, 'peak_measurement_method' : peak_measurement_method }

	# Get the total number of items in settings dictionary and save the number in the dictionary. The number can be used for degugging settings.
	number_of_all_items_in_dictionary = len(all_settings_dict)
	all_settings_dict['number_of_all_items_in_dictionary'] = number_of_all_items_in_dictionary

	if debug == True:
		# Print variables.
		title_text = '\nConfiguration variables written to ' + configfile_path + ' are:'
		
		print()
		print(title_text)
		print((len(title_text) + 1) * '-' + '\n') # Print a line exactly the length of the title text line + 1.
		print('language =', all_settings_dict['language'])
		print('english =', all_settings_dict['english'])
		print('finnish =', all_settings_dict['finnish'])
		print()	
		print('target_path =', all_settings_dict['target_path'])
		print('hotfolder_path =', all_settings_dict['hotfolder_path'])
		print('directory_for_temporary_files =', all_settings_dict['directory_for_temporary_files'])
		print('directory_for_results =', all_settings_dict['directory_for_results'])
		print('libebur128_path =', all_settings_dict['libebur128_path'])
		print()
		print('delay_between_directory_reads =', all_settings_dict['delay_between_directory_reads'])	
		print('number_of_processor_cores =', all_settings_dict['number_of_processor_cores'])
		print('file_expiry_time =', all_settings_dict['file_expiry_time'])
		print()
		print('natively_supported_file_formats =', all_settings_dict['natively_supported_file_formats'])
		print('ffmpeg_output_format =', all_settings_dict['ffmpeg_output_format'])
		print('peak_measurement_method =', all_settings_dict['peak_measurement_method'])
		print()	
		print('silent =', all_settings_dict['silent'])
		print()	
		print('write_html_progress_report =', all_settings_dict['write_html_progress_report'])
		print('html_progress_report_write_interval =', all_settings_dict['html_progress_report_write_interval'])
		print('web_page_name =', all_settings_dict['web_page_name'])
		print('web_page_path =', all_settings_dict['web_page_path'])
		print()
		print('heartbeat =', all_settings_dict['heartbeat'])
		print('heartbeat_file_name =', all_settings_dict['heartbeat_file_name'])
		print('heartbeat_write_interval =', all_settings_dict['heartbeat_write_interval'])
		print()
		print('where_to_send_error_messages =', all_settings_dict['where_to_send_error_messages'])
		print('send_error_messages_to_logfile =', all_settings_dict['send_error_messages_to_logfile'])
		print('directory_for_error_logs =', all_settings_dict['directory_for_error_logs'])
		print()
		print('send_error_messages_by_email =', all_settings_dict['send_error_messages_by_email'])
		print('email_sending_details =', all_settings_dict['email_sending_details'])
		print()
		print('number_of_all_items_in_dictionary =', all_settings_dict['number_of_all_items_in_dictionary'])
		print()
		print('config_file_created_by_installer_version =', all_settings_dict['config_file_created_by_installer_version'])
		print()

	##############################################################################
	# Copy scripts and write init scripts and config files to system directories #
	##############################################################################

	global path_to_loudnesscorrection
	global path_to_heartbeat_checker

	password = root_password.get()  + '\n' # Add a carriage return after the root password
	password = password.encode('utf-8') # Convert password from string to binary format.
	# Sudo switches are:
	# -k = Forget authentication immediately after command.
	# -p = Use a custom string to prompt the user for the password (we use an empty string here).
	# -S = Read password from stdin.
	
	#######################################
	# Copy BackupParanoia.py to /usr/bin/ #
	#######################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'cp', '-f', path_to_loudnesscorrection, '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.

	########################################
	# Change BackupParanoia.py permissions #
	########################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	##################################
	# Change BackupParanoia.py owner #
	##################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.	

	##########################################
	# Copy HeartBeat_Checker.py to /usr/bin/ #
	##########################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'cp', path_to_heartbeat_checker, '/usr/bin/' + os.path.basename(path_to_heartbeat_checker)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.

	###########################################
	# Change HeartBeat_Checker.py permissions #
	###########################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', '/usr/bin/' + os.path.basename(path_to_heartbeat_checker)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.

	#####################################
	# Change HeartBeat_Checker.py owner #
	#####################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', '/usr/bin/' + os.path.basename(path_to_heartbeat_checker)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.	

	###############################################################################################################################
	# Write all configuration variables in the config dictionary to the config file in '/tmp/Loudness_Correction_Settings.pickle' #
	###############################################################################################################################

	global directory_for_os_temporary_files
	path_for_configfile_in_temp_directory = directory_for_os_temporary_files + os.sep + os.path.basename(configfile_path)

	try:
		with open(path_for_configfile_in_temp_directory, 'wb') as configfile_handler:
			pickle.dump(all_settings_dict, configfile_handler)
			configfile_handler.flush() # Flushes written data to os cache
			os.fsync(configfile_handler.fileno()) # Flushes os cache to disk
	except IOError as reason_for_error:
		error_in_string_format = 'Error opening configfile for writing ' + str(reason_for_error)
		show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format)
		return(True) # There was an error, exit this subprogram.
	except OSError as reason_for_error:
		error_in_string_format = 'Error opening configfile for writing ' + str(reason_for_error)
		show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format)
		return(True) # There was an error, exit this subprogram.

	#########################################################################################################################
	# Move configfile from '/tmp/Loudness_Correction_Settings.pickle' to '/etc/Loudness_Correction_Settings.pickle' as root #
	#########################################################################################################################

	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'mv', '-f', path_for_configfile_in_temp_directory, configfile_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	#################################
	# Change configfile permissions #
	#################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '644', configfile_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	###########################
	# Change configfile owner #
	###########################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', configfile_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.

	########################################################################
	# Check if user wants to share the HotFolder to the network with samba #
	########################################################################

	if use_samba.get() == True:

		#################################################################
		# Check if directory '/etc/samba' exists, if not then create it #
		#################################################################
		
		if not os.path.exists('/etc/samba'):
			commands_to_run = ['sudo', '-k', '-p', '', '-S', 'mkdir', '-p', '/etc/samba'] # Create the commandline we need to run as root.

			# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
			sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
			sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
			
			# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
			if len(sudo_stderr_string) != 0:
				show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
				return(True) # There was an error, exit this subprogram.
			
			# Password was accepted and our command was successfully run as root.
			root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.

			###################################
			# Change '/etc/samba' permissions #
			###################################
			
			commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', '/etc/samba'] # Create the commandline we need to run as root.

			# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
			sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
			sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
			
			# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
			if len(sudo_stderr_string) != 0:
				show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
				return(True) # There was an error, exit this subprogram.
			
			# Password was accepted and our command was successfully run as root.
			root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
			
			#######################################
			# Change configfile'/etc/samba' owner #
			#######################################
			
			commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', '/etc/samba'] # Create the commandline we need to run as root.

			# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
			sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
			sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
			
			# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
			if len(sudo_stderr_string) != 0:
				show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
				return(True) # There was an error, exit this subprogram.
			
			# Password was accepted and our command was successfully run as root.
			root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
			
		##################################################################################################################################################################
		# Check if there already is an old version of smb.conf, if found read then last modification time of file and rename it adding the modification time to the name #
		##################################################################################################################################################################
		
		if os.path.exists('/etc/samba/smb.conf'):
			old_samba_configfile_timestamp = int(os.lstat('/etc/samba/smb.conf').st_mtime)
			old_samba_configfile_timestamp_string = parse_time(old_samba_configfile_timestamp)
			old_samba_configfile_timestamp_string = old_samba_configfile_timestamp_string.replace(' at ', '__')
		
			commands_to_run = ['sudo', '-k', '-p', '', '-S', 'mv', '-f', '/etc/samba/smb.conf', '/etc/samba/smb.conf' + '_' + old_samba_configfile_timestamp_string] # Create the commandline we need to run as root.

			# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
			sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
			sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
			
			# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
			if len(sudo_stderr_string) != 0:
				show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
				return(True) # There was an error, exit this subprogram.
			
			# Password was accepted and our command was successfully run as root.
			root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
		
		##############################################
		# Write samba configuration to /tmp/smb.conf #
		##############################################
		
		try:
			with open(directory_for_os_temporary_files + os.sep + 'smb.conf', 'wt') as samba_configfile_handler:
				samba_configfile_handler.write('\n'.join(samba_configuration_file_content))
				samba_configfile_handler.flush() # Flushes written data to os cache
				os.fsync(samba_configfile_handler.fileno()) # Flushes os cache to disk
		except IOError as reason_for_error:
			error_in_string_format = 'Error opening Samba configfile for writing ' + str(reason_for_error)
			show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format)
			return(True) # There was an error, exit this subprogram.
		except OSError as reason_for_error:
			error_in_string_format = 'Error opening Samba configfile for writing ' + str(reason_for_error)
			show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format)
			return(True) # There was an error, exit this subprogram.
		
		###############################################################################
		# Move Samba configfile from '/tmp/smb.conf' to '/etc/samba/smb.conf' as root #
		###############################################################################
		
		commands_to_run = ['sudo', '-k', '-p', '', '-S', 'mv', '-f', directory_for_os_temporary_files + os.sep + 'smb.conf', '/etc/samba/smb.conf'] # Create the commandline we need to run as root.

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		
		# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
		if len(sudo_stderr_string) != 0:
			show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
			return(True) # There was an error, exit this subprogram.
		
		# Password was accepted and our command was successfully run as root.
		root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
		
		#######################################
		# Change Samba configfile permissions #
		#######################################
		
		commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '644', '/etc/samba/smb.conf'] # Create the commandline we need to run as root.

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		
		# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
		if len(sudo_stderr_string) != 0:
			show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
			return(True) # There was an error, exit this subprogram.
		
		# Password was accepted and our command was successfully run as root.
		root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
		
		#################################
		# Change Samba configfile owner #
		#################################
		
		commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', '/etc/samba/smb.conf'] # Create the commandline we need to run as root.

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		
		# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
		if len(sudo_stderr_string) != 0:
			show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
			return(True) # There was an error, exit this subprogram.
		
		# Password was accepted and our command was successfully run as root.
		root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
		
	##############################################################
	# Write init script to '/tmp/LoudnessCorrection-init_script' #
	##############################################################
	
	global loudnesscorrection_init_script_name
	global loudnesscorrection_init_script_path
	global loudnesscorrection_init_script_link_path
	
	try:
		with open(directory_for_os_temporary_files + os.sep + loudnesscorrection_init_script_name, 'wt') as init_script_file_handler:
			init_script_file_handler.write('\n'.join(loudness_correction_init_script_content))
			init_script_file_handler.flush() # Flushes written data to os cache
			os.fsync(init_script_file_handler.fileno()) # Flushes os cache to disk
	except IOError as reason_for_error:
		error_in_string_format = 'Error opening init script file for writing ' + str(reason_for_error)
		show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format)
		return(True) # There was an error, exit this subprogram.
	except OSError as reason_for_error:
		error_in_string_format = 'Error opening init script file for writing ' + str(reason_for_error)
		show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format)
		return(True) # There was an error, exit this subprogram.
	
	#######################################################################################################################
	# Move init script from '/tmp/loudnesscorrection_init_script' to '/etc/init.d/loudnesscorrection_init_script' as root #
	#######################################################################################################################

	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'mv', '-f', directory_for_os_temporary_files + os.sep + loudnesscorrection_init_script_name, loudnesscorrection_init_script_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	##################################
	# Change init script permissions #
	##################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', loudnesscorrection_init_script_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	############################
	# Change init script owner #
	############################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', loudnesscorrection_init_script_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	######################################################################################################################
	# Create a link for init script in /etc/rc2.d that starts up all LoudnessCorrection scripts when the computer starts #
	# The link will be named /etc/rc2.d/S99loudnesscorrection_init_script                                                #
	######################################################################################################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'ln', '-s', '-f', loudnesscorrection_init_script_path, loudnesscorrection_init_script_link_path] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
		return(True) # There was an error, exit this subprogram.
	
	# Password was accepted and our command was successfully run as root.
	root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.
	
	# Our scripts were installed successfully, update the label the to tell it to the user.
	loudnesscorrection_scripts_are_installed.set('Installed')
	
	# Disable Back - button since navigating back to the previous window and back here would delete /usr/bin/LoudnessCorrection.py. The previous window copies this file to test our root - password and then deletes it.
	seventh_window_back_button['state'] = 'disabled'
	
	return(False) # False means 'No errors happened everything was installed successfully :)'.
	
def test_if_root_password_is_valid(*args):
	
	#######################################################################################################################################
	# Test if root password is valid by copying LoudnessCorrection.py to /usr/bin and changing its permissions and owner.                 #
	# This copy is deleted from /usr/bin after the test because the file will be later be copied again with all other scripts and files.  #
	#######################################################################################################################################

	global path_to_loudnesscorrection
	root_password_was_accepted = True

	password = root_password.get()  + '\n' # Add a carriage return after the root password
	password = password.encode('utf-8') # Convert password from string to binary format.
	# Sudo switches are:
	# -k = Forget authentication immediately after command.
	# -p = Use a custom string to prompt the user for the password (we use an empty string here).
	# -S = Read password from stdin.
	
	#######################################
	# Copy BackupParanoia.py to /usr/bin/ #
	#######################################
	
	commands_to_run = ['sudo', '-k', '-p', '', '-S', 'cp', '-f', path_to_loudnesscorrection, '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

	# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
	sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
	sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
	if len(sudo_stderr_string) != 0:
		root_password_was_accepted = False
		show_error_message_on_root_password_window(sudo_stderr, sudo_stderr_string)

	########################################
	# Change BackupParanoia.py permissions #
	########################################
	
	if root_password_was_accepted == True:
	
		commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		
		# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
		if len(sudo_stderr_string) != 0:
			root_password_was_accepted = False
			show_error_message_on_root_password_window(sudo_stderr, sudo_stderr_string)
		
	##################################
	# Change BackupParanoia.py owner #
	##################################
	
	if root_password_was_accepted == True:
	
		commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		
		# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
		if len(sudo_stderr_string) != 0:
			root_password_was_accepted = False
			show_error_message_on_root_password_window(sudo_stderr, sudo_stderr_string)

	##########################################
	# Delete BackupParanoia.py from /usr/bin #
	##########################################
	
	if root_password_was_accepted == True:
	
		commands_to_run = ['sudo', '-k', '-p', '', '-S', 'rm', '-f', '/usr/bin/' + os.path.basename(path_to_loudnesscorrection)] # Create the commandline we need to run as root.

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		
		# If sudo stderr ouput is nonempty, then an error happened, check for the cause for the error.
		if len(sudo_stderr_string) != 0:
			root_password_was_accepted = False
			show_error_message_on_root_password_window(sudo_stderr, sudo_stderr_string)

	# If root password was valid then call the next window.
	if root_password_was_accepted == True:
		# Password was accepted and our command was successfully run as root.
		root_password_was_not_accepted_message.set('') # Remove possible error message from the screen.	
		call_seventh_frame_on_top() # Call the next window.

def show_error_message_on_root_password_window(error_in_binary_format, error_in_string_format):
	
	# If sudo stderror output includes string 'try again', then password was not valid.
	# Display an error message to the user. If user inputs wrong passwords many times in a row, change error messages between two messages.
	if 'try again' in error_in_string_format:
		if root_password_was_not_accepted_message.get() == 'Wrong password !!!!!!!':
			root_password_was_not_accepted_message.set('Wrong password again !!!!!!!')
		else:
			root_password_was_not_accepted_message.set('Wrong password !!!!!!!')
	else:
		# We don't know what the reason for error was, print the sudo error message on the window for the user.
		root_password_was_not_accepted_message.set('Error !!!!!!!\n\n' + error_in_string_format)
		
	# The error message may bee too long to display on the current window, resize the window again.
	sixth_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(sixth_frame.winfo_reqwidth()+40) +'x'+ str(sixth_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
	if debug == True:
		print()
		print('error_in_binary_format =', error_in_binary_format)
	
	# Make the window 'shake head' like Apples OS X input windows do, when the input is not accepted :)
	counter = 1
	while counter < 5:
		root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position + 20)) + '+' + str(int(y_position)))
		time.sleep(0.1)
		root_window.update()
		root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
		time.sleep(0.1)
		root_window.update()
		
		counter = counter + 1

def find_program_in_os_path(program_name_to_find):
	# Find a program in the operating system path. Returns the full path to the program (search for python3 returns: '/usr/bin/python3').
	program_path = ''
	os_environment_list = os.environ["PATH"].split(os.pathsep)
	for os_path in os_environment_list:
		true_or_false = os.path.exists(os_path + os.sep + program_name_to_find) and os.access(os_path + os.sep + program_name_to_find, os.X_OK) # True if program can be found in the path and it has executable permissions on.
		if true_or_false == True:
			program_path = os_path + os.sep + program_name_to_find
	return(program_path)

def find_program_in_current_dir(program_name_to_find):
	# Find a program in the current path. Returns the full path to the program (search for LoudnessCorrection.py returns: '/directory/LoudnessCorrection.py').
	program_path = ''
	current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
	true_or_false = os.path.exists(current_directory + os.sep + program_name_to_find) # True if program can be found in the path.
	if true_or_false == True:
			program_path = current_directory + os.sep + program_name_to_find
	return(program_path)

def set_seventh_window_label_texts_and_colors():

	# Set seventh window text labels and colors Seventh window tells the user if all needed programs are installed or not.
	
	global samba_path
	
	# Find paths to all critical programs we need to run LoudnessCorrection
	find_paths_to_all_external_programs_we_need()
	
	seventh_window_label_3['foreground'] = 'dark green'
	seventh_window_label_5['foreground'] = 'dark green'
	seventh_window_label_7['foreground'] = 'dark green'
	seventh_window_label_8['foreground'] = 'black'
	seventh_window_label_9['foreground'] = 'dark green'
	seventh_window_label_11['foreground'] = 'dark green'

	if ffmpeg_is_installed.get() == 'Not Installed':
		seventh_window_label_3['foreground'] = 'red'
	if sox_is_installed.get() == 'Not Installed':
		seventh_window_label_5['foreground'] = 'red'
	if gnuplot_is_installed.get() == 'Not Installed':
		seventh_window_label_7['foreground'] = 'red'		
	if use_samba.get() == False:
		samba_is_installed.set('Not Needed')
		seventh_window_label_8['foreground'] = 'dark gray'
		seventh_window_label_9['foreground'] = 'dark gray'
	if samba_is_installed.get() == 'Not Installed':
		seventh_window_label_9['foreground'] = 'red'
	if libebur128_is_installed.get() == 'Not Installed':
		seventh_window_label_11['foreground'] = 'red'

def find_paths_to_all_external_programs_we_need():

	# Find paths for all needed programs and define some tkinter variables, that are used on labels to indicate if some needed programs are installed or not.

	global python3_path
	global ffmpeg_path
	global sox_path
	global gnuplot_path
	global samba_path
	global loudness_path
	global all_needed_external_programs_are_installed

	all_needed_external_programs_are_installed = True
	python3_path = find_program_in_os_path('python3')
	
	ffmpeg_path = find_program_in_os_path('ffmpeg')
	if ffmpeg_path == '':
		ffmpeg_is_installed.set('Not Installed')
		all_needed_external_programs_are_installed = False
	else:
		ffmpeg_is_installed.set('Installed')

	sox_path = find_program_in_os_path('sox')
	if sox_path == '':
		sox_is_installed.set('Not Installed')
		all_needed_external_programs_are_installed = False
	else:
		sox_is_installed.set('Installed')

	gnuplot_path = find_program_in_os_path('gnuplot')
	if gnuplot_path == '':
		gnuplot_is_installed.set('Not Installed')
		all_needed_external_programs_are_installed = False
	else:
		gnuplot_is_installed.set('Installed')

	samba_path = find_program_in_os_path('smbd')
	if samba_path == '':
		samba_is_installed.set('Not Installed')
		# Check if user wants us to use samba, if not we don't care if it's installed or not.
		if use_samba.get() == True:
			all_needed_external_programs_are_installed = False
	else:
		samba_is_installed.set('Installed')

	loudness_path = find_program_in_os_path('loudness')
	if loudness_path == '':
		libebur128_is_installed.set('Not Installed')
		all_needed_external_programs_are_installed = False
	else:
		libebur128_is_installed.set('Installed')

def set_button_and_label_states_on_window_seven():
	
	# Set the label and button enable / disable state on window seven.
	
	global all_needed_external_programs_are_installed
	global external_program_installation_has_been_already_run
	
	if all_needed_external_programs_are_installed == False:
		# Some needed external programs are not installed.
		# Button and text label for: install all missings programs
		seventh_window_label_14['foreground'] = 'black'
		seventh_window_install_button['state'] = 'normal'
		# Button and text label for: Show me the installation shell commands
		seventh_window_label_15['foreground'] = 'black'
		seventh_window_show_button_1['state'] = 'normal'
		# The 'Next' button for the window
		seventh_window_next_button['state'] = 'disabled'
	else:
		# All needed external programs are installed.
		# Button and text label for: install all missings programs
		seventh_window_label_14['foreground'] = 'dark gray'
		seventh_window_install_button['state'] = 'disabled'
		# Button and text label for: Show me the installation shell commands
		seventh_window_label_15['foreground'] = 'dark gray'
		seventh_window_show_button_1['state'] = 'disabled'
		# The 'Next' button for the window
		seventh_window_next_button['state'] = 'normal'

	if loudnesscorrection_scripts_are_installed.get() == 'Not Installed':
		seventh_window_label_14['foreground'] = 'black'
		seventh_window_install_button['state'] = 'normal'
		seventh_window_next_button['state'] = 'disabled'

	if external_program_installation_has_been_already_run == False:
		# Our program installation rutine has not been run yet.
		# Button and text label for: Show me the messages output during the installation
		seventh_window_label_18['foreground'] = 'dark gray'
		seventh_window_show_button_2['state'] = 'disabled'
	else:
		# Our program installation rutine has been run.
		# Button and text label for: Show me the messages output during the installation
		seventh_window_label_18['foreground'] = 'black'
		seventh_window_show_button_2['state'] = 'normal'

def show_installation_shell_commands(*args):
	
	# Gather all package install and configure and buils commands to a string that is displayed to the user.
	
	global eight_window_textwidget_text_content
	eight_window_textwidget_text_content = ''
	
	global all_needed_external_programs_are_installed
	global apt_get_commands
	global needed_packages_install_commands

	global apt_get_commands
	global libebur128_dependencies_install_commands

	global loudness_path
	global git_commands
	global git_commands
	global cmake_commands
	global make_build_and_install_commands
	
	if needed_packages_install_commands != []:
		eight_window_textwidget_text_content = '# Install missing programs.\n' + ' '.join(apt_get_commands) + ' ' + ' '.join(needed_packages_install_commands) + '\n\n'
		
	if libebur128_dependencies_install_commands != []:
		eight_window_textwidget_text_content = eight_window_textwidget_text_content + '# Install compilation tools and developer packages needed to build libebur128.\n' + ' '.join(apt_get_commands) + ' ' + ' '.join(libebur128_dependencies_install_commands) + '\n\n'
		
	if loudness_path == '':
		eight_window_textwidget_text_content = eight_window_textwidget_text_content + '# Download libebur128 source code, build it and install.\n' + '\n'.join(git_commands) + '\n'
		eight_window_textwidget_text_content = eight_window_textwidget_text_content+ '\n'.join(simplified_build_and_install_commands_displayed_to_user) + '\n'
		
	install_commands_text_widget.delete('1.0', 'end')
	install_commands_text_widget.insert('1.0', eight_window_textwidget_text_content)
		
	call_eigth_frame_on_top()
	
def show_installation_output_messages(*args):
	
	global eight_window_textwidget_text_content
	global all_installation_messages
	
	eight_window_textwidget_text_content = all_installation_messages
	
	install_commands_text_widget.delete('1.0', 'end')
	install_commands_text_widget.insert('1.0', eight_window_textwidget_text_content)
	
	call_eigth_frame_on_top()
	
def install_missing_programs(*args):
	
	global apt_get_commands
	global needed_packages_install_commands
	global libebur128_dependencies_install_commands
	global git_commands
	global cmake_commands
	global make_build_and_install_commands
	global debug
	global external_program_installation_has_been_already_run
	global all_installation_messages
	global directory_for_os_temporary_files
	
	an_error_has_happened = False
	all_installation_messages = ''
	
	password = root_password.get()  + '\n' # Add a carriage return after the root password	
	password = password.encode('utf-8') # Convert password from string to binary format.
	
	if needed_packages_install_commands != []:
	
		###################################################
		# Run apt-get as root to install missing programs #
		###################################################
		
		# Create the commandline we need to run as root.
		commands_to_run = ['sudo', '-k', '-p', '', '-S']
		commands_to_run.extend(apt_get_commands)
		commands_to_run.extend(needed_packages_install_commands)

		seventh_window_label_16['foreground'] = 'dark green'
		seventh_window_label_17['foreground'] = 'dark green'
		seventh_window_message_1.set('Note: The GUI freezes while I run some external commands.\nPlease wait patiently :)')
		seventh_window_message_2.set('Installing program packages...')
		
		# Update window.
		seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
		
		# Get Frame dimensions and resize root_window to fit the whole frame.
		root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
		
		# Get root window geometry and center it on screen.
		root_window.update()
		x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
		y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
		root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
		
		# The user might come to this window again after an error message, resize the window again.
		seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
		
		# Get Frame dimensions and resize root_window to fit the whole frame.
		root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
		
		# Get root window geometry and center it on screen.
		root_window.update()
		x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
		y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
		root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
		
		if debug == True:
			print()
			print('Running commands:', commands_to_run)

		# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
		sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
		sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
		all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
		
		if debug == True:
			print()
			print('sudo_stdout:', sudo_stdout)
			print('sudo_stderr:', sudo_stderr)
		
		# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
		if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
			show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
			an_error_has_happened = True
	
	if an_error_has_happened == False:
		
		find_paths_to_all_external_programs_we_need()
		set_button_and_label_states_on_window_seven()
		call_seventh_frame_on_top()
		
		if libebur128_dependencies_install_commands != []:
	
			#################################################################
			# Run apt-get as root to install missing libebur128 dependecies #
			#################################################################
			
			# Create the commandline we need to run as root.
			commands_to_run = ['sudo', '-k', '-p', '', '-S']
			commands_to_run.extend(apt_get_commands)
			commands_to_run.extend(libebur128_dependencies_install_commands)

			seventh_window_label_16['foreground'] = 'dark green'
			seventh_window_label_17['foreground'] = 'dark green'
			seventh_window_message_1.set('Note: The GUI freezes while I run some external commands.\nPlease wait patiently :)')
			seventh_window_message_2.set('Installing libebur128 dependencies...')
			
			# The user might come to this window again after an error message, resize the window again.
			seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
			
			# Get Frame dimensions and resize root_window to fit the whole frame.
			root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
			
			# Get root window geometry and center it on screen.
			root_window.update()
			x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
			y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
			root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
			
			if debug == True:
				print()
				print('Running commands:', commands_to_run)

			# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
			sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
			sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
			sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
			all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
			
			if debug == True:
				print()
				print('sudo_stdout:', sudo_stdout)
				print('sudo_stderr:', sudo_stderr)
			
			# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
			if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
				show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
				an_error_has_happened = True
		
	if an_error_has_happened == False:
		
		find_paths_to_all_external_programs_we_need()
		set_button_and_label_states_on_window_seven()
		call_seventh_frame_on_top()
		
		if git_commands != []:

			############################################################################################
			# Write libebur128 source code download commands to '/tmp/libebur128_download_commands.sh' #
			############################################################################################
			
			libebur128_source_downloadfile = 'libebur128_download_commands.sh'
			
			try:
				with open(directory_for_os_temporary_files + os.sep + libebur128_source_downloadfile, 'wt') as libebur128_source_downloadfile_handler:
					libebur128_source_downloadfile_handler.write('#!/bin/bash\n' + '\n'.join(git_commands))
					libebur128_source_downloadfile_handler.flush() # Flushes written data to os cache
					os.fsync(libebur128_source_downloadfile_handler.fileno()) # Flushes os cache to disk
			except IOError as reason_for_error:
				error_in_string_format = 'Error opening file ' + directory_for_os_temporary_files + os.sep + libebur128_source_downloadfile + ' for writing ' + str(reason_for_error)
				show_error_message_on_seventh_window('', error_in_string_format)
				an_error_has_happened = True
			except OSError as reason_for_error:
				error_in_string_format = 'Error opening file ' + directory_for_os_temporary_files + os.sep + libebur128_source_downloadfile + ' for writing ' + str(reason_for_error)
				show_error_message_on_seventh_window('', error_in_string_format)
				an_error_has_happened = True
						
			if an_error_has_happened == False:
					
				#############################################################
				# Change '/tmp/libebur128_download_commands.sh' permissions #
				#############################################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', directory_for_os_temporary_files + os.sep + libebur128_source_downloadfile]

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
		
			if an_error_has_happened == False:
					
				#######################################################
				# Change '/tmp/libebur128_download_commands.sh' owner #
				#######################################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', directory_for_os_temporary_files + os.sep + libebur128_source_downloadfile]

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
		
			if an_error_has_happened == False:
					
				##############################################
				# Run '/tmp/libebur128_download_commands.sh' #
				##############################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', directory_for_os_temporary_files + os.sep + libebur128_source_downloadfile]
				
				seventh_window_label_16['foreground'] = 'dark green'
				seventh_window_label_17['foreground'] = 'dark green'
				seventh_window_message_1.set('Note: The GUI freezes while I run some external commands.\nPlease wait patiently :)')
				seventh_window_message_2.set('Downloading libebur128 source code...')
				
				# The user might come to this window again after an error message, resize the window again.
				seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
				
				# Get Frame dimensions and resize root_window to fit the whole frame.
				root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
				
				# Get root window geometry and center it on screen.
				root_window.update()
				x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
				y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
				root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
	
			if an_error_has_happened == False:
				
				find_paths_to_all_external_programs_we_need()
				set_button_and_label_states_on_window_seven()
				call_seventh_frame_on_top()

				####################################################
				# Write cmake commands to '/tmp/cmake_commands.sh' #
				####################################################
				
				cmake_commandfile = 'cmake_commands.sh'
				
				try:
					with open(directory_for_os_temporary_files + os.sep + cmake_commandfile, 'wt') as cmake_commandfile_handler:
						cmake_commandfile_handler.write('#!/bin/bash\n' + '\n'.join(cmake_commands))
						cmake_commandfile_handler.flush() # Flushes written data to os cache
						os.fsync(cmake_commandfile_handler.fileno()) # Flushes os cache to disk
				except IOError as reason_for_error:
					error_in_string_format = 'Error opening file ' + directory_for_os_temporary_files + os.sep + cmake_commandfile + ' for writing ' + str(reason_for_error)
					show_error_message_on_seventh_window('', error_in_string_format)
					an_error_has_happened = True
				except OSError as reason_for_error:
					error_in_string_format = 'Error opening file ' + directory_for_os_temporary_files + os.sep + cmake_commandfile + ' for writing ' + str(reason_for_error)
					show_error_message_on_seventh_window('', error_in_string_format)
					an_error_has_happened = True
						
			if an_error_has_happened == False:
					
				###############################################
				# Change '/tmp/cmake_commands.sh' permissions #
				###############################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', directory_for_os_temporary_files + os.sep + cmake_commandfile]

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
		
			if an_error_has_happened == False:
					
				#########################################
				# Change '/tmp/cmake_commands.sh' owner #
				#########################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', directory_for_os_temporary_files + os.sep + cmake_commandfile]

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
		
			if an_error_has_happened == False:
					
				################################
				# Run '/tmp/cmake_commands.sh' #
				################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', directory_for_os_temporary_files + os.sep + cmake_commandfile]
				
				seventh_window_label_16['foreground'] = 'dark green'
				seventh_window_label_17['foreground'] = 'dark green'
				seventh_window_message_1.set('Note: The GUI freezes while I run some external commands.\nPlease wait patiently :)')
				seventh_window_message_2.set('Preparing to compile libebur128 source...')
				
				# The user might come to this window again after an error message, resize the window again.
				seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
				
				# Get Frame dimensions and resize root_window to fit the whole frame.
				root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
				
				# Get root window geometry and center it on screen.
				root_window.update()
				x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
				y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
				root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
	
			if an_error_has_happened == False:
				
				find_paths_to_all_external_programs_we_need()
				set_button_and_label_states_on_window_seven()
				call_seventh_frame_on_top()

				############################################################
				# Write make commands to '/tmp/make_and_build_commands.sh' #
				############################################################
				
				make_and_build_commandfile = 'make_and_build_commands.sh'
				
				try:
					with open(directory_for_os_temporary_files + os.sep + make_and_build_commandfile, 'wt') as make_and_build_commandfile_handler:
						make_and_build_commandfile_handler.write('#!/bin/bash\n' + '\n'.join(make_build_and_install_commands))
						make_and_build_commandfile_handler.flush() # Flushes written data to os cache
						os.fsync(make_and_build_commandfile_handler.fileno()) # Flushes os cache to disk
				except IOError as reason_for_error:
					error_in_string_format = 'Error opening file ' + directory_for_os_temporary_files + os.sep + make_and_build_commandfile + ' for writing ' + str(reason_for_error)
					show_error_message_on_seventh_window('', error_in_string_format)
					an_error_has_happened = True
				except OSError as reason_for_error:
					error_in_string_format = 'Error opening file ' + directory_for_os_temporary_files + os.sep + make_and_build_commandfile + ' for writing ' + str(reason_for_error)
					show_error_message_on_seventh_window('', error_in_string_format)
					an_error_has_happened = True
						
			if an_error_has_happened == False:
					
				########################################################
				# Change '/tmp/make_and_build_commands.sh' permissions #
				########################################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chmod', '755', directory_for_os_temporary_files + os.sep + make_and_build_commandfile]

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
		
			if an_error_has_happened == False:
					
				##################################################
				# Change '/tmp/make_and_build_commands.sh' owner #
				##################################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', 'chown', 'root:root', directory_for_os_temporary_files + os.sep + make_and_build_commandfile]

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
					an_error_has_happened = True
		
			if an_error_has_happened == False:
					
				#########################################
				# Run '/tmp/make_and_build_commands.sh' #
				#########################################
				
				# Create the commandline we need to run as root.
				commands_to_run = ['sudo', '-k', '-p', '', '-S', directory_for_os_temporary_files + os.sep + make_and_build_commandfile]
				
				seventh_window_label_16['foreground'] = 'dark green'
				seventh_window_label_17['foreground'] = 'dark green'
				seventh_window_message_1.set('Note: The GUI freezes while I run some external commands.\nPlease wait patiently :)')
				seventh_window_message_2.set('Compiling libebur128 source...')
				
				# The user might come to this window again after an error message, resize the window again.
				seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
				
				# Get Frame dimensions and resize root_window to fit the whole frame.
				root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
				
				# Get root window geometry and center it on screen.
				root_window.update()
				x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
				y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
				root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

				if debug == True:
					print()
					print('Running commands:', commands_to_run)

				# Run our commands as root. The root password is piped to sudo stdin by the '.communicate(input=password)' method.
				sudo_stdout, sudo_stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=password)
				sudo_stdout_string = str(sudo_stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				sudo_stderr_string = str(sudo_stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
				all_installation_messages = all_installation_messages + '-' * 80 + '\n' + sudo_stdout_string + sudo_stderr_string
				
				if debug == True:
					print()
					print('sudo_stdout:', sudo_stdout)
					print('sudo_stderr:', sudo_stderr)
				
				# If 'error' or 'fail' exist in std_err output then an error happened, check for the cause for the error.
				if ('error' in sudo_stderr_string.lower()) or ('fail' in sudo_stderr_string.lower()) or ('try again' in sudo_stderr_string.lower()):
					show_error_message_on_seventh_window(sudo_stderr, sudo_stderr_string)
			
	external_program_installation_has_been_already_run = True
	
	# Install BackupParanoia.py, HeartBeat_Checker.py and init scripts.
	seventh_window_label_16['foreground'] = 'dark green'
	seventh_window_label_17['foreground'] = 'dark green'
	seventh_window_message_1.set('Note: The GUI freezes while I run some external commands.\nPlease wait patiently :)')
	seventh_window_message_2.set('Installing LoudnessCorrection and init scripts...')
	
	# The user might come to this window again after an error message, resize the window again.
	seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
	find_paths_to_all_external_programs_we_need()
	set_button_and_label_states_on_window_seven()
	
	an_error_has_happened = install_init_scripts_and_config_files()
	
	find_paths_to_all_external_programs_we_need()
	set_button_and_label_states_on_window_seven()
	
	if (an_error_has_happened == False) and (all_needed_external_programs_are_installed == True) and (loudnesscorrection_scripts_are_installed.get() == 'Installed'):
		seventh_window_label_16['foreground'] = 'dark green'
		seventh_window_label_17['foreground'] = 'dark green'
		seventh_window_loudnesscorrection_label['foreground'] = 'dark green'
		seventh_window_message_1.set('Success :)')
		seventh_window_message_2.set('You can go ahead and click the NEXT button.')
		
		# The user might come to this window again after an error message, resize the window again.
		seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
		
		# Get Frame dimensions and resize root_window to fit the whole frame.
		root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
		
		# Get root window geometry and center it on screen.
		root_window.update()
		x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
		y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
		root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
	call_seventh_frame_on_top()

def show_error_message_on_seventh_window(error_in_binary_format, error_in_string_format):
	
	# If sudo stderror output includes string 'try again', then password was not valid.
	# Display an error message to the user. If user inputs wrong passwords many times in a row, change error messages between two messages.
	
	if 'try again' in error_in_string_format:
		if seventh_window_error_message_1.get() == 'Wrong password !!!!!!!':
			seventh_window_error_message_1.set('Wrong password again !!!!!!!')
		else:
			seventh_window_error_message_1.set('Wrong password !!!!!!!')
	else:
		# We don't know what the reason for error was, print the sudo error message on the window for the user.
		seventh_window_error_message_1.set('Error !!!!!!!\n\n')
		seventh_window_error_message_2.set(error_in_string_format)
	
	# Assign message to the variable that actually displays the error message on label.
	seventh_window_message_1.set(seventh_window_error_message_1.get())
	seventh_window_message_2.set(seventh_window_error_message_2.get())
	
	# Set message color to red.
	seventh_window_label_16['foreground'] = 'red'
	seventh_window_label_17['foreground'] = 'red'
		
	# The error message may bee too long to display on the current window, resize the window again.
	seventh_frame.update() # Update the frame that has possibly changed, this triggers updating all child objects.
	
	# Get Frame dimensions and resize root_window to fit the whole frame.
	root_window.geometry(str(seventh_frame.winfo_reqwidth()+40) +'x'+ str(seventh_frame.winfo_reqheight()))
	
	# Get root window geometry and center it on screen.
	root_window.update()
	x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
	y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
	root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))
	
	if debug == True:
		print()
		print('error_in_binary_format =', error_in_binary_format)	

def get_ip_addresses_of_the_host_machine():
	
	global all_ip_addresses_of_the_machine
	
	# Create the commandline we need to run as root.
	commands_to_run = ['hostname', '-I']

	if debug == True:
		print()
		print('Running commands:', commands_to_run)

	# Run our command.
	stdout, stderr = subprocess.Popen(commands_to_run, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	stdout = str(stdout.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	stderr = str(stderr.decode('UTF-8')) # Convert sudo possible error output from binary to UTF-8 text.
	
	all_ip_addresses_of_the_machine = stdout.split()
	
	return(all_ip_addresses_of_the_machine)
	
	if debug == True:
		print()
		print('stdout:', stdout)
		print('stderr:', stderr)
		print('all_ip_addresses_of_the_machine =', all_ip_addresses_of_the_machine)

def set_sample_peak_measurement_method(*args):
	
	global peak_measurement_method
	
	if sample_peak.get() == True:
		peak_measurement_method = '--peak=sample'
	else:
		peak_measurement_method = '--peak=true'
	
	if debug == True:
		true_false_string = [False, True]
		print()
		print('sample_peak =', true_false_string[sample_peak.get()])
		print('peak_measurement_method =', peak_measurement_method)


###############################
# Main program starts here :) #
###############################

# Set the following variable to True to print variable changes on the shell display as they happen.
debug = False

# Create the root GUI window.
root_window = tkinter.Tk()
root_window.title("LoudnessCorrection Installer Program, version " + version + '.')
#root_window.geometry('800x600')
root_window.grid_columnconfigure(0, weight=1)
root_window.grid_rowconfigure(0, weight=1)

# Define text wrap length
text_wrap_length_in_pixels = 500

# Define some tkinter variables
first_window_label_text = tkinter.StringVar()
language = tkinter.StringVar()
language.set('english')
target_path = tkinter.StringVar()
target_path.set('/')
hotfolder_path = tkinter.StringVar()
directory_for_temporary_files = tkinter.StringVar()
directory_for_results = tkinter.StringVar()
hotfolder_path_truncated_for_display = tkinter.StringVar()
directory_for_temporary_files_truncated_for_display = tkinter.StringVar()
directory_for_results_truncated_for_display = tkinter.StringVar()
directory_for_error_logs = tkinter.StringVar()
directory_for_error_logs_truncated_for_display = tkinter.StringVar()
file_expiry_time_in_minutes = tkinter.StringVar()
number_of_processor_cores = tkinter.StringVar()
write_html_progress_report = tkinter.BooleanVar()
write_html_progress_report.set(True)
web_page_path = tkinter.StringVar()
web_page_path_truncated_for_display = tkinter.StringVar()
create_a_ram_disk_for_html_report = tkinter.BooleanVar()
create_a_ram_disk_for_html_report.set(True)
ram_device_name = tkinter.StringVar()
user_account = tkinter.StringVar()
root_password = tkinter.StringVar()
root_password_was_not_accepted_message = tkinter.StringVar()
use_samba  = tkinter.BooleanVar()
use_samba.set(True)
web_page_name = tkinter.StringVar()
sample_peak = tkinter.BooleanVar()
sample_peak.set(True)

# Define variables that will be used as the text content on seventh window. The variables can hold one of two values: 'Installed' / 'Not Installed'.
ffmpeg_is_installed = tkinter.StringVar()
sox_is_installed = tkinter.StringVar()
gnuplot_is_installed = tkinter.StringVar()	
samba_is_installed = tkinter.StringVar()
libebur128_is_installed = tkinter.StringVar()
loudnesscorrection_scripts_are_installed = tkinter.StringVar()
seventh_window_message_1 = tkinter.StringVar()
seventh_window_message_2 = tkinter.StringVar()
seventh_window_error_message_1 = tkinter.StringVar()
seventh_window_error_message_2 = tkinter.StringVar()

# Define Email variables
send_error_messages_by_email = tkinter.BooleanVar()
send_error_messages_by_email.set(False)
use_tls = tkinter.BooleanVar()
use_tls.set(False)
smtp_server_requires_authentication = tkinter.BooleanVar()
smtp_server_requires_authentication.set(False)
smtp_server_name = tkinter.StringVar()
smtp_server_port = tkinter.StringVar()
smtp_username = tkinter.StringVar()
smtp_password = tkinter.StringVar()
email_sending_interval_in_minutes = tkinter.StringVar()
email_addresses_string = tkinter.StringVar()
email_address_1 = tkinter.StringVar()
email_address_2 = tkinter.StringVar()
email_address_3 = tkinter.StringVar()
email_address_4 = tkinter.StringVar()
email_address_5 = tkinter.StringVar()
email_sending_details = {}
message_recipients = []
heartbeat = tkinter.BooleanVar()
heartbeat.set(False)
email_sending_message_1 = tkinter.StringVar()
email_sending_message_2 = tkinter.StringVar()

# We need to know when user inputs a new value in a combobox and call a subroutine that writes that value to our variable.
# To achieve this we must trace when the combobox value changes.
smtp_server_name.trace('w', define_smtp_server_name)
smtp_server_port.trace('w', define_smtp_server_port)

# Define some normal python variables
english = 1
finnish = 0
file_expiry_time = 28800
email_sending_interval = 600
message_text_string = ''
list_of_ram_devices = []
list_of_normal_users_accounts = []
loudness_correction_init_script_content = []
ram_disk_mount_commands = []
delay_between_directory_reads = 5
natively_supported_file_formats = ['.wav', '.flac', '.ogg']
ffmpeg_output_format = 'flac'
silent = True
html_progress_report_write_interval = 5
send_error_messages_to_logfile = True
heartbeat_file_name = '00-HeartBeat.pickle'
heartbeat_write_interval = 30
where_to_send_error_messages = ['logfile'] # Tells where to print / send the error messages. The list can have any or all of these values: screen, logfile, email.
configfile_path = '/etc/Loudness_Correction_Settings.pickle'
loudnesscorrection_init_script_name = 'loudnesscorrection_init_script'
loudnesscorrection_init_script_path = '/etc/init.d/' + loudnesscorrection_init_script_name
loudnesscorrection_init_script_link_name = 'S99' + loudnesscorrection_init_script_name
loudnesscorrection_init_script_link_path = '/etc/rc2.d/' + loudnesscorrection_init_script_link_name
all_needed_external_programs_are_installed = True
external_program_installation_has_been_already_run = False
eight_window_textwidget_text_content  = ''
all_installation_messages = ''
all_ip_addresses_of_the_machine = []
all_ip_addresses_of_the_machine = get_ip_addresses_of_the_host_machine()
peak_measurement_method = '--peak=sample'

# Get the directory the os uses for storing temporary files.
directory_for_os_temporary_files = tempfile.gettempdir()

# Define global variables that later hold paths to external programs that LoudnessCorrection nedds to operate.
python3_path = ''
ffmpeg_path = ''
sox_path = ''
gnuplot_path = ''
samba_path = ''
loudness_path = ''

# Find paths to all critical programs we need to run LoudnessCorrection
find_paths_to_all_external_programs_we_need()

# Check if we need to install some programs that LoudnessCorrection needs and add install commands to list.
apt_get_commands = ['apt-get', '-q=2', '-y', 'install']
needed_packages_install_commands = []
libebur128_dependencies_install_commands = []
git_commands = []

if sox_path == '':
	needed_packages_install_commands.append('sox')
if ffmpeg_path == '':
	needed_packages_install_commands.append('ffmpeg')
if gnuplot_path == '':
	needed_packages_install_commands.append('gnuplot')
if samba_path == '':
	needed_packages_install_commands.append('samba')
if loudness_path == '':
	libebur128_dependencies_install_commands = ['build-essential', 'git', 'cmake', 'libsndfile-dev', 'libmpg123-dev', 'libmpcdec-dev', \
	'libglib2.0-dev', 'libfreetype6-dev', 'librsvg2-dev', 'libspeexdsp-dev', 'libavcodec-dev', 'libavformat-dev', 'libtag1-dev', \
	'libxml2-dev', 'libgstreamer0.10-dev', 'libgstreamer-plugins-base0.10-dev', 'libqt4-dev']
if loudness_path == '':
	# Store commands of downloading and building libebur128 sourcecode to lists.
	git_commands = ['cd ' + directory_for_os_temporary_files, 'git clone http://github.com/jiixyj/libebur128.git', 'cd libebur128', \
	'mv .gitmodules .gitmodules.orig', "cat .gitmodules.orig | sed 's/git:\/\//http:\/\//g' > .gitmodules", \
	'git submodule init', 'git submodule update']

	cmake_commands = ['cd ' + directory_for_os_temporary_files + '/libebur128', 'mkdir build', 'cd build', 'cmake -Wno-dev -DCMAKE_INSTALL_PREFIX:PATH=/usr ..']
	make_build_and_install_commands = ['cd ' + directory_for_os_temporary_files + '/libebur128/build', 'make -w', 'make install']
	simplified_build_and_install_commands_displayed_to_user = ['mkdir build', 'cd build', 'cmake -Wno-dev -DCMAKE_INSTALL_PREFIX:PATH=/usr ..', 'make -w', 'make install']

# Find the path to LoudnessCorrection.py and HeartBeat_Checker.py in the current directory.
path_to_loudnesscorrection = find_program_in_current_dir('LoudnessCorrection.py')
path_to_heartbeat_checker = find_program_in_current_dir('HeartBeat_Checker.py')

# Define initial samba configuration
samba_configuration_file_content = ['# Samba Configuration File', \
'', \
'[global]', \
'workgroup = WORKGROUP', \
'server string = %h server (Samba, LoudnessCorrection)', \
'force create mode = 0777', \
'unix extensions = no', \
'log file = /var/log/samba/log.%m', \
'max log size = 1000', \
'syslog = 0', \
'panic action = /usr/share/samba/panic-action %d', \
'security = share', \
'socket options = TCP_NODELAY', \
'', \
'[LoudnessCorrection]', \
'comment = LoudnessCorrection', \
'read only = no', \
'locking = no', \
'path = /LoudnessCorrection', \
'guest ok = yes', \
'browseable = yes']
samba_configuration_file_content_as_a_string = '\n'.join(samba_configuration_file_content)

# Create frames inside the root window to hold other GUI elements. All frames and widgets must be created in the main program, otherwise they are not accessible in subroutines. 
first_frame=tkinter.ttk.Frame(root_window)
first_frame.grid(column=0, row=0, padx=20, pady=5, columnspan=4, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

first_frame_child_frame_1=tkinter.ttk.Frame(first_frame)
first_frame_child_frame_1['borderwidth'] = 2
first_frame_child_frame_1['relief'] = 'sunken'
first_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
	
second_frame=tkinter.ttk.Frame(root_window)
second_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame_child_frame_1=tkinter.ttk.Frame(second_frame)
second_frame_child_frame_1['borderwidth'] = 2
second_frame_child_frame_1['relief'] = 'sunken'
second_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame_child_frame_2=tkinter.ttk.Frame(second_frame)
second_frame_child_frame_2['borderwidth'] = 2
second_frame_child_frame_2['relief'] = 'sunken'
second_frame_child_frame_2.grid(column=0, row=1, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame_child_frame_3=tkinter.ttk.Frame(second_frame)
second_frame_child_frame_3['borderwidth'] = 2
second_frame_child_frame_3['relief'] = 'sunken'
second_frame_child_frame_3.grid(column=0, row=2, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame_child_frame_4=tkinter.ttk.Frame(second_frame)
second_frame_child_frame_4['borderwidth'] = 2
second_frame_child_frame_4['relief'] = 'sunken'
second_frame_child_frame_4.grid(column=0, row=3, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

third_frame=tkinter.ttk.Frame(root_window)
third_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

third_frame_child_frame_1=tkinter.ttk.Frame(third_frame)
third_frame_child_frame_1['borderwidth'] = 2
third_frame_child_frame_1['relief'] = 'sunken'
third_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

fourth_frame=tkinter.ttk.Frame(root_window)
fourth_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

fourth_frame_child_frame_1=tkinter.ttk.Frame(fourth_frame)
fourth_frame_child_frame_1['borderwidth'] = 2
fourth_frame_child_frame_1['relief'] = 'sunken'
fourth_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

fifth_frame=tkinter.ttk.Frame(root_window)
fifth_frame.columnconfigure(0, weight=1)
fifth_frame.columnconfigure(1, weight=1)
fifth_frame.columnconfigure(2, weight=1)
fifth_frame.columnconfigure(3, weight=1)
fifth_frame.rowconfigure(0, weight=1)
fifth_frame.rowconfigure(1, weight=0)
fifth_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

fifth_frame_child_frame_1=tkinter.ttk.Frame(fifth_frame)
fifth_frame_child_frame_1['borderwidth'] = 2
fifth_frame_child_frame_1['relief'] = 'sunken'
fifth_frame_child_frame_1.columnconfigure(0, weight=1)
fifth_frame_child_frame_1.rowconfigure(0, weight=0)
fifth_frame_child_frame_1.rowconfigure(1, weight=1)
fifth_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

sixth_frame=tkinter.ttk.Frame(root_window)
sixth_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

sixth_frame_child_frame_1=tkinter.ttk.Frame(sixth_frame)
sixth_frame_child_frame_1['borderwidth'] = 2
sixth_frame_child_frame_1['relief'] = 'sunken'
sixth_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

seventh_frame=tkinter.ttk.Frame(root_window)
seventh_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

seventh_frame_child_frame_1=tkinter.ttk.Frame(seventh_frame)
seventh_frame_child_frame_1['borderwidth'] = 2
seventh_frame_child_frame_1['relief'] = 'sunken'
seventh_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

eigth_frame=tkinter.ttk.Frame(root_window)
eigth_frame.columnconfigure(0, weight=1)
eigth_frame.columnconfigure(1, weight=1)
eigth_frame.columnconfigure(2, weight=1)
eigth_frame.columnconfigure(3, weight=1)
eigth_frame.rowconfigure(0, weight=1)
eigth_frame.rowconfigure(1, weight=0)
eigth_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

eigth_frame_child_frame_1=tkinter.ttk.Frame(eigth_frame)
eigth_frame_child_frame_1['borderwidth'] = 2
eigth_frame_child_frame_1['relief'] = 'sunken'
eigth_frame_child_frame_1.columnconfigure(0, weight=1)
eigth_frame_child_frame_1.rowconfigure(0, weight=0)
eigth_frame_child_frame_1.rowconfigure(1, weight=1)
eigth_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

ninth_frame=tkinter.ttk.Frame(root_window)
ninth_frame.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

ninth_frame_child_frame_1=tkinter.ttk.Frame(ninth_frame)
ninth_frame_child_frame_1['borderwidth'] = 2
ninth_frame_child_frame_1['relief'] = 'sunken'
ninth_frame_child_frame_1.grid(column=0, row=0, columnspan=4, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

###########################################################################################################
# Window number 1                                                                                         #
###########################################################################################################

# Define the text message to display on the first window.
# This is the introcution window, with nothing but text on it.
text_wrap_length_in_pixels
first_window_label_text.set('This program lets you configure LoudnessCorrection settings and install all needed Linux init scripts.\n\nAfter configuration LoudnessCorrection starts automatically every time the computer starts up. There will be a 1 - 2 minute delay after boot before LoudnessCorrection is started. This makes sure all needed Linux services are up when we start up.')
first_window_label = tkinter.ttk.Label(first_frame_child_frame_1, textvariable=first_window_label_text, wraplength=text_wrap_length_in_pixels)
first_window_label.grid(column=0, row=0, columnspan=4, pady=10, padx=20, sticky=(tkinter.E, tkinter.N))

# Create the buttons for the frame
first_window_quit_button = tkinter.Button(first_frame, text = "Quit", command = quit_program)
first_window_quit_button.grid(column=1, row=2, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
first_window_next_button = tkinter.Button(first_frame, text = "Next", command = call_second_frame_on_top)
first_window_next_button.grid(column=2, row=2, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 2                                                                                         #
###########################################################################################################

# This window lets put in information for paths, language, how many processor cores to use for processing and file expiry time.

#################
# Child Frame 1 #
#################

# HotFolder path
second_window_label_1 = tkinter.ttk.Label(second_frame_child_frame_1, text='Target Directory:')
second_window_label_1.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))
second_window_target_path_label = tkinter.ttk.Label(second_frame_child_frame_1, textvariable=target_path, wraplength=text_wrap_length_in_pixels)
second_window_target_path_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))
second_window_browse_button = tkinter.Button(second_frame_child_frame_1, text = "Browse", command = get_target_directory, width = 10)
second_window_browse_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
second_window_label_2 = tkinter.ttk.Label(second_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='The directory structure needed by the scripts is automatically created in the target directory. One of the directories that is created is called the HotFolder. HotFolder is the folder that users drop audio files into for loudness correction.\nThe name of the HotFolder is:')
second_window_label_2.grid(column=0, row=2, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

# Define label that shows the hotfolder path
hotfolder_path_label_1 = tkinter.ttk.Label(second_frame_child_frame_1,  textvariable=hotfolder_path_truncated_for_display)
hotfolder_path_label_1.grid(column=0, row=3, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))

# Define a dummy label to show an empty row beneath the others
second_window_dummy_label_1 = tkinter.ttk.Label(second_frame_child_frame_1,  text='')
second_window_dummy_label_1.grid(column=0, row=5, columnspan=2, sticky=(tkinter.W, tkinter.N))

#################
# Child Frame 2 #
#################

# Define items to display in the GUI frames.
second_window_label_3 = tkinter.ttk.Label(second_frame_child_frame_2,  text='Language for HotFolder pathnames and result-graphics:')
second_window_label_3.grid(column=0, row=0, columnspan=2, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

# Language for pathnames and result-graphics
english_radiobutton = tkinter.ttk.Radiobutton(second_frame_child_frame_2, text='English', variable=language, value='english', command=set_directory_names_according_to_language)
finnish_radiobutton = tkinter.ttk.Radiobutton(second_frame_child_frame_2, text='Finnish', variable=language, value='finnish', command=set_directory_names_according_to_language)
english_radiobutton.grid(column=2, row=0, padx=15)
finnish_radiobutton.grid(column=3, row=0, padx=15)

# Define label that shows the hotfolder path
second_window_label_4 = tkinter.ttk.Label(second_frame_child_frame_2, wraplength=text_wrap_length_in_pixels, text='Language setting affects directory names and text language in loudness result graphics. The following directories will be created in the Target Directory:')
second_window_label_4.grid(column=0, row=1, columnspan=4, padx=10, pady=10, sticky=(tkinter.W, tkinter.N))

# Define label that shows the hotfolder path
hotfolder_path_label_2 = tkinter.ttk.Label(second_frame_child_frame_2,  textvariable=hotfolder_path_truncated_for_display)
hotfolder_path_label_2.grid(column=0, row=2, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))

# Define label that shows the path for 'directory_for_results'
directory_for_results_label = tkinter.ttk.Label(second_frame_child_frame_2,  textvariable=directory_for_results_truncated_for_display)
directory_for_results_label.grid(column=0, row=3, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))

# Define label that shows the path for 'web_page_path'
web_page_path_label = tkinter.ttk.Label(second_frame_child_frame_2,  textvariable=web_page_path_truncated_for_display)
web_page_path_label.grid(column=0, row=4, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))

# Define label that shows the path for 'directory_for_error_logs'
directory_for_error_logs_label = tkinter.ttk.Label(second_frame_child_frame_2,  textvariable=directory_for_error_logs_truncated_for_display)
directory_for_error_logs_label.grid(column=0, row=5, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))

# Define label that shows the path for 'directory_for_temporary_files'
directory_for_temporary_files_label = tkinter.ttk.Label(second_frame_child_frame_2,  textvariable=directory_for_temporary_files_truncated_for_display)
directory_for_temporary_files_label.grid(column=0, row=6, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))

# Define a dummy label to show an empty row beneath the others
second_window_dummy_label_2 = tkinter.ttk.Label(second_frame_child_frame_2,  text='')
second_window_dummy_label_2.grid(column=0, row=7, columnspan=2, sticky=(tkinter.W, tkinter.N))

#################
# Child Frame 3 #
#################

# Number of processor to use for processing
second_window_label_4 = tkinter.ttk.Label(second_frame_child_frame_3, text='Number Of Processor Cores to Use:')
second_window_label_4.grid(column=0, row=0, columnspan=2, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))
number_of_processor_cores_combobox = tkinter.ttk.Combobox(second_frame_child_frame_3, justify=tkinter.CENTER, width=4, textvariable=number_of_processor_cores)
number_of_processor_cores_combobox['values'] = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64)
number_of_processor_cores_combobox.set(4)
number_of_processor_cores_combobox.bind('<<ComboboxSelected>>', print_number_of_processors_cores_to_use)
number_of_processor_cores_combobox.grid(column=3, row=0, pady=10, padx=10, sticky=(tkinter.E))
second_window_label_5 = tkinter.ttk.Label(second_frame_child_frame_3, wraplength=text_wrap_length_in_pixels, text='If your HotFolder is on a fast RAID, then selecting more processor cores here than you actually have speeds up processing (For Example select 6 cores, when you only have 2 real ones). Each file that is processed ties up two processor cores. Selecting more cores here results in more files being processed in parallel. It is adviced that you test different settings to find the sweet spot of your machine.')
second_window_label_5.grid(column=0, row=1, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

#################
# Child Frame 4 #
#################

# File expiry time
second_window_label_6 = tkinter.ttk.Label(second_frame_child_frame_4, text='File expiry time in minutes: \n\nFiles that have been in Hotfolder for longer than this time, will be automatically deleted.')
second_window_label_6.grid(column=0, row=0, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))
file_expiry_time_in_minutes_combobox = tkinter.ttk.Combobox(second_frame_child_frame_4, justify=tkinter.CENTER, width=5, textvariable=file_expiry_time_in_minutes)
file_expiry_time_in_minutes_combobox['values'] = (60, 90, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960)
file_expiry_time_in_minutes_combobox.set(480)
file_expiry_time_in_minutes_combobox.bind('<<ComboboxSelected>>', convert_file_expiry_time_to_seconds)
file_expiry_time_in_minutes_combobox.grid(column=3, row=0, pady=10, padx=10, sticky=(tkinter.N))

# Create the buttons under childframes
second_window_back_button = tkinter.Button(second_frame, text = "Back", command = call_first_frame_on_top)
second_window_back_button.grid(column=1, row=5, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
second_window_next_button = tkinter.Button(second_frame, text = "Next", command = call_third_frame_on_top)
second_window_next_button.grid(column=2, row=5, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 3                                                                                         #
###########################################################################################################

# Email settings and send test email.

# Define label and two buttons (enable / disable email settings)
third_window_label_1 = tkinter.ttk.Label(third_frame_child_frame_1, text='Send LoudnessCorrection error messages through email:')
third_window_label_1.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))
send_error_messages_by_email_true_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='Yes', variable=send_error_messages_by_email, value=True, command=enable_email_settings)
send_error_messages_by_email_false_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='No', variable=send_error_messages_by_email, value=False, command=enable_email_settings)
send_error_messages_by_email_true_button.grid(column=1, row=0, padx=15)
send_error_messages_by_email_false_button.grid(column=2, row=0, padx=15)

third_window_label_10 = tkinter.ttk.Label(third_frame_child_frame_1, text='(Settings to use for Gmail:   TLS = yes   Authentication = yes   Server name = smtp.gmail.com   Port = 587.)', foreground='dark gray')
third_window_label_10.grid(column=0, row=1, pady=10, padx=10, columnspan=3, sticky=(tkinter.W, tkinter.N))

third_window_label_2 = tkinter.ttk.Label(third_frame_child_frame_1, text='Smtp Server requires TLS encryption:')
third_window_label_2.grid(column=0, row=2, padx=10, sticky=(tkinter.W, tkinter.N))

use_tls_true_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='Yes', variable=use_tls, value=True, command=print_use_tls)
use_tls_false_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='No', variable=use_tls, value=False, command=print_use_tls)
use_tls_true_button.state(['disabled'])
use_tls_false_button.state(['disabled'])
use_tls_true_button.grid(column=1, row=2, padx=15)
use_tls_false_button.grid(column=2, row=2, padx=15)

third_window_label_3 = tkinter.ttk.Label(third_frame_child_frame_1, text='Smtp Server requires authentication:')
third_window_label_3.grid(column=0, row=3, padx=10, sticky=(tkinter.W, tkinter.N))

smtp_server_requires_authentication_true_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='Yes', variable=smtp_server_requires_authentication, value=True, command=print_smtp_server_requires_authentication)
smtp_server_requires_authentications_false_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='No', variable=smtp_server_requires_authentication, value=False, command=print_smtp_server_requires_authentication)
smtp_server_requires_authentication_true_button.state(['disabled'])
smtp_server_requires_authentications_false_button.state(['disabled'])
smtp_server_requires_authentication_true_button.grid(column=1, row=3, padx=15)
smtp_server_requires_authentications_false_button.grid(column=2, row=3, padx=15)

# Define a dummy label to space out groups of rows.
third_window_dummy_label_0 = tkinter.ttk.Label(third_frame_child_frame_1,  text='')
third_window_dummy_label_0.grid(column=0, row=4, sticky=(tkinter.W, tkinter.E))

# Smtp server name
third_window_label_4 = tkinter.ttk.Label(third_frame_child_frame_1, text='Smtp server name:')
third_window_label_4.grid(column=0, row=5, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

smtp_server_name_combobox = tkinter.ttk.Combobox(third_frame_child_frame_1, textvariable=smtp_server_name)
smtp_server_name_combobox['values'] = ('smtp.gmail.com')
smtp_server_name_combobox.state(['disabled'])
smtp_server_name_combobox.grid(column=2, row=5, padx=10, sticky=(tkinter.N, tkinter.E))

# Smtp server port
third_window_label_5 = tkinter.ttk.Label(third_frame_child_frame_1, text='Smtp server port:')
third_window_label_5.grid(column=0, row=6, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

smtp_server_port_combobox = tkinter.ttk.Combobox(third_frame_child_frame_1, textvariable=smtp_server_port)
smtp_server_port_combobox['values'] = (25, 465, 587)
smtp_server_port_combobox.state(['disabled'])
smtp_server_port_combobox.grid(column=2, row=6, padx=10, sticky=(tkinter.N, tkinter.E))

# Define a dummy label to space out groups of rows.
third_window_dummy_label_1 = tkinter.ttk.Label(third_frame_child_frame_1,  text='')
third_window_dummy_label_1.grid(column=0, row=7, sticky=(tkinter.W, tkinter.E))

# Smtp username
third_window_label_6 = tkinter.ttk.Label(third_frame_child_frame_1, text='Smtp user name')
third_window_label_6.grid(column=0, row=8, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

smtp_username_entrybox = tkinter.ttk.Entry(third_frame_child_frame_1, width=35, textvariable=smtp_username)
smtp_username_entrybox.state(['disabled'])
smtp_username_entrybox.grid(column=2, row=8, padx=10, sticky=(tkinter.N, tkinter.E))
smtp_username_entrybox.bind('<Key>', print_smtp_username)

# Smtp password
third_window_label_7 = tkinter.ttk.Label(third_frame_child_frame_1, text='Smtp password')
third_window_label_7.grid(column=0, row=9, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

smtp_password_entrybox = tkinter.ttk.Entry(third_frame_child_frame_1, width=35, textvariable=smtp_password, show='*')
smtp_password_entrybox.state(['disabled'])
smtp_password_entrybox.grid(column=2, row=9, padx=10, sticky=(tkinter.N, tkinter.E))
smtp_password_entrybox.bind('<Key>', print_smtp_password)

# Define a dummy label to space out groups of rows.
third_window_dummy_label_2 = tkinter.ttk.Label(third_frame_child_frame_1,  text='')
third_window_dummy_label_2.grid(column=0, row=10, sticky=(tkinter.W, tkinter.E))

# Email sending interval
third_window_label_8 = tkinter.ttk.Label(third_frame_child_frame_1, text='Email sending interval in minutes:')
third_window_label_8.grid(column=0, row=11, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

email_sending_interval_combobox = tkinter.ttk.Combobox(third_frame_child_frame_1, justify=tkinter.CENTER, width=5, textvariable=email_sending_interval_in_minutes)
email_sending_interval_combobox['values'] = (1, 2, 3, 4, 5, 10, 12, 15, 18, 20, 25, 30, 40, 50, 60, 90, 120, 180, 240, 300)
email_sending_interval_combobox.set(10)
email_sending_interval_combobox.state(['disabled'])
email_sending_interval_combobox.bind('<<ComboboxSelected>>', convert_email_sending_interval_to_seconds)
email_sending_interval_combobox.grid(column=2, row=11, padx=10, sticky=(tkinter.N, tkinter.E))

# Email sending recipients
third_window_label_9 = tkinter.ttk.Label(third_frame_child_frame_1, text='Add email addresses separated\nby commas and press Enter:')
third_window_label_9.grid(column=0, row=12, pady=10, padx=10, rowspan=2, sticky=(tkinter.W, tkinter.N))

email_address_entrybox = tkinter.ttk.Entry(third_frame_child_frame_1, width=45, textvariable=email_addresses_string)
email_address_entrybox.state(['disabled'])
email_address_entrybox.grid(column=1, row=12, pady=10, padx=10, columnspan=3, sticky=(tkinter.N, tkinter.E))
email_address_entrybox.bind('<Return>', add_email_addresses_to_list)

# Define a dummy label to space out groups of rows.
third_window_dummy_label_3 = tkinter.ttk.Label(third_frame_child_frame_1,  text='')
third_window_dummy_label_3.grid(column=0, row=13, sticky=(tkinter.W, tkinter.E))

email_address_text_1 = tkinter.ttk.Label(third_frame_child_frame_1, text='Email address 1:')
email_address_text_1.grid(column=0, row=14, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))
email_address_label_1 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_address_1)
email_address_label_1.grid(column=1, row=14, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

email_address_text_2 = tkinter.ttk.Label(third_frame_child_frame_1, text='Email address 2:')
email_address_text_2.grid(column=0, row=15, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))
email_address_label_2 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_address_2)
email_address_label_2.grid(column=1, row=15, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

email_address_text_3 = tkinter.ttk.Label(third_frame_child_frame_1, text='Email address 3:')
email_address_text_3.grid(column=0, row=16, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))
email_address_label_3 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_address_3)
email_address_label_3.grid(column=1, row=16, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

email_address_text_4 = tkinter.ttk.Label(third_frame_child_frame_1, text='Email address 4:')
email_address_text_4.grid(column=0, row=17, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))
email_address_label_4 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_address_4)
email_address_label_4.grid(column=1, row=17, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

email_address_text_5 = tkinter.ttk.Label(third_frame_child_frame_1, text='Email address 5:')
email_address_text_5.grid(column=0, row=18, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))
email_address_label_5 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_address_5)
email_address_label_5.grid(column=1, row=18, padx=10, columnspan=2, sticky=(tkinter.W, tkinter.N))

# Define a dummy label to space out groups of rows.
third_window_dummy_label_4 = tkinter.ttk.Label(third_frame_child_frame_1,  text='')
third_window_dummy_label_4.grid(column=0, row=19, sticky=(tkinter.W, tkinter.E))

# Heartbeat settings
third_window_label_11 = tkinter.ttk.Label(third_frame_child_frame_1, text='Start HeartBeat Checker:')
third_window_label_11.grid(column=0, row=20, padx=10, sticky=(tkinter.W, tkinter.N))

heartbeat_true_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='Yes', variable=heartbeat, value=True, command=print_heartbeat)
heartbeat_false_button = tkinter.ttk.Radiobutton(third_frame_child_frame_1, text='No', variable=heartbeat, value=False, command=print_heartbeat)
heartbeat_true_button.state(['disabled'])
heartbeat_false_button.state(['disabled'])
heartbeat_true_button.grid(column=1, row=20, padx=15)
heartbeat_false_button.grid(column=2, row=20, padx=15)

third_window_label_12 = tkinter.ttk.Label(third_frame_child_frame_1, text="HeartBeat Checker monitors the health of LoudnessCorrection's threads and sends email if one stops.")
third_window_label_12.grid(column=0, row=21, pady=10, padx=10, columnspan=3, sticky=(tkinter.W, tkinter.N))

# Define a horizontal line to space out groups of rows.
third_window_separator_1 = tkinter.ttk.Separator(third_frame_child_frame_1, orient=tkinter.HORIZONTAL)
third_window_separator_1.grid(column=0, row=22, padx=10, columnspan=3, sticky=(tkinter.W, tkinter.E))

# Define another label.
third_window_label_14 = tkinter.ttk.Label(third_frame_child_frame_1, text="Send a test email using the above settings")
third_window_label_14.grid(column=0, row=23, padx=10, pady=10, columnspan=3, sticky=(tkinter.W, tkinter.N))

third_window_send_button = tkinter.Button(third_frame_child_frame_1, text = "Send", command = send_test_email)
third_window_send_button.grid(column=2, row=23, pady=10, sticky=(tkinter.N))	
third_window_send_button['state'] = 'disabled'

# Define a horizontal line to space out groups of rows.
third_window_separator_2 = tkinter.ttk.Separator(third_frame_child_frame_1, orient=tkinter.HORIZONTAL)
third_window_separator_2.grid(column=0, row=24, padx=10, columnspan=3, sticky=(tkinter.W, tkinter.E))

# Define labels that are used to display error or success messages.
third_window_label_15 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_sending_message_1, wraplength=text_wrap_length_in_pixels)
third_window_label_15.grid(column=0, row=25, padx=10, pady=5, columnspan=3, sticky=(tkinter.W, tkinter.N))

third_window_label_17 = tkinter.ttk.Label(third_frame_child_frame_1, textvariable=email_sending_message_2, wraplength=text_wrap_length_in_pixels)
third_window_label_17.grid(column=0, row=26, padx=10, pady=5, columnspan=3, sticky=(tkinter.W, tkinter.N))

# Create the buttons for the frame
third_window_back_button = tkinter.Button(third_frame, text = "Back", command = call_second_frame_on_top)
third_window_back_button.grid(column=1, row=1, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
third_window_next_button = tkinter.Button(third_frame, text = "Next", command = call_fourth_frame_on_top)
third_window_next_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 4                                                                                         #
###########################################################################################################

# This window lets the user define if he want's html-report written on disk or and a ram disk created for writing it in.

# Html - report settings
fourth_window_label_1 = tkinter.ttk.Label(fourth_frame_child_frame_1, text='Write html progress report:')
fourth_window_label_1.grid(column=0, row=0, columnspan=2, padx=10, sticky=(tkinter.W, tkinter.N))
write_html_progress_report_true_radiobutton = tkinter.ttk.Radiobutton(fourth_frame_child_frame_1, text='Yes', variable=write_html_progress_report, value=True, command=print_write_html_progress_report)
write_html_progress_report_false_radiobutton = tkinter.ttk.Radiobutton(fourth_frame_child_frame_1, text='No', variable=write_html_progress_report, value=False, command=print_write_html_progress_report)
write_html_progress_report_true_radiobutton.grid(column=3, row=0, padx=15)
write_html_progress_report_false_radiobutton.grid(column=4, row=0, padx=15)

# Ram - disk.
fourth_window_label_2 = tkinter.ttk.Label(fourth_frame_child_frame_1, text='Create a ram - disk for html report:')
fourth_window_label_2.grid(column=0, row=2, columnspan=2, padx=10, sticky=(tkinter.W, tkinter.N))
create_a_ram_disk_for_html_report_true_radiobutton = tkinter.ttk.Radiobutton(fourth_frame_child_frame_1, text='Yes', variable=create_a_ram_disk_for_html_report, value=True, command=print_create_a_ram_disk_for_html_report_and_toggle_next_button_state)
create_a_ram_disk_for_html_report_false_radiobutton = tkinter.ttk.Radiobutton(fourth_frame_child_frame_1, text='No', variable=create_a_ram_disk_for_html_report, value=False, command=print_create_a_ram_disk_for_html_report_and_toggle_next_button_state)
create_a_ram_disk_for_html_report_true_radiobutton.grid(column=3, row=2, padx=15)
create_a_ram_disk_for_html_report_false_radiobutton.grid(column=4, row=2, padx=15)

# Some explanatory texts.
twentyfirst_label = tkinter.ttk.Label(fourth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Html progress report is a live view into LoudnessCorrection process queue showing a list of files being processed, waiting in the queue and 100 last completed files.\n\nProgress report is a html-file in the HotFolder that can be viewed with a web-browser. The page updates every 5 seconds and because of this needs speedy access to the disk. During heavy disk traffic html-page cannot be updated frequently enough unless a ram disk is created and mounted as the directory where the html-page is written into.')
twentyfirst_label.grid(column=0, row=3, pady=10, padx=10, columnspan=4, sticky=(tkinter.W, tkinter.N))

# Define a horizontal line to space out groups of rows.
fourth_window_separator_1 = tkinter.ttk.Separator(fourth_frame_child_frame_1, orient=tkinter.HORIZONTAL)
fourth_window_separator_1.grid(column=0, row=4, padx=10, pady=10, columnspan=5, sticky=(tkinter.W, tkinter.E))

# Ram device name.
fourth_window_label_3 = tkinter.ttk.Label(fourth_frame_child_frame_1, text='Use this ram device for creating the ram disk:')
fourth_window_label_3.grid(column=0, row=5, columnspan=4, padx=10, sticky=(tkinter.W, tkinter.N))
ram_device_name_combobox = tkinter.ttk.Combobox(fourth_frame_child_frame_1, justify=tkinter.CENTER, textvariable=ram_device_name)
# Get the ram device names from the os.
error_happened, error_message, list_of_ram_devices = get_list_of_ram_devices_from_os()
if error_happened == True:
	fourth_window_error_label_1 = tkinter.ttk.Label(fourth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, foreground='red', text=error_message)
	fourth_window_error_label_1.grid(column=0, row=10, columnspan=4, padx=10, pady=10, sticky=(tkinter.W, tkinter.N))
ram_device_name_combobox['values'] = list_of_ram_devices
if len(list_of_ram_devices) > 0:
	ram_device_name_combobox.set(list_of_ram_devices[0])
ram_device_name_combobox.bind('<<ComboboxSelected>>', print_ram_device_name)
ram_device_name_combobox.grid(column=3, row=5, columnspan=2, padx=10, sticky=(tkinter.N))

# Create another label with explanatory text on it.
fourth_window_label_4 = tkinter.ttk.Label(fourth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text="If you know you haven't used ram - devices for anything on this computer, then you can just select the first ram device /dev/ram1.")
fourth_window_label_4.grid(column=0, row=6, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

# Define a horizontal line to space out groups of rows.
fourth_window_separator_1 = tkinter.ttk.Separator(fourth_frame_child_frame_1, orient=tkinter.HORIZONTAL)
fourth_window_separator_1.grid(column=0, row=7, padx=10, pady=10, columnspan=5, sticky=(tkinter.W, tkinter.E))

# Choose which username LoudnessCorrection will run under.
fourth_window_label_5 = tkinter.ttk.Label(fourth_frame_child_frame_1, text='Which user account LoudnessCorrection will use to run:')
fourth_window_label_5.grid(column=0, row=8, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))
username_combobox = tkinter.ttk.Combobox(fourth_frame_child_frame_1, justify=tkinter.CENTER, textvariable=user_account)
# Get user account names from the os.
error_happened, error_message, list_of_normal_useraccounts = get_list_of_normal_user_accounts_from_os()
if error_happened == True:
	fourth_window_error_label_2 = tkinter.ttk.Label(fourth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, foreground='red', text=error_message)
	fourth_window_error_label_2.grid(column=0, row=11, columnspan=4, padx=10, pady=10, sticky=(tkinter.W, tkinter.N))
username_combobox['values'] = list_of_normal_useraccounts
if len(list_of_normal_useraccounts) > 0:
	username_combobox.set(list_of_normal_useraccounts[0])
username_combobox.bind('<<ComboboxSelected>>', print_user_account)
username_combobox.grid(column=3, row=8, columnspan=2, pady=10, padx=10, sticky=(tkinter.N))

fourth_window_label_7 = tkinter.ttk.Label(fourth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='LoudnessCorrection will be run with non root privileges, you can choose here which user account to use.\n\nIf you choose the HotFolder to be shared to the network with Samba in the next screen, the HotFolder directory structure read and write permissions will be set so that only this user has write access to files in Hotfolder directories and all other users can only read.')
fourth_window_label_7.grid(column=0, row=9, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

# Define a horizontal line to space out groups of rows.
fourth_window_separator_1 = tkinter.ttk.Separator(fourth_frame_child_frame_1, orient=tkinter.HORIZONTAL)
fourth_window_separator_1.grid(column=0, row=10, padx=10, pady=10, columnspan=5, sticky=(tkinter.W, tkinter.E))

# Peak metering settings
fourth_window_label_1 = tkinter.ttk.Label(fourth_frame_child_frame_1, text='Peak measurement method:')
fourth_window_label_1.grid(column=0, row=11, columnspan=2, padx=10, sticky=(tkinter.W, tkinter.N))
sample_peak_radiobutton = tkinter.ttk.Radiobutton(fourth_frame_child_frame_1, text='Sample Peak', variable=sample_peak, value=True, command=set_sample_peak_measurement_method)
true_peak_radiobutton = tkinter.ttk.Radiobutton(fourth_frame_child_frame_1, text='TruePeak', variable=sample_peak, value=False, command=set_sample_peak_measurement_method)
sample_peak_radiobutton.grid(column=3, row=11, padx=15)
true_peak_radiobutton.grid(column=4, row=11, padx=15)

# Some explanatory texts.
peak_measurement_label = tkinter.ttk.Label(fourth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='This options lets you choose if you want to use sample peak or TruePeak measurement. The peak value is important only in cases where file loudness is below target -23 LUFS and needs to be increased. If increasing volume would cause peaks to go over a set limit (-2 dBFS for TruePeak and -4 dB for sample peak) then a protective limiter is used. The resulting max peaks will be about 1 dB above the limit (-1 dBFS / -3 dBFS).\n\nNote that using TruePeak slows down file processing by a factor of 4. When using sample peak you still have about 3 dBs headroom for the true peaks to exist.')
peak_measurement_label.grid(column=0, row=12, pady=10, padx=10, columnspan=4, sticky=(tkinter.W, tkinter.N))

# Create the buttons for the frame
fourth_window_back_button = tkinter.Button(fourth_frame, text = "Back", command = call_third_frame_on_top)
fourth_window_back_button.grid(column=1, row=1, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
fourth_window_next_button = tkinter.Button(fourth_frame, text = "Next", command = call_fifth_frame_on_top)

# If we were no successful in getting the list of ram device names from the os and create_ram_disk = True, disable the next button.
if (len(list_of_ram_devices) == 0) and (create_a_ram_disk_for_html_report.get() == True):
	fourth_window_next_button['state'] = 'disabled'
# If we were not successful in getting the list of user accounts from the os, disable the next button.
if len(list_of_normal_useraccounts) == 0:
	fourth_window_next_button['state'] = 'disabled'
fourth_window_next_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 5                                                                                         #
###########################################################################################################

# Define a label and two buttons for Samba configuration enable / disable.
fifth_window_label_1 = tkinter.ttk.Label(fifth_frame_child_frame_1,  text='Share HotFolder to the network with Samba:')
fifth_window_label_1.grid(column=0, row=0, columnspan=2, pady=20, padx=10, sticky=(tkinter.W, tkinter.N))

# Language for pathnames and result-graphics
enable_samba_radiobutton = tkinter.ttk.Radiobutton(fifth_frame_child_frame_1, text='Yes', variable=use_samba, value=True, command=print_use_samba_variable_and_toggle_text_widget)
disable_samba_radiobutton = tkinter.ttk.Radiobutton(fifth_frame_child_frame_1, text='No', variable=use_samba, value=False, command=print_use_samba_variable_and_toggle_text_widget)
enable_samba_radiobutton.grid(column=2, row=0, padx=15, pady=20)
disable_samba_radiobutton.grid(column=3, row=0, padx=15, pady=20)

# Create a text widget to display the samba configuration.
samba_config_text_widget = tkinter.Text(fifth_frame_child_frame_1, width=80, height=40, wrap='none', undo=True)
samba_config_text_widget.insert('1.0', samba_configuration_file_content_as_a_string)
samba_config_text_widget.columnconfigure(0, weight=1)
samba_config_text_widget.rowconfigure(0, weight=1)
samba_config_text_widget['background'] = 'white'
samba_config_text_widget.bind('<Control z>', undo_text_in_text_widget) # Bind Ctrl+z to our subroutine. The last command of the subroutine stops tkinter from processing system level bound Ctrl+z which would undo too far and empty our text widget totally.
samba_config_text_widget.grid(column=0, row=1, columnspan=4, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

# .edit_modified() returns = 1 if the text in the widget has modified.
# The first insertion of text by this program in the widget is also considered as a modification of text.
# This results in user being able to undo past the first text insestion, resulting in an empty text display.
# To prevent user undoing too far, we set the flag to 'False' after the inital text is inserted.
# After this the user cannot undo so far that the text widget becomes empty.
samba_config_text_widget.edit_modified(False)

# Add scrollbars to the text widget.
samba_config_text_widget_vertical_scrollbar = tkinter.ttk.Scrollbar(fifth_frame_child_frame_1, orient=tkinter.VERTICAL, command=samba_config_text_widget.yview)
samba_config_text_widget.configure(yscrollcommand=samba_config_text_widget_vertical_scrollbar.set)
samba_config_text_widget_vertical_scrollbar.grid(column=5, row=1, sticky=(tkinter.N, tkinter.S))

samba_config_text_widget_horizontal_scrollbar = tkinter.ttk.Scrollbar(fifth_frame_child_frame_1, orient=tkinter.HORIZONTAL, command=samba_config_text_widget.xview)
samba_config_text_widget.configure(xscrollcommand=samba_config_text_widget_horizontal_scrollbar.set)
samba_config_text_widget_horizontal_scrollbar.grid(column=0, row=2, columnspan=4, sticky=(tkinter.W, tkinter.E))

# Create the buttons for the frame
first_window_back_button = tkinter.Button(fifth_frame, text = "Back", command = call_fourth_frame_on_top)
first_window_back_button.grid(column=1, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))
first_window_undo_button = tkinter.Button(fifth_frame, text = "Undo", command = undo_text_in_text_widget)
first_window_undo_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))
first_window_next_button = tkinter.Button(fifth_frame, text = "Next", command = call_sixth_frame_on_top)
first_window_next_button.grid(column=3, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 6                                                                                         #
###########################################################################################################

# Ask for root password

# Create the label for the frame
sixth_window_label_1 = tkinter.ttk.Label(sixth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Root password is needed to write LoudnessCorrection init scripts to system directories:')
sixth_window_label_1.grid(column=0, row=0, columnspan=4, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

root_password_entrybox = tkinter.ttk.Entry(sixth_frame_child_frame_1, width=35, textvariable=root_password, show='*')
root_password_entrybox.grid(column=0, row=1, padx=10, pady=10, sticky=(tkinter.N, tkinter.E))
root_password_entrybox.bind('<Key>', print_root_password)
root_password_entrybox.bind('<Return>', test_if_root_password_is_valid)

# Define label that is used to display error messages.
sixth_window_label_2 = tkinter.ttk.Label(sixth_frame_child_frame_1, foreground='red', textvariable=root_password_was_not_accepted_message, wraplength=text_wrap_length_in_pixels)
sixth_window_label_2.grid(column=0, row=2, padx=10, pady=5, columnspan=4, sticky=(tkinter.W, tkinter.N))

# Create the buttons for the frame
sixth_window_back_button = tkinter.Button(sixth_frame, text = "Back", command = call_fifth_frame_on_top)
sixth_window_back_button.grid(column=1, row=1, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
sixth_window_next_button = tkinter.Button(sixth_frame, text = "Next", command = test_if_root_password_is_valid)
sixth_window_next_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 7                                                                                         #
###########################################################################################################

# Create the labels for the frame
seventh_window_label_1 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='This window displays all external programs LoudnessCorrection needs to do its job.\nAll programs displayed as "Not Installed" must be installed in order to use LoudnessCorrection.')
seventh_window_label_1.grid(column=0, row=0, columnspan=4, padx=10, pady=5, sticky=(tkinter.W, tkinter.N))

# Define a horizontal line to space out groups of rows.
seventh_window_separator_1 = tkinter.ttk.Separator(seventh_frame_child_frame_1, orient=tkinter.HORIZONTAL)
seventh_window_separator_1.grid(column=0, row=1, padx=10, pady=10, columnspan=5, sticky=(tkinter.W, tkinter.E))

# ffmpeg
seventh_window_label_2 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='FFmpeg')
seventh_window_label_2.grid(column=0, row=2, columnspan=1, padx=10, sticky=(tkinter.W, tkinter.N))
seventh_window_label_3 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, textvariable=ffmpeg_is_installed)
seventh_window_label_3.grid(column=3, row=2, columnspan=1, padx=10, sticky=(tkinter.N))

# sox
seventh_window_label_4 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Sox')
seventh_window_label_4.grid(column=0, row=3, columnspan=1, padx=10, sticky=(tkinter.W, tkinter.N))
seventh_window_label_5 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, textvariable=sox_is_installed)
seventh_window_label_5.grid(column=3, row=3, columnspan=1, padx=10, sticky=(tkinter.N))

# gnuplot
seventh_window_label_6 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Gnuplot')
seventh_window_label_6.grid(column=0, row=4, columnspan=1, padx=10, sticky=(tkinter.W, tkinter.N))
seventh_window_label_7 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, textvariable=gnuplot_is_installed)
seventh_window_label_7.grid(column=3, row=4, columnspan=1, padx=10, sticky=(tkinter.N))

# samba
seventh_window_label_8 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Samba')
seventh_window_label_8.grid(column=0, row=5, columnspan=1, padx=10, sticky=(tkinter.W, tkinter.N))
seventh_window_label_9 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, textvariable=samba_is_installed)
seventh_window_label_9.grid(column=3, row=5, columnspan=1, padx=10, sticky=(tkinter.N))

# libebur128
seventh_window_label_10 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Libebur128')
seventh_window_label_10.grid(column=0, row=6, columnspan=1, padx=10, sticky=(tkinter.W, tkinter.N))
seventh_window_label_11 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, textvariable=libebur128_is_installed)
seventh_window_label_11.grid(column=3, row=6, columnspan=1, padx=10, sticky=(tkinter.N))

# LoudnessCorrection
seventh_window_label_12 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='LoudnessCorrection Scripts')
seventh_window_label_12.grid(column=0, row=7, columnspan=1, padx=10, sticky=(tkinter.W, tkinter.N))
loudnesscorrection_scripts_are_installed.set('Not Installed')
seventh_window_loudnesscorrection_label = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, textvariable=loudnesscorrection_scripts_are_installed)
seventh_window_loudnesscorrection_label['foreground'] = 'red'
seventh_window_loudnesscorrection_label.grid(column=3, row=7, columnspan=1, padx=10, sticky=(tkinter.N))

# Define a horizontal line to space out groups of rows.
seventh_window_separator_2 = tkinter.ttk.Separator(seventh_frame_child_frame_1, orient=tkinter.HORIZONTAL)
seventh_window_separator_2.grid(column=0, row=8, padx=10, pady=10, columnspan=5, sticky=(tkinter.W, tkinter.E))

seventh_window_label_14 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Install all missing programs:')
seventh_window_label_14.grid(column=0, row=9, columnspan=2, padx=10, pady=2, sticky=(tkinter.W))
seventh_window_install_button = tkinter.Button(seventh_frame_child_frame_1, text = "Install", command = install_missing_programs)
seventh_window_install_button.grid(column=3, row=9, padx=30, pady=2, sticky=(tkinter.N))

seventh_window_label_15 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Show me the shell commands to install external programs:')
seventh_window_label_15.grid(column=0, row=10, columnspan=2, padx=10, pady=2, sticky=(tkinter.W))
seventh_window_show_button_1 = tkinter.Button(seventh_frame_child_frame_1, text = "Show", command = show_installation_shell_commands)
seventh_window_show_button_1.grid(column=3, row=10, padx=30, pady=2, sticky=(tkinter.N))

# Define a horizontal line to space out groups of rows.
seventh_window_separator_3 = tkinter.ttk.Separator(seventh_frame_child_frame_1, orient=tkinter.HORIZONTAL)
seventh_window_separator_3.grid(column=0, row=11, padx=10, pady=10, columnspan=5, sticky=(tkinter.W, tkinter.E))

# Define labels that are used to display error or success messages.
seventh_window_label_16 = tkinter.ttk.Label(seventh_frame_child_frame_1, textvariable=seventh_window_message_1, wraplength=text_wrap_length_in_pixels)
seventh_window_label_16.grid(column=0, row=12, padx=10, pady=5, columnspan=3, sticky=(tkinter.W, tkinter.N))

seventh_window_label_17 = tkinter.ttk.Label(seventh_frame_child_frame_1, textvariable=seventh_window_message_2, wraplength=text_wrap_length_in_pixels)
seventh_window_label_17.grid(column=0, row=13, padx=10, pady=5, columnspan=3, sticky=(tkinter.W, tkinter.N))

seventh_window_label_18 = tkinter.ttk.Label(seventh_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text='Show me the messages that the installation produced:')
seventh_window_label_18.grid(column=0, row=14, columnspan=2, padx=10, pady=2, sticky=(tkinter.W))
seventh_window_show_button_2 = tkinter.Button(seventh_frame_child_frame_1, text = "Show", command = show_installation_output_messages)
seventh_window_show_button_2.grid(column=3, row=14, padx=30, pady=2, sticky=(tkinter.N))

# Create the buttons for the frame
seventh_window_back_button = tkinter.Button(seventh_frame, text = "Back", command = call_sixth_frame_on_top)
seventh_window_back_button.grid(column=1, row=1, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
seventh_window_next_button = tkinter.Button(seventh_frame, text = "Next", command = call_ninth_frame_on_top)
seventh_window_next_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))	

set_seventh_window_label_texts_and_colors()
set_button_and_label_states_on_window_seven()

###########################################################################################################
# Window number 8                                                                                         #
###########################################################################################################

# Create the label for the frame
eigth_window_label = tkinter.ttk.Label(eigth_frame_child_frame_1, text='You can copy selected text with control + c to clipboard.')
eigth_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.W, tkinter.N))

# Create a text widget to display the installation commands.
install_commands_text_widget = tkinter.Text(eigth_frame_child_frame_1, width=80, height=40, wrap='none', undo=False)
install_commands_text_widget.insert('1.0', eight_window_textwidget_text_content)
install_commands_text_widget.columnconfigure(0, weight=1)
install_commands_text_widget.rowconfigure(0, weight=1)
install_commands_text_widget['background'] = 'white'
install_commands_text_widget.grid(column=0, row=1, columnspan=4, sticky=(tkinter.W, tkinter.N, tkinter.E, tkinter.S))

# Add scrollbars to the text widget.
install_commands_text_widget_vertical_scrollbar = tkinter.ttk.Scrollbar(eigth_frame_child_frame_1, orient=tkinter.VERTICAL, command=install_commands_text_widget.yview)
install_commands_text_widget.configure(yscrollcommand=install_commands_text_widget_vertical_scrollbar.set)
install_commands_text_widget_vertical_scrollbar.grid(column=5, row=1, sticky=(tkinter.N, tkinter.S))

install_commands_text_widget_horizontal_scrollbar = tkinter.ttk.Scrollbar(eigth_frame_child_frame_1, orient=tkinter.HORIZONTAL, command=install_commands_text_widget.xview)
install_commands_text_widget.configure(xscrollcommand=install_commands_text_widget_horizontal_scrollbar.set)
install_commands_text_widget_horizontal_scrollbar.grid(column=0, row=2, columnspan=4, sticky=(tkinter.W, tkinter.E))

# Disable all other key presses on the text widget but control+c.
# The user will not be able to modify text in the window, but he will be able to take a copy of it to the clipboard with Control+c.
install_commands_text_widget.bind('<Control c>', lambda ctrl_c: '')
install_commands_text_widget.bind('<Key>', lambda any_key: 'break')

# Create the Back - button for the frame
eigth_window_back_button = tkinter.Button(eigth_frame, text = "Back", command = call_seventh_frame_on_top)
eigth_window_back_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

###########################################################################################################
# Window number 9                                                                                         #
###########################################################################################################

# Create the label for the frame
ninth_window_label = tkinter.ttk.Label(ninth_frame_child_frame_1, wraplength=text_wrap_length_in_pixels, text="Everything was installed successfully :)\n\nLoudnessCorrection will be started when you boot up your computer, or you can start it now manually with the command:\n\nsudo   -b   /etc/init.d/loudnesscorrection_init_script   start'\n\nNote that there will be 90 seconds delay before LoudnessCorrection starts, HearBeat_Checker will start 60 seconds after LoudnessCorrection.")
ninth_window_label.grid(column=0, row=0, columnspan=4, pady=10, padx=10, sticky=(tkinter.N))

# Create the buttons for the frame
ninth_window_back_button = tkinter.Button(ninth_frame_child_frame_1, text = "Back", command = call_seventh_frame_on_top)
ninth_window_back_button.grid(column=1, row=1, padx=30, pady=10, sticky=(tkinter.E, tkinter.N))
ninth_window_finish_button = tkinter.Button(ninth_frame_child_frame_1, text = "Finish", command = quit_program)
ninth_window_finish_button.grid(column=2, row=1, padx=30, pady=10, sticky=(tkinter.W, tkinter.N))

##################################
# Window definitions end here :) #
##################################

# Set directory names according to language
set_directory_names_according_to_language()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
ninth_frame.grid_forget()
eigth_frame.grid_forget()
seventh_frame.grid_forget()
sixth_frame.grid_forget()
fifth_frame.grid_forget()
fourth_frame.grid_forget()
third_frame.grid_forget()
second_frame.grid_forget()

## Set ttk window theme.
## Themes found in Ubuntu 12.04 are:
## ('clam', 'alt', 'default', 'classic')
#ttk_theme_name = 'clam'
#window_theme = tkinter.ttk.Style()
#available_styles = window_theme.theme_names()
## If a style named 'clam' is available, use it.
#if ttk_theme_name in available_styles:
#window_theme.theme_use(ttk_theme_name)

# Get root window geometry and center it on screen.
root_window.update()
x_position = (root_window.winfo_screenwidth() / 2) - (root_window.winfo_width() / 2) - 8
y_position = (root_window.winfo_screenheight() / 2) - (root_window.winfo_height() / 2) - 20
root_window.geometry(str(root_window.winfo_width()) + 'x' +str(root_window.winfo_height()) + '+' + str(int(x_position)) + '+' + str(int(y_position)))

# Start tkinter event - loop
root_window.mainloop()