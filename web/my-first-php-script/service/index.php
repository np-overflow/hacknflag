<html>
<title>Kevin's Ping Script</title>
<body>
<form method=GET>
Enter IP: <input type=text name=ip>
<input type=submit>
</form>
<pre>
<?php
if($_GET['ip'])
{
if(preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\z/m',$_GET['ip'])){
system("ping -c 2 -W 1 " . $_GET['ip']);
}
else{
echo("Invalid IP");
}
}
?>
</pre>
</body>
</html>
