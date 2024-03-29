// gets data from the server
function httpGet(theUrl)
{
	var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

// function to get the IEEE format
function ieee(fnum=document.getElementById('infloat').value)
{
	//fnum=document.getElementById('infloat').value;
	url="/experiment/"+fnum
	ret={}
	ret=httpGet(url) //requests server for the IEEE format of input
	ret=JSON.parse(ret)
	if (ret['status']=="fail")  //Input is not a valid float
	{
		$("#ftable tr").remove();
		document.getElementById('cont').innerHTML="<br>Enter a vaid floating point number."
	}
	else
	{
		//remove the existing table and add a new one
		document.getElementById('cont').innerHTML="<br>"
		$("#ftable tr").remove();
		// document.getElementById("ftable").deleteRow(0);
		var table = document.getElementById("ftable");
		var row = table.insertRow(0);
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		cell1.innerHTML = "Sign";
		cell2.innerHTML = ret['sign'];
		row = table.insertRow(1);
		cell1 = row.insertCell(0);
		cell2 = row.insertCell(1);
		cell1.innerHTML = "Exponent";
		cell2.innerHTML = ret['exponent'];
		row = table.insertRow(2);
		cell1 = row.insertCell(0);
		cell2 = row.insertCell(1);
		cell1.innerHTML = "Exponent bits";
		cell2.innerHTML = ret['exponent_bits'];
		row = table.insertRow(3);
		cell1 = row.insertCell(0);
		cell2 = row.insertCell(1);
		cell1.innerHTML = "Mantissa/Fraction";
		cell2.innerHTML = ret['mantissa'];
		row = table.insertRow(4);
		cell1 = row.insertCell(0);
		cell2 = row.insertCell(1);
		cell1.innerHTML = "IEEE 754 Representation";
		cell2.innerHTML = ret['final'];
		return final
	}
}
