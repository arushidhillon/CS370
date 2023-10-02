<?php

$connect = mysql_connect(“server_name”, “admin_name”, “password”); if (!connect) { die('Connection Failed: ' . mysql_error()); { mysql_select_db(“database_name”, $connect);

$user_tags = “INSERT INTO table_name (skill) VALUES ('$_POST[Skill_input]')”; if (!mysql_query($user_info, $connect)) { die('Error: ' . mysql_error()); }

echo “Your information was added to the database.”;

mysql_close($connect); ?>