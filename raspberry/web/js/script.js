var link;

$('#wrappep').on('click', 'a', function (event) {
	link = $(this).parent().attr('id');
	console.log(link);
})