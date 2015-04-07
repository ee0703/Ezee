<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error occured!</title>
    <style>
		body, html{
			padding: 0;
			margin: 0;
			font-family: "Helvetica Neue", "Luxi Sans", "DejaVu Sans", Tahoma, "Hiragino Sans GB", "Microsoft Yahei", sans-serif;
			background: #fff8dc;
			width: 100%;
			height: 100%;
			zoom: 1;
		}
		.head{
			margin-top:0px;
			padding:16px;
			font-size:1.2em;
			background:#000;
			color:#FF9900;
		}
		h2,h3{ padding: 0; margin: 0; }
		pre{
			width: 80%;
			margin: 8px;
			padding: 8px;
			overflow: auto;
			background: #FFF;
			border: 1px solid #e0dcbf;
			white-space: pre-wrap;
		}
		p{
			padding: 8px;
		}

		.footer{
			padding: 16px 8px;
			background: #000;
			color: #FFF;
		}
    </style>
</head>
<body>
	<div class="head">
		<h2>Error Occured: $$err_type !</h2>
	</div>
	<div class="content">
		<p>Here is all the URL Routers:</p>
		<pre>$$urls </pre>
		<p>The Environment is:</p>
		<pre>$$env </pre>
	</div>
    <div class="footer">
    	<h3>Ezee Web FrameWork</h3>
    </div>
</body>
</html>