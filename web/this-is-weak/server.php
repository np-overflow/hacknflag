<?php
$_ENV["SECRET_PASSWORD"] = "pinkponyridingblackjumpingcarnivorouslion";
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $json_str = file_get_contents('php://input');
    $json_obj = json_decode($json_str, true); 
    $password = $json_obj['password'];
    $username = $json_obj['username'];
    if (!isset($password) and !isset($username)){
        $username = $_POST['username'];
        $password = $_POST['password'];
    }
    if($username == 'admin' && $password == $_ENV["SECRET_PASSWORD"]) {
        echo "Here's the flag!";
        include('flag.php');
    }else{
        echo "Wrong credential!";
    }
}else{
?>
<!DOCTYPE html>
<html lang="en">
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<head>
    <title>Safe Admin Page</title>
</head>
<body>
<div id="page">
    <header id="banner">
            <h1>Admin Page</h1>
            <h2>OnLY for ADMINS Don't BOTHER HACKING</h2>
    </header>
        <form id="login" method="post">
            <label for="username">Username:</label>
            <input id="username" name="username" type="text" required>
            <label for="password">Password:</label>
            <input id="password" name="password" type="password" required>                    
            <br />
            <input id="submit" type="submit" value="Login">
        </form>
</div>
</body>
</html>
<?php } ?>