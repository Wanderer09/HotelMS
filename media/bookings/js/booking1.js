
    function validation(){
        var firstname = document.getElementById('first-name').value;
        var lastname = document.getElementById('last-name').value;
        var phone = document.getElementById('phone-number').value;
        var town = document.getElementById('town').value;
        var email = document.getElementById('email-address').value;
        var rooms = document.getElementById('number-rooms').value;
        var guests = document.getElementById('number-guests').value;
        var adults = document.getElementById('number-adults').value;
        var children = document.getElementById('number-children').value;

        var firstcheck = /^[A-Za-z. ]{1,}$/;
        var lastcheck = /^[A-Za-z. ]{1,}$/;
        var phonecheck=/^(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}$/;
        var towncheck =/^[A-za-z ]{1,}$/;
        var emailcheck=/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
        var roomscheck=/^[0-9]{1,}$/;
        var guestscheck=/^[0-9]{1,}$/;
        var adultscheck=/^[0-9]{1,}$/;
        var childrencheck=/^[0-9]{1,}$/;

        if (roomscheck.test(rooms)){
        document.getElementById('user-rooms').style.visibility = "hidden";
        }else{
        document.getElementById('user-rooms').style.visibility = "visible";
        return false;
        }  

        if (guestscheck.test(guests)){
        document.getElementById('user-guests').style.visibility = "hidden" ;
        }else{
        document.getElementById('user-guests').style.visibility = "visible";
        return false;
        }  

        if (adultscheck.test(adults)){
        document.getElementById('user-adults').style.visibility = "hidden";
        }else{
        document.getElementById('user-adults').style.visibility = "visible";
        return false;
        }  
        
        if (childrencheck.test(children)){
            document.getElementById('user-children').style.visibility = "hidden";
        }else{
            document.getElementById('user-children').style.visibility = "visible";
            return false;
        }

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
        return true;  
    }
