<?php

$intersept = "intersept if off";
$host = "localhost";
$port = 1234;
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
$result = socket_bind($socket, $host, $port) or die("Could not bind to socket\n");

if(isset($_POST['intersept'])){
	
	$intersept = "intersept is on";
	$result = socket_listen($socket, 3) or die("Could not set up socket listener\n");

	while (True) {
		$spawn = socket_accept($socket) or die("Could not accept incoming connection\n");
		$input = socket_read($spawn, 1024) or die("Could not read input\n");
		
	}
	
	

}



?>
<html>
<head>
	<title>proxy server</title>
	<style>
		textarea {
			width: 70%;
			height: 500px;
			padding: 12px 20px;
			box-sizing: border-box;
			border: 2px solid #ccc;
			border-radius: 4px;
			background-color: #f8f8f8;
			font-size: 15px;
			resize: none;

		}
	</style>
</head>
<body>
	<form method="post" action="">
		<br>
		<input type="submit" name="forward" value="forward">
		<input type="submit" name="drop" value="drop">
		<input type="submit" name="intersept" value="<?php echo $intersept; ?>">
		<br>
		<br>
		<textarea type="textarea" name="data"><?php echo $input; ?></textarea> 
	</form>
</body>
</html>
