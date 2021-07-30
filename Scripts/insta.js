// FOR THE TASKS TO FOLLOW.

let buttons = document.querySelectorAll('button');
let times = 0;

for (button of buttons){

	if(button.textContent == 'Seguir'){

		button.click();
		break;
	}


	else if(times == 4){
  
  // LIKE BUTTON CLICK
		document.querySelector('article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button').click();
		break;
	}

else {

	console.log('No is the button of follow.');
	times++;
}

	};