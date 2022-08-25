<?php


$servername = "localhost";
$username = '';
$password = '';


if(isset($_POST["username"])){
    try{
        
        $USR = $_POST["username"];
        $conn = new PDO("mysql:host=$servername;dbname=account", $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $sql = "SELECT `user` FROM users WHERE `user`='$USR'";  // vuln query
        $query = $conn->prepare($sql);
        $query->execute();


    ### get data is:

        $resualts = $query->fetchAll(PDO::FETCH_OBJ);
        if(isset($resualts[0]->user)){
            echo (json_encode(array("user"=>"exist")));
        }
        else{
            echo (json_encode(array("user"=>"doesnt exist")));
        }
    }
    catch(PDOException $e){

        echo $e->getMessage();

    }
}