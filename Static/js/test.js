/*
var countQuestions = document.createElement("INPUT");
countQuestions.type = 'hidden';
countQuestions.name = 'count_questions'; 

var autoIncrement = parseInt(getQueryVariable("len_questions"));

function getQueryVariable(variable) {
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for (var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=");
    if (pair[0] == variable) {
      return pair[1];
    }
  } 
  alert('Query Variable ' + variable + ' not found');
}
*/

var autoIncrement = parseInt(document.getElementById("len_questions").value);


function addQuestion(){

	autoIncrement++;
	
	var possibleAns = 1;
	
	var br = document.createElement("BR");
	var br2 = document.createElement("BR");
	var questionDiv = document.createElement("DIV");
	
	var questionText = document.createElement("INPUT");
	
	var possibleAns1 = document.createElement("INPUT");
	var possibleAns2 = document.createElement("INPUT");
	var possibleAns3 = document.createElement("INPUT");
	var possibleAns4 = document.createElement("INPUT");
	
	var possiblePoints = document.createElement("INPUT");
	
	var checkBox1 = document.createElement("INPUT");
	var checkBox2 = document.createElement("INPUT");
	var checkBox3 = document.createElement("INPUT");
	var checkBox4 = document.createElement("INPUT");
	
	var myImg = document.createElement("INPUT")
	/**************************/
	questionDiv.className = 'question-block';
	questionDiv.id = 'QDIV_' + autoIncrement;
	/**************************/
	questionText.type = 'TEXT';
	questionText.className = 'question';
	questionText.name = 'Q_' + autoIncrement;
	questionText.style.fontSize = "15px";
	questionText.placeholder = 'Pregunta';
	questionDiv.appendChild(questionText);
	/**************************/
	possiblePoints.type = 'TEXT';
	possiblePoints.className = 'possible-points';
	possiblePoints.name = 'PossPtsQ_' + autoIncrement;
	possiblePoints.style.fontSize = "15px";
	possiblePoints.placeholder = 'Posibles puntos';
	questionDiv.appendChild(possiblePoints);

	/**************************/
	myImg.type = "FILE";
	myImg.className = 'image';
	myImg.name = 'Q_I'+ autoIncrement;
	myImg.style.fontSize = "15px";
    myImg.style.textAlign = "left";
	myImg.placeholder = 'Cargar Imagen';
	questionDiv.appendChild(myImg);
	
	questionDiv.appendChild(br);
	/**************************/
	
	

	possibleAns1.type = 'TEXT';
	possibleAns1.className = 'answer';
	possibleAns1.name = 'Q_' + autoIncrement + '_A_' + possibleAns;
	possibleAns1.placeholder = 'Respuesta 1';
	checkBox1.type = 'checkbox';
	checkBox1.className = 'checkbox-answer';
	checkBox1.name = 'Q_' + autoIncrement + '_ChkBox_' + possibleAns;
	questionDiv.appendChild(possibleAns1);
	possibleAns1.style.fontSize = "20px";
	questionDiv.appendChild(checkBox1);
	possibleAns++;
	/**************************/
	possibleAns2.type = 'TEXT';
	possibleAns2.className = 'answer';
	possibleAns2.name = 'Q_' + autoIncrement + '_A_' + possibleAns;
	possibleAns2.placeholder = 'Respuesta 2';
	checkBox2.type = 'checkbox';
	checkBox2.className = 'checkbox-answer';
	checkBox2.name = 'Q_' + autoIncrement + '_ChkBox_' + possibleAns;
	questionDiv.appendChild(possibleAns2);
	possibleAns2.style.fontSize = "20px";
	questionDiv.appendChild(checkBox2);
	possibleAns++;
	/**************************/
	possibleAns3.type = 'TEXT';
	possibleAns3.className = 'answer';
	possibleAns3.name = 'Q_' + autoIncrement + '_A_' + possibleAns;
	possibleAns3.placeholder = 'Respuesta 3';
	checkBox3.type = 'checkbox';
	checkBox3.className = 'checkbox-answer';
	checkBox3.name = 'Q_' + autoIncrement + '_ChkBox_' + possibleAns;
	questionDiv.appendChild(possibleAns3);
	possibleAns3.style.fontSize = "20px";
	questionDiv.appendChild(checkBox3);
	/**************************/
	
	possibleAns++;
	/**************************/
	
	possibleAns4.type = 'TEXT';
	possibleAns4.className = 'answer';
	possibleAns4.name = 'Q_' + autoIncrement + '_A_' + possibleAns;
	possibleAns4.placeholder = 'Respuesta 4';
	checkBox4.type = 'checkbox';
	checkBox4.className = 'checkbox-answer';
	checkBox4.name = 'Q_' + autoIncrement + '_ChkBox_' + possibleAns;
	questionDiv.appendChild(possibleAns4);
	possibleAns4.style.fontSize = "20px";
	questionDiv.appendChild(checkBox4);
	
	document.getElementById("len_questions").value = autoIncrement
	var form = document.getElementById("addQuestions");
	form.insertBefore(questionDiv, form.firstChild );


}


function deleteQuestion(){
	var lastQuestion = document.getElementById("QDIV_" + (autoIncrement) );
	lastQuestion.parentNode.removeChild(lastQuestion);
	autoIncrement--;
	document.getElementById("len_questions").value = autoIncrement
}