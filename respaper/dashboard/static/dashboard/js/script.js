console.log($("#origin"))
$("#origin ").sortable({connectWith: "#drop"});
$("#origin2").sortable({connectWith: "#drop"});
$("#drop").sortable({connectWith: "#origin2 , #origin"});

function submit123(){
var idsInOrder = $("#drop").sortable("toArray");
console.log(idsInOrder);}
