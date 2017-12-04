
// alert("hello");

function go(){
    // alert("hellonikhar");
    var q = document.getElementById("search").value;
    
    window.open("/?q="+q,"_self");
}


function exp(){
    
    window.open("/static/output.csv","_self");
}

var $rows = $('#table tr');
$('#search').keyup(function() {
    
    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;
    
    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).hide();
});

