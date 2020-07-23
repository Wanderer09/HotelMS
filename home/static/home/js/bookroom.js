function validation(){
    var firstname = document.getElementById('first-name').value;
    var lastname = document.getElementById('last-name').value;
    var phone = document.getElementById('phone-number').value;
    var town = document.getElementById('town').value;
    var email = document.getElementById('email-address').value;

    var firstcheck = /^[A-Za-z. ]{1,}$/;
    var lastcheck = /^[A-Za-z. ]{1,}$/;
    var phonecheck=/^(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}$/;
    var towncheck =/^[A-za-z ]{1,}$/;
    var emailcheck=/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;

    if (firstcheck.test(firstname)){
        document.getElementById('user-first').innerHTML ="";
        document.getElementById('user-name-first').style.visibility = "hidden";
    }else{
        document.getElementById('user-first').innerHTML ="Please Enter Valid Name";
        document.getElementById('user-name-first').style.visibility = "visible";
        return false;
    }


    if (lastcheck.test(lastname)){
         document.getElementById('user-last').innerHTML ="";
         document.getElementById('user-name-last').style.visibility = "hidden";
    }else{
        document.getElementById('user-last').innerHTML ="Please Enter Valid Name";
        document.getElementById('user-name-last').style.visibility = "visible";
        return false;
    }

    if (phonecheck.test(phone)){
        document.getElementById('user-phone').innerHTML ="";
        document.getElementById('user-name-phone').style.visibility = "hidden";
    }else{
        document.getElementById('user-phone').innerHTML ="Please Enter Valid Phone-Number";
        document.getElementById('user-name-phone').style.visibility = "visible";
        return false;
    }


    if (towncheck.test(town)){
        document.getElementById('user-town').innerHTML ="";
        document.getElementById('user-name-town').style.visibility = "hidden";
    }else{
        document.getElementById('user-town').innerHTML ="Please Enter Valid Town";
        document.getElementById('user-name-town').style.visibility = "visible";
        return false;
    }
   
    if (emailcheck.test(email)){
        document.getElementById('user-email').innerHTML ="";
        document.getElementById('user-name-email').style.visibility = "hidden";
     }else{
         document.getElementById('user-email').innerHTML ="Please Enter Valid Email-Address";
         document.getElementById('user-name-email').style.visibility = "visible";
        return false;
        }
    return false;    
}

