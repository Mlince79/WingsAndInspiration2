
function sendMail(contactForm) {
    emailjs.send("gmail", "denisse_olsson", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "meeting_request": contactForm.text.value,
})
.then(
    function(response) {
        console.log("SUCCESS", response);
    },
    function(error) {
        console.log("FAILED", error);
    });