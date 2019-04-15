function httpGet(theUrl)
{
	var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
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

	length = form["q5"].length;
	for(i=0; i<length; i++)
		if(form["q5"][i].checked)
			q5 = form["q5"][i].value;
	k[0]=q1;k[1]=q2;k[2]=q3;k[3]=q4;k[4]=q5;
	url="/quizzes?q1="+q1+"&q2="+q2+"&q3="+q3+"&q4="+q4+"&q5="+q5
	ret=httpGet(url)
	for(i=0;i<5;++i)
	{
		if(ret[i]==1)
			document.getElementById(i+1).innerHTML="Correct"
		else if(k[i]!=5)
			document.getElementById(i+1).innerHTML="Incorrect"
	}
}
function reset(argument)
{
	for(i=0;i<5;++i)
	{
		if(ret[i]==1)
			document.getElementById(i+1).innerHTML=""
		else if(k[i]!=5)
			document.getElementById(i+1).innerHTML=""
	}

	$(document).ready(function(){
    $('.check:button').toggle(function(){
        $('input:radio').attr('checked','checked');
        $(this).val('uncheck all');
    },function(){
        $('input:radio').removeAttr('checked');
        $(this).val('check all');        
    })
	})
	
}
