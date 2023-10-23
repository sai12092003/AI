<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "exam";

$con = mysqli_connect($servername, $username, $password, $dbname);
if (!$con) {
    echo "Sorry, " . mysqli_connect_error();
} else {

    
    if (isset($_GET['delete'])) {
        $emailToDelete = $_GET['delete'];
        $deleteSql = "DELETE FROM `login` WHERE `email_name` = '$emailToDelete'";
        mysqli_query($con, $deleteSql);
    }


    $sql = "SELECT * FROM `login`";
    $result = mysqli_query($con, $sql);

    while ($row = mysqli_fetch_assoc($result)) {
        echo "Email/Name: " . $row['email_name'] . "<br>";
        echo "Password: " . $row['password'] . "<br>";
        echo '<a href="?delete=' . $row['email_name'] . '">Delete</a><br>';
        echo "<hr>"; 
    }
}
?>
