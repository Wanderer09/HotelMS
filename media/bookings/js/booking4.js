function details(x){
          if(x==0){
           document.getElementById('credit-card-info').style.display="block";
          }
          else{
              document.getElementById('credit-card-info').style.display="none";
          }
          if(x==1){
           document.getElementById('debit-card-info').style.display="block";
          }
          else{
              document.getElementById('debit-card-info').style.display="none";
          }
          if(x==2){
           document.getElementById('debit-card-info').style.display="none";
           document.getElementById('credit-card-info').style.display="none";
          }
          return false;
        }