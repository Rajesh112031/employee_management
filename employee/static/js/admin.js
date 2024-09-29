// admin.js

document.addEventListener('DOMContentLoaded', function () {
    const linkButton = document.querySelector('.link-button');
    linkButton.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        const confirmed = confirm("Are you sure you want to go to the Employee List?");
        if (confirmed) {
            window.location.href = this.href; // Redirect to the link if confirmed
        }
    });
});
