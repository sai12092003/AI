<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "exam";

$con = mysqli_connect($servername, $username, $password, $dbname);
if (!$con) {
    echo "Sorry, " . mysqli_connect_error();
} else {
    // Connection successful; now fetch all data from the login table
    $sql = "SELECT * FROM `login`";
    $result = mysqli_query($con, $sql);
    
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Email/Name</th><th>Password</th></tr>";
    
    while ($row = mysqli_fetch_assoc($result)) {
        echo "<tr>";
        echo "<td>" . $row['id'] . "</td>";
        echo "<td>" . $row['email_name'] . "</td>";
        echo "<td>" . $row['password'] . "</td>";
        echo "</tr>";
    }
    
    echo "</table>";
}
?>
