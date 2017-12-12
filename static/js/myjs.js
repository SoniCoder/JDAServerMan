
// alert("hello");

function go(){
    // alert("hellonikhar");
    var q = document.getElementById("search").value;
    var r=document.getElementById("columnName");
    var rtext=r.options[r.selectedIndex].value;
    
    
    window.open("/?q="+q+"&rtext="+rtext,"_self");
}





function exp(){
    
    window.open("/static/output.csv","_self");
}



