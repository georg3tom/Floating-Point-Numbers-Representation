// sends request to the server
function httpGet(theUrl)
{
	var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
//evaluate the quiz
function check(argument)
{
	var form=document.forms["quiz"];
	var q1=5,q2=5,q3=5, q4=5,q5=5,length,k=new Array();
	length = form["q1"].length;
	for(i=0; i<length; i++)
		if(form["q1"][i].checked)
			q1 = form["q1"][i].value;

	length = form["q2"].length;
	for(i=0; i<length; i++)
		if(form["q2"][i].checked)
			q2 = form["q2"][i].value;

	length = form["q3"].length;
	for(i=0; i<length; i++)
		if(form["q3"][i].checked)
			q3 = form["q3"][i].value;

	length = form["q4"].length;
	for(i=0; i<length; i++)
		if(form["q4"][i].checked)
			q4 = form["q4"][i].value;

	k[0]=q1;k[1]=q2;k[2]=q3;k[3]=q4;
	var kk=new Array()
	kk[0]=document.querySelector('.q1').id
	kk[1]=document.querySelector('.q2').id
	kk[2]=document.querySelector('.q3').id
	kk[3]=document.querySelector('.q4').id
	url="/quizzes?q1="+q1+"&q11="+kk[0]+"&q2="+q2+"&q22="+kk[1]+"&q3="+q3+"&q33="+kk[2]+"&q4="+q4+"&q44="+kk[3];
	ret=httpGet(url);
	//ret contains 1s and 0s 1 if it is correct and 0 if it is wrong
	for(i=0;i<4;++i)
	{
		if(ret[i]==1)
		{
			document.getElementById(kk[i]).innerHTML="Correct";
			document.getElementById(kk[i]).style.color="green";
		}
		else if(k[i]!=5)
		{
			document.getElementById(kk[i]).innerHTML="Incorrect";
			document.getElementById(kk[i]).style.color="red";
		}
	}
}
//resets the quiz
function resetq(argument)
{
	var kk=new Array()
	kk[0]=document.querySelector('.q1').id
	kk[1]=document.querySelector('.q2').id
	kk[2]=document.querySelector('.q3').id
	kk[3]=document.querySelector('.q4').id
	for(i=0;i<4;++i)
	{
		document.getElementById(kk[i]).innerHTML="";
	}
	$( "input" ).prop( "checked", false )

}
