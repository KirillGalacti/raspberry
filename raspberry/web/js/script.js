$(function(){
    $("#one").on("click", function(){
        var id = $(this).attr("id");
        alert(id);
    });
});

localStorage.setItem("#one");