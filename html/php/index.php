<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>File transfer</title>
</head>
<body>
	<form method="post" enctype="multipart/form-data">
		<input type="file" name="file">
		<input type="submit" name="submit">
		
	</form>

</body>
</html>
<?php

if (isset($_POST['submit'])) {
	echo "hello";

	$file_name = $_FILES['file']['name'];
	$file_tmp =$_FILES['file']['tmp_name'];

	if(move_uploaded_file($file_tmp,"file/".$file_name)){
            echo '<p style="color:green;">Successfully file uploaded</p>';
        }
}

?>