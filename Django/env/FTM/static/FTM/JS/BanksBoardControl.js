
$(document).ready(function() {
	$.ajaxSetup({ cache: false });

	/* Member ids: */
	var idNathan = 1;
	var idKara = 2;
	var idGrace = 3;
	var idEvie = 4;
	var idTessa = 5;
	var idMikaela = 6;


	document.getElementById('Kara').style.display = 'none';
	//document.getElementById('Kara').style.height = '1%';
	document.getElementById('Nathan').style.display = 'none';
	//document.getElementById('Nathan').style.height = '1%';
	document.getElementById('Evelyn').style.display = 'none';
	//document.getElementById('Evelyn').style.height = '1%';	
	document.getElementById('Grace').style.display = 'none';
	//document.getElementById('Grace').style.height = '1%';	
	document.getElementById('Tessa').style.display = 'none';
	//document.getElementById('Tessa').style.height = '1%';		
		
});

function allowDrop(ev)  {
   ev.preventDefault();
	document.getElementById(ev).children[1].style.display = 'block';
	document.getElementById(ev).children[0].style.display = 'none';
 }
 
 function drag(ev)  {
    ev.dataTransfer.setData("text", ev.target.id);
 }
 
 function showStuff(ev) {	 
	document.getElementById(ev).children[1].style.display = 'block';
	document.getElementById(ev).children[0].style.display = 'none';
}

function hideStuff(ev){
	document.getElementById(ev).children[0].style.display = 'block';
	document.getElementById(ev).children[1].style.display = 'none';	

	var tickets = document.getElementById(ev).getElementsByClassName('modal custModal');

}


 function drop(ev)  {
	
   ev.preventDefault();
   var tId = ev.dataTransfer.getData("text");
   ev.target.appendChild(document.getElementById(tId));
	
    switch(ev.target.id){
	   case "Kara": {
			setTechId(tId,"Kara");
		   break;
	   }
	   case "Evelyn": {
		  setTechId(tId,"Evelyn");
		   break;
	   }
	   case "Nathan": {
			setTechId(tId,"Nathan");
		   break;
	   }
	   case "Grace": {
			setTechId(tId,"Grace");
		   break;
	   }
	   case "waiting": {
			setTechId(tId,"waiting");
		   break;
	   }
	   case "blocked": {
			setTechId(tId,"blocked");
		   break;
	   }	   
	   
	   case "done": {
		   	/* Set ticket to done */
			var jsonObj = {"statustype":{"type":"StatusType","id":3}};
			var jsonStr = JSON.stringify(jsonObj)
			$.ajax({
			  url: "http://helpdesk/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets/"+tId+"?apiKey=GTxT2m6i2rEw4bnbaQ7HjWubPjQVQANJM43iXc2N",
			  contentType: 'application/json',
			  type: 'PUT',
			  data: jsonStr,
			  success: function(data) {}
			});
	   
		   break;
	   }
	   default: {
		   console.log('Working on BackLog.');
		   var jsonObj = {"customFields": [{"definitionId": 30, "restValue": "backlog"}]};
		   var jsonStr = JSON.stringify(jsonObj);

	   /* Set custom attribute to tech id */
		$.ajax({
			  url: "http://helpdesk/helpdesk/WebObjects/Helpdesk.woa/ra/Tickets/"+tId+"?apiKey=GTxT2m6i2rEw4bnbaQ7HjWubPjQVQANJM43iXc2N",
			  contentType: 'application/json',
			  type: 'PUT',
			  data: jsonStr,
			  success: function(data) {
				
			  }
			});


		   break;
	   }	   
	   
   }

 
 }
 /* Ticket Population */
 function popTickets(containerName, buttonClass, theGetUrl){
		$.getJSON(theGetUrl, function(json) {

			 var container = document.getElementById(containerName);
			 for(var i=0; i<json.length; i++){

				var ticket = json[i];
				var latestNote = "No recent notes";
				if (ticket.latestNote !=null) {latestNote = ticket.latestNote.mobileListText;};
				var client = ticket.displayClient;
				var subject = ticket.shortSubject;
				var detail = ticket.shortDetail;
				var button = "<button type='button' draggable='true' class='"+buttonClass+"' data-toggle='modal' data-target='#modal"+ticket.id+"' ondragstart='drag(event)' id='"+ticket.id+"'>"+ticket.id+"<p>"+ticket.shortSubject+"</p></button>";
				container.innerHTML+=button;
				var modal = "<div class='modal custModal' id='modal"+ticket.id+"'>\
							  <div class='modal-dialog'>\
								<div class='modal-content'>\
								  <div class='modal-header'>\
									<h4 class='modal-title'>"+ticket.id+"</h4>\
								  </div>\
								  <div class='modal-body'>\
									<p>Client: "+client+"</p>\
									<p>Subject: "+subject+"</p>\
									<p>Detail: "+detail+"</p>\
									<p>"+latestNote+"</p>\
									<a href='http://helpdesk/helpdesk/WebObjects/Helpdesk.woa/wa/TicketActions/view?ticket="+ticket.id+"' target='_blank'>Ticket: "+ticket.id+"</a>\
								  </div>\
								  <div class='modal-footer'>\
									<button type='button' class='btn btn-primary' data-dismiss='modal'>Close</button>\
								  </div>\
								</div>\
							  </div>\
							</div>"
				container.innerHTML+=modal;

			 };
		});
}
	   /* Set custom attribute to tech id */
function setTechId(ticketId, techName){
	/* TODO change Ticket member assignmetn */
	
}