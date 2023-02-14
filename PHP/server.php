<?php
//this folder and file is temporary 
//to run the server locally go into the PHP file in the console and run the command php -S localhost:8000
    header('Access-Control-Allow-Origin: http://localhost:3000');
    $user = $_POST['name'];
    echo ("Hello from server: $user");
?>
