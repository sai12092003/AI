<?php
if($_SERVER['REQUEST_METHOD']=='POST')
{
$name=$_POST['name'];
$pass=$_POST['pass'];


$servername="localhost";
$usernmae="root";
$password="";
$dbname= "exam";

$con=mysqli_connect($servername,$usernmae,$password,$dbname);

if(!$con)
{
    echo "sorry".mysqli_connect_error();
}
else{
    $sql="SELECT *  FROM `login` WHERE `email_name`='$name' and `password`= '$pass' ";
    $result=mysqli_query($con,$sql);

    if(mysqli_num_rows($result)>0){
        header("location:home.html");
        exit();
    }
    else{
        header("Loaction:register.html");
        exit();
    }
}


}

?>
