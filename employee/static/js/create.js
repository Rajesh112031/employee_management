// create.js
$(document).ready(function () {
    // Form submission event
    $('form').on('submit', function (event) {
        let hasError = false;

        // Validate required fields
        $('input[required], select[required]').each(function () {
            if (!$(this).val()) {
                $(this).addClass('error');
                hasError = true;
            } else {
                $(this).removeClass('error');
            }
        });

        // Check if at least one course is selected
        if ($('input[name="courses"]:checked').length === 0) {
            alert('Please select at least one course.');
            hasError = true;
        }

        // Prevent form submission if there are errors
        if (hasError) {
            event.preventDefault();
        }
    });

    // Display selected courses
    $('input[name="courses"]').change(function () {
        const selectedCourses = $('input[name="courses"]:checked').map(function () {
            return $(this).val();
        }).get().join(', ');

        if (selectedCourses) {
            console.log("Selected courses: " + selectedCourses);
        }
    });
});
