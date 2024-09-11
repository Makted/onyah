<script>
    // Function for smooth scroll when clicking on navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Interactivity for "Book Now" button
    document.querySelector('.book-now').addEventListener('click', function() {
        alert('Redirecting to the booking page...');
        window.location.href = '#';  // Replace with actual link
    });

    // Play Video functionality
    document.querySelector('.play-video').addEventListener('click', function() {
        alert('Playing video...');
        // Here you can embed a modal or redirect to a video player
    });

    // Sign-Up button alert
    document.querySelector('.sign-up').addEventListener('click', function() {
        alert('Redirecting to the Sign-Up page...');
        window.location.href = '#';  // Replace with actual sign-up link
    });

    // Toggle mobile menu
    const toggleMenu = document.querySelector('.menu-toggle');
    const navbarRight = document.querySelector('.navbar-right');

    toggleMenu.addEventListener('click', () => {
        navbarRight.classList.toggle('active');
    });
</script>