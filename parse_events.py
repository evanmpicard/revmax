#!/usr/bin/python
#-*- coding: utf-8 -*-
#this is used to clean text from SQL dump from nanda to SQL LOAD events

import sys
import csv

def fix_string(intext):
	str = intext.decode('utf-8')
	str = str.replace("\u2013", "-") #en dash
	str = str.replace("\u2014", "--") #em dash
	str = str.replace('\n', ' ')
	str = str.replace(',', ' ')
	str = str.replace('^M', '')
	str = str.replace("'", '')
	str = str.replace('"', '')
	# str = str.replace('@', '')
	str = str.encode('utf-8')
	str = str.replace('@', '')
	return str


with open("revmax_all_events_01-01-2017.csv") as file_csv:
	readcsv = csv.reader(file_csv, delimiter=',', skipinitialspace=True)
	for r in readcsv:
		# try:
		venue_latitude = fix_string(r[29])  ## dont bother w the rest of it if there's no geometry
		venue_longitude = fix_string(r[30])
		if venue_longitude and venue_latitude:
			event_id = fix_string(r[0])
			created_at = fix_string(r[1])
			updated_at = fix_string(r[2])

			name = fix_string(r[3])
			start_time = fix_string(r[4])
			handle = fix_string(r[5])
			fid = fix_string(r[6])
			attending_count = fix_string(r[7])
			can_guests_invite = fix_string(r[8])
			category = fix_string(r[9])
			declined_count = fix_string(r[10])
			guest_list_enabled = fix_string(r[11])
			interested_count = fix_string(r[12])
			is_canceled = fix_string(r[13])
			is_page_owned = fix_string(r[14])
			is_viewer_admin = fix_string(r[15])
			maybe_count = fix_string(r[16])
			noreply_count = fix_string(r[17])
			# parent_group = fix_string(r[18])
			# ticket_uri = fix_string(r[19])
			timezone = fix_string(r[20])
			end_time = fix_string(r[21])
			updated_time = fix_string(r[22])
			event_type = fix_string(r[23])
			venue_fid = fix_string(r[24])
			venue_name = fix_string(r[25])
			if '|' in venue_name:
				venue_name_clean, venue_address = venue_name.split('|')
				venue_name = venue_name_clean
			venue_city = fix_string(r[26])
			venue_state = fix_string(r[27])
			venue_country = fix_string(r[28])
			owner_name = fix_string(r[31])
			# cover_source = fix_string(r[32])
			print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (event_id, created_at, updated_at, name, start_time, handle, fid, attending_count, can_guests_invite, category, declined_count, guest_list_enabled, interested_count, is_canceled, is_page_owned, is_viewer_admin, maybe_count, noreply_count, timezone, end_time, updated_time, event_type, venue_fid, venue_name, venue_city, venue_state, venue_country, venue_latitude, venue_longitude)

		# except:
		# 	pass
