/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

a {
    text-decoration: none;
    color: inherit;
}

/* Navbar Styles */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #2c3e50;
}

.navbar-left a {
    font-size: 1.5rem;
    color: white;
    font-weight: bold;
}

.navbar-right a, .sign-up {
    color: white;
    margin: 0 1rem;
    font-size: 1rem;
    transition: color 0.3s;
}

.navbar-right a:hover, .sign-up:hover {
    color: #3498db;
}

.sign-up {
    background-color: #3498db;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

.navbar-right.active {
    display: block;
}

/* Hero Section */
.hero {
    display: flex;
    justify-content: space-between;
    padding: 4rem;
    background-color: #f3f3f3;
}

.hero-text h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-text p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

.cta-buttons button {
    padding: 0.7rem 1.5rem;
    border: none;
    margin-right: 1rem;
    cursor: pointer;
    transition: background-color 0.3s;
}

.book-now {
    background-color: #3498db;
    color: white;
}

.play-video {
    background-color: #2c3e50;
    color: white;
}

.book-now:hover, .play-video:hover {
    background-color: #2980b9;
}

/* Statistics Section */
.statistics {
    display: flex;
    justify-content: space-around;
    padding: 2rem;
    background-color: #ecf0f1;
}

.stat-box h2 {
    font-size: 2rem;
    color: #2c3e50;
}

.stat-box p {
    color: #7f8c8d;
}

/* Services Section */
.services {
    text-align: center;
    padding: 4rem;
    background-color: #fff;
}

.service-cards {
    display: flex;
    justify-content: space-around;
}

.service-card {
    padding: 1.5rem;
    border: 1px solid #bdc3c7;
    width: 20%;
    transition: box-shadow 0.3s;
}

.service-card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.service-card .icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

/* Doctors Section */
.doctors {
    text-align: center;
    padding: 4rem;
    background-color: #ecf0f1;
}

.doctor-cards {
    display: flex;
    justify-content: space-around;
}

.doctor-card {
    padding: 1.5rem;
    border: 1px solid #bdc3c7;
    width: 20%;
    transition: transform 0.3s;
}

.doctor-card:hover {
    transform: translateY(-10px);
}

/* Footer Section */
footer {
    background-color: #2c3e50;
    color: white;
    padding: 2rem;
}

.footer-top {
    display: flex;
    justify-content: space-between;
}

.footer-logo {
    font-size: 1.5rem;
}

.footer-links ul {
    list-style: none;
    padding: 0;
}

.footer-links a {
    color: white;
    transition: color 0.3s;
}

.footer-links a:hover {
    color: #3498db;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .hero {
        flex-direction: column;
        align-items: center;
    }

    .service-cards, .doctor-cards {
        flex-direction: column;
        align-items: center;
    }

    .service-card, .doctor-card {
        width: 80%;
        margin-bottom: 1rem;
    }

    .navbar-right {
        display: none;
    }

    .navbar-right.active {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 0;
        background-color: #2c3e50;
        width: 100%;
        text-align: center;
        padding: 1rem 0;
    }

    .menu-toggle {
        display: block;
        color: white;
        cursor: pointer;
    }
}