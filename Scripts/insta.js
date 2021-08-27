function like_photo_or_video(){

  if (window.location.pathname.indexOf('/p/') > -1){

     document.querySelector('article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button').click();
   }

  else{

    follow_profile();
  }};



function follow_profile(){

for (button of document.querySelectorAll('button')){

  if (button.textContent == 'Seguir'){

    button.click();
    break;
    

}}};


if (window.location.host == 'www.instagram.com'){

    setTimeout(function init(){

      like_photo_or_video();

      } , 6 * 1000 )

    setTimeout(function close_page(){

      window.close();

       } , 13 * 1000)

          };