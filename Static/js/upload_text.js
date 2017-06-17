$(document).ready(function(){
	$("select[name='chapter']").change(function() {
		chp=$("select[name='chapter'] option:selected").attr('value');
		$.post('/upload-options',
		{
			chapter:chp
		},function(data,status){
			$("select[name='subject']").html(data);
		});
	});
	
	$("input[type='radio']").change(function() {
		id=$(this).attr('id');
		$("article[id^='field-']").hide();
		$("#submit").show();
		$("#field-"+id).toggle();		
	});
	
});
