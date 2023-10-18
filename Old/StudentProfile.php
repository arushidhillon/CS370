<?php

$connect = mysql_connect(“server_name”, “admin_name”, “password”); if (!connect) { die('Connection Failed: ' . mysql_error()); { mysql_select_db(“database_name”, $connect);

$user_tags = “INSERT INTO table_name (skill) VALUES ('$_POST[Skill_input]')”; if (!mysql_query($user_tags, $connect)) { die('Error: ' . mysql_error()); }

echo “Your information was added to the database.”;

$user_bios = “INSERT INTO table_name (biography) VALUES ('$_POST[bio]')”; if (!mysql_query($user_bios, $connect)) { die('Error: ' . mysql_error()); }

echo “Your information was added to the database.”;

$user_courses = “INSERT INTO table_name (courses) VALUES ('$_POST[Course_input]')”; if (!mysql_query($user_courses, $connect)) { die('Error: ' . mysql_error()); }

echo “Your information was added to the database.”;

mysql_close($connect); ?>

mysql_close($connect); ?>