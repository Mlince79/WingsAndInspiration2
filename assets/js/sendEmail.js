
function sendMail(contactForm) {
    emailjs.send("gmail", "denisse_olsson", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "meeting_request": contactForm.meeting.value,
    })
    .then(
        function (response) {
            console.log("SUCCESS", response);
        },
        function (error) {
            console.log("FAILED", error);
        }
    );
    return false;
}

