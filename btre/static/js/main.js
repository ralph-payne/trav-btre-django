const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Use JQuery to do a fadeout
// setTimeout is a JS function that holds off from doing something, and then does something
// setTimeout takes in a function
// We want jQuery to grab the element with the id of message
// We want to do a slow fade-out
// The second paramater for setTimeout is the time (in milliseconds). We put 3000
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);