$(function(){
    $("#one").on("click", function(){
        var id = $(this).attr("id");
        alert(id);
    });
});

localStorage.setItem("#one");

function newWindow(target) {
    eel.new_window(target);
}