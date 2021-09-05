var today = new Date();
var hourNow = today.getHours();
var greeting;
var username;

username = '';

if (hourNow > 18) {
	greeting = 'Good evening!';
} else if (hourNow > 12) {
	greeting = 'Good afternoon!';
}else if (hourNow > 0){
	greeting = 'Good morning!';
}else {
	greeting = 'Welcome';
}
var elName = document.getElementById('name');
elName.textContent = username;

document.write('<h3>' + greeting + '<h3>');


for (var i=0; i < 0; i++){
	var elName = document.getElementById('name');
	elName.textContent = i;
}