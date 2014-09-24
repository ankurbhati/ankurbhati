$(document).ready(function(){
	$('#search-blogs').on('click', function(){
		$this = $(this);
		window.location = $this.data('url')+$('input[name="search-text"]').val();
	});
});
