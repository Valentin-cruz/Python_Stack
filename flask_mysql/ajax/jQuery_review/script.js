$("#container").click(function() {
    // add a new paragraph to the container div
	$("#container").append("<p>New paragraph!</p>");
});
    
$("p").hover(function() {
    	// change the text color of all elements with class 'xyz' to blue
        $(".xyz").css("color", "blue");
    },
    function() {
    	// change the text color of all elements with class 'xyz' to black
        $(".xyz").css("color", "black");
});
