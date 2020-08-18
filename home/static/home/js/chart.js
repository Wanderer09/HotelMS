window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer", {    
      theme: "light2",          
      title:{
        text: "Rooms Status"  ,
        fontFamily:'Cabin',
        horizontalAlign:'center',
        fontSize:16,
        padding:13,
        fontWeight:700,

      },   
      axisY:{
        gridColor: "#d8d8de",
        labelFontColor: "#a0a0a0",
        labelFontFamily: "Cabin",
      },
      axisX:{
        labelFontFamily: "Cabin",
        labelFontColor: "#a0a0a0",
      },
      dataPointMaxWidth: 9,
      data: [  //array of dataSeries     
      { //dataSeries - first quarter
   /*** Change type "column" to "bar", "area", "line" or "pie"***/        
       type: "column",
       name: "Booked",
       toolTipContent: "{y} Booked",
       color:"#713bdb",
       dataPoints: [
       { label: "Week-1", y: 258 },
       { label: "Week-2", y: 269 },
       { label: "Week-3", y: 380 },                                    
       { label: "Week-4", y: 174 },
       ]
       
     },
     { //dataSeries - second quarter

      type: "column",
      name: "Cancelled",
      color:"#33d695",
      toolTipContent: "{y} Cancelled",             
      dataPoints: [
      { label: "Week-1", y: 120 },
      { label: "Week-2", y: 90 },
      { label: "Week-3", y: 125 },                                    
      { label: "Week-4", y: 115},
      ]
    },
    ]
  });
  var chartnew = new CanvasJS.Chart("chart",
    {
      title:{
        text:"Monthly Report",
        fontFamily: "Cabin",
        fontWeight: "700",
        fontSize:16,
        padding:10,
      },
      legend: {
        reversed: true,
        horizontalAlign: "center",
        verticalAlign:"top",
      },   
      data: [
      {
       type: "doughnut",
       innerRadius: "86%",
       toolTipContent: "{y} %",
       indexLabel: "{x}",
       showInLegend: true,
       dataPoints: [
       { label:"Cancelled", y: 10 , color:"#fe8b57",legendText:"Cancelled"},
       { label:"Booked" ,y: 70 , color:"#32d69f",legendText:"Booked"},
       { label:"Vaccant", y: 20 , color:"#713bdb",legendText:"Vaccant"}
       ]
     }
     ]
   });
   var chartLine = new CanvasJS.Chart("chart-line",
		{
      theme: "light2", 
			title:{
        text: "Occupancy Rate %",
        fontFamily:'Cabin',
        horizontalAlign:'center',
        fontSize:16,
        padding:13,
        fontWeight:700,
			},    
      axisY:{
        gridColor: "#d8d8de",
        labelFontColor: "#a0a0a0",
        labelFontFamily: "Cabin",
      },
			data: [
			{        
				toolTipContent: "{y} %",
				type: "splineArea",
        markerSize: 0,
        color: "#fe9b6f",
        markerBorderColor:"#feab85",
        lineThickness:3,
        fillOpacity:.1,
				dataPoints: [
          { label: "Week-1", y: 55 },
          { label: "Week-2", y: 79 },
          { label: "Week-3", y: 42 },                                    
          { label: "Week-4", y: 72}   
				]
			}             
			]
    });
    var chartExplode = new CanvasJS.Chart("chart-explode",
    {
        title:{
        text: "Type Of Rooms",
        fontFamily:'Cabin',
        horizontalAlign:'center',
        fontSize:16,
        padding:13,
        fontWeight:700,
      },
      legend: {
        reversed: true,
        horizontalAlign: "center",
        verticalAlign:"top",
        maxHeight: 15,
      },  
      data: [
      {
       type: "doughnut",
       indexLabel: "{x}",
       showInLegend:true,
       innerRadius: "80%",
       maxHeight:15,
       dataPoints: [
       {  y: 120, label:"Luxury", exploded: true , legendText:"Luxury" , color:"#EAB543"},
       {  y: 80, label:"Deluxe", exploded: true , legendText:"Deluxe" , color:"#fe8b57" },
       {  y: 300,label:"Standard" , exploded: true , legendText:"Standard" , color:"#32d69f" },
       {  y: 120,label: "King", exploded: true , legendText:"King" , color:"#B33771"},
       {  y: 130,label:"Queens" , exploded: true , legendText:"Queens", color:"#fb5180"},
       {  y: 250,label: "Triple" , exploded: true , legendText:"Triple",color:"#713bdb"}
       ]
     }
     ]
   });
    chart.render();
    chartnew.render();
    chartLine.render();
    chartExplode.render();
  }    
