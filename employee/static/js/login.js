document.getElementById("loginForm").addEventListener("submit", function(event) {
    const username = document.querySelector("input[name='username']").value; // Get username input value
    const password = document.querySelector("input[name='password']").value; // Get password input value

    // Simple validation
    if (username.trim() === "" || password.trim() === "") {
        alert("Please fill in both fields.");
        event.preventDefault(); // Prevent form submission
    }
});

document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.getElementById('passwordField');
    const icon = this;
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        icon.textContent = '🙈'; // Change icon to indicate password is visible
    } else {
        passwordField.type = 'password';
        icon.textContent = '👁️'; // Change icon back to show password
    }
});