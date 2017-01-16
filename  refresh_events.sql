
\qecho 'Truncating events table...'
TRUNCATE events_test;

\qecho 'Creating temp table...'

  CREATE TEMP TABLE temp_events (
                  event_id bigint
                , created_at date
                , updated_at date
                , name varchar
                , start_time timestamp
                , handle text
                , fid bigint
                , attending_count  int
                , can_guests_invite boolean
                , category text
                , declined_count int
                , guest_list_enabled boolean
                , interested_count int
                , is_canceled boolean
                , is_page_owned boolean
                , is_viewer_admin boolean
                , maybe_count int
                , noreply_count int
                , timezone text
                , end_time timestamp
                , updated_time timestamp
                , type text
                , venue_fid bigint
                , venue_name text
                , venue_city text
                , venue_state text
                , venue_country text
                , venue_latitude text
                , venue_longitude text
                );

\qecho 'Copying temp table from csv...'
\qecho :LAST_FILE

--COPY temp_events FROM :LAST_FILE CSV header delimiter ',';
--##EXECUTE format($$COPY zip_codes FROM %L DELIMITER ',' CSV$$, $1);
EXECUTE format($$COPY temp_events FROM %L DELIMITER ',' CSV$$, :LAST_FILE);

\qecho 'Inserting into events table...'
  INSERT INTO events_test 
        SELECT    event_id
                , created_at
                , updated_at
                , name
                , start_time
                , handle
                , fid
                , attending_count
                , can_guests_invite
                , category
                , declined_count
                , guest_list_enabled
                , interested_count
                , is_canceled
                , is_page_owned
                , is_viewer_admin
                , maybe_count
                , noreply_count
                , timezone
                , end_time
                , updated_time
                , type
                , venue_fid
                , venue_name
                , venue_city
                , venue_state
                , venue_country
                , venue_latitude
                , venue_longitude
                , ST_GeomFromText(('POINT(' || venue_longitude || ' ' || venue_latitude || ')'),4326) 
        FROM temp_events;

DROP TABLE temp_events;
\q
