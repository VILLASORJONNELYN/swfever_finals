function sign(){
    var checkboxes = document.getElementsByName('Symptoms');  		
  var arr = [];
    var checkboxesChecked = [];
    for (var i=0; i<checkboxes.length; i++) {
   if (checkboxes[i].checked) {
      checkboxesChecked.push(checkboxes[i].value);
      
  }
  }
  document.getElementById("show").value = checkboxesChecked;
  
  if (checkboxes[0].checked == true){
      arr.push('10')
  }
  else {
      arr.push('0')
  }
  if (checkboxes[1].checked == true){
      arr.push('15')
  }
  else {
      arr.push('0')
  }
  if (checkboxes[2].checked == true){
      arr.push('10')
  }
  else{
      arr.push('0')
  }
  if (checkboxes[3].checked == true){
      arr.push('15')
  }
  else {
      arr.push('0')
  }
  if (checkboxes[4].checked == true){
      arr.push('10')
  }
  else {
      arr.push('0')
  }
  if (checkboxes[5].checked == true){
      arr.push('15')
  }
  else {
      arr.push('0')
  }
  if (checkboxes[6].checked == true){
      arr.push('10')
  }
  else {
      arr.push('0')
  }
  if (checkboxes[7].checked == true){
      arr.push('15')
  }
  else {
      arr.push('0')
  }

  
  a = parseInt(arr[0]) + parseInt(arr[1]) + parseInt(arr[2]) + parseInt(arr[3]) + parseInt(arr[4]) + parseInt(arr[5]) + parseInt(arr[6]) + parseInt(arr[7]);
  document.getElementById('display').innerHTML = "The health condition percentage of pigs is " + a + "%," + " which is not good. The higher the percentage, the greater the risk of pigs dying.";
    }

var i = 1;
function addSymptoms() {
i++;
var div = document.createElement('div');
var id = i;
div.innerHTML = 'Symptoms_' + id + ': <input type="text" name="text1' + id + '"/>' + ' <input type="button" id="add_symptoms()_' + id + '" onclick="addSymptoms()" value="Add" />' + ' <input type="button" id="rem_symptoms()_' + id + '" onclick="remsigns(this)" value="Remove" />';
document.getElementById('signs').appendChild(div);
}

function remsigns(div) {
document.getElementById('signs').removeChild(div.parentNode);
i--;
}