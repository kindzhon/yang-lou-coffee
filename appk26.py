
html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>洋语楼咖啡 | Yangyulou Coffee</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        :root {
            --cream: #FAF6F0;
            --warm-white: #FDFBF7;
            --latte: #D4C5B0;
            --coffee: #8B6914;
            --espresso: #3D2B1F;
            --rose: #C9A9A6;
            --soft-brown: #A0826D;
            --sage: #B5C4A8;
            --text-dark: #2C2416;
            --text-light: #6B5B4F;
            --gold: #C8A96E;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Noto Sans SC', sans-serif;
            background-color: var(--cream);
            color: var(--text-dark);
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        /* ===== NAVIGATION ===== */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            padding: 20px 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.5s ease;
            background: transparent;
        }

        nav.scrolled {
            background: rgba(250, 246, 240, 0.92);
            backdrop-filter: blur(20px);
            padding: 15px 60px;
            box-shadow: 0 2px 30px rgba(44, 36, 22, 0.08);
        }

        .logo {
            font-family: 'Noto Serif SC', serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--espresso);
            letter-spacing: 4px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo-icon {
            width: 36px;
            height: 36px;
            background: var(--espresso);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--cream);
            font-size: 0.9rem;
        }

        .nav-links {
            display: flex;
            gap: 40px;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-dark);
            font-size: 0.95rem;
            font-weight: 400;
            letter-spacing: 1px;
            position: relative;
            padding: 5px 0;
            transition: color 0.3s;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 1.5px;
            background: var(--coffee);
            transition: width 0.4s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-links a:hover {
            color: var(--coffee);
        }

        .nav-icons {
            display: flex;
            gap: 20px;
            align-items: center;
        }

        .nav-icons i {
            font-size: 1.1rem;
            color: var(--text-dark);
            cursor: pointer;
            transition: color 0.3s, transform 0.3s;
        }

        .nav-icons i:hover {
            color: var(--coffee);
            transform: scale(1.1);
        }

        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: var(--coffee);
            color: white;
            font-size: 0.65rem;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
        }

        .cart-icon-wrap {
            position: relative;
        }

        /* ===== HERO SECTION ===== */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            background: var(--cream);
        }

        .hero-bg-pattern {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.04;
            background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%233D2B1F' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        }

        .hero-content {
            text-align: center;
            z-index: 2;
            max-width: 800px;
            padding: 0 40px;
        }

        .hero-subtitle {
            font-family: 'Noto Serif SC', serif;
            font-size: 1rem;
            color: var(--soft-brown);
            letter-spacing: 6px;
            margin-bottom: 20px;
            opacity: 0;
            animation: fadeInUp 1s ease 0.3s forwards;
        }

        .hero-title {
            font-family: 'Noto Serif SC', serif;
            font-size: 4.5rem;
            font-weight: 700;
            color: var(--espresso);
            line-height: 1.2;
            margin-bottom: 25px;
            opacity: 0;
            animation: fadeInUp 1s ease 0.6s forwards;
        }

        .hero-title span {
            display: block;
            font-size: 1.8rem;
            font-weight: 300;
            color: var(--soft-brown);
            margin-top: 10px;
            letter-spacing: 8px;
        }

        .hero-desc {
            font-size: 1.1rem;
            color: var(--text-light);
            line-height: 1.8;
            margin-bottom: 40px;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
            opacity: 0;
            animation: fadeInUp 1s ease 0.9s forwards;
        }

        .hero-cta {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            padding: 16px 40px;
            background: var(--espresso);
            color: var(--cream);
            text-decoration: none;
            font-size: 0.95rem;
            letter-spacing: 2px;
            border-radius: 50px;
            transition: all 0.4s ease;
            opacity: 0;
            animation: fadeInUp 1s ease 1.2s forwards;
            border: 2px solid var(--espresso);
        }

        .hero-cta:hover {
            background: transparent;
            color: var(--espresso);
            transform: translateY(-3px);
            box-shadow: 0 10px 40px rgba(61, 43, 31, 0.15);
        }

        .hero-visual {
            position: absolute;
            right: 5%;
            top: 50%;
            transform: translateY(-50%);
            width: 400px;
            height: 500px;
            opacity: 0;
            animation: fadeIn 1.5s ease 1s forwards;
        }

        .hero-visual img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 200px 200px 20px 20px;
            box-shadow: 0 30px 60px rgba(61, 43, 31, 0.15);
        }

        .floating-element {
            position: absolute;
            border-radius: 50%;
            opacity: 0.6;
            animation: float 6s ease-in-out infinite;
        }

        .float-1 {
            width: 80px;
            height: 80px;
            background: var(--latte);
            top: 15%;
            left: 10%;
            animation-delay: 0s;
        }

        .float-2 {
            width: 120px;
            height: 120px;
            background: var(--rose);
            bottom: 20%;
            left: 15%;
            animation-delay: 2s;
            opacity: 0.3;
        }

        .float-3 {
            width: 60px;
            height: 60px;
            background: var(--sage);
            top: 60%;
            right: 8%;
            animation-delay: 4s;
            opacity: 0.4;
        }

        /* ===== SECTION COMMON ===== */
        section {
            padding: 100px 60px;
            position: relative;
        }

        .section-header {
            text-align: center;
            margin-bottom: 70px;
        }

        .section-tag {
            font-family: 'Noto Serif SC', serif;
            font-size: 0.85rem;
            color: var(--coffee);
            letter-spacing: 4px;
            margin-bottom: 15px;
            display: block;
        }

        .section-title {
            font-family: 'Noto Serif SC', serif;
            font-size: 2.8rem;
            font-weight: 600;
            color: var(--espresso);
            margin-bottom: 15px;
        }

        .section-desc {
            color: var(--text-light);
            font-size: 1rem;
            max-width: 500px;
            margin: 0 auto;
            line-height: 1.7;
        }

        /* ===== ABOUT SECTION ===== */
        .about {
            background: var(--warm-white);
            display: flex;
            align-items: center;
            gap: 80px;
            padding: 120px 80px;
        }

        .about-image {
            flex: 1;
            position: relative;
        }

        .about-image img {
            width: 100%;
            max-width: 500px;
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(61, 43, 31, 0.1);
        }

        .about-image::before {
            content: '';
            position: absolute;
            top: -20px;
            left: -20px;
            width: 100%;
            max-width: 500px;
            height: 100%;
            border: 2px solid var(--latte);
            border-radius: 20px;
            z-index: -1;
        }

        .about-content {
            flex: 1;
        }

        .about-content h2 {
            font-family: 'Noto Serif SC', serif;
            font-size: 2.2rem;
            color: var(--espresso);
            margin-bottom: 25px;
            line-height: 1.3;
        }

        .about-content p {
            color: var(--text-light);
            line-height: 1.9;
            margin-bottom: 20px;
            font-size: 1rem;
        }

        .about-stats {
            display: flex;
            gap: 40px;
            margin-top: 40px;
        }

        .stat-item h3 {
            font-family: 'Noto Serif SC', serif;
            font-size: 2.5rem;
            color: var(--coffee);
            margin-bottom: 5px;
        }

        .stat-item p {
            font-size: 0.85rem;
            color: var(--text-light);
            letter-spacing: 1px;
        }

        /* ===== PRODUCTS SECTION ===== */
        .products {
            background: var(--cream);
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            max-width: 1300px;
            margin: 0 auto;
        }

        .product-card {
            background: var(--warm-white);
            border-radius: 24px;
            overflow: hidden;
            transition: all 0.5s ease;
            position: relative;
            box-shadow: 0 5px 25px rgba(61, 43, 31, 0.06);
        }

        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 50px rgba(61, 43, 31, 0.12);
        }

        .product-image {
            height: 320px;
            overflow: hidden;
            position: relative;
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s ease;
        }

        .product-card:hover .product-image img {
            transform: scale(1.08);
        }

        .product-tag {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(255, 255, 255, 0.9);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.75rem;
            color: var(--coffee);
            letter-spacing: 1px;
            backdrop-filter: blur(10px);
        }

        .product-info {
            padding: 30px;
        }

        .product-info h3 {
            font-family: 'Noto Serif SC', serif;
            font-size: 1.3rem;
            color: var(--espresso);
            margin-bottom: 8px;
        }

        .product-info .origin {
            font-size: 0.85rem;
            color: var(--soft-brown);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .product-info .description {
            font-size: 0.9rem;
            color: var(--text-light);
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .product-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .price {
            font-family: 'Noto Serif SC', serif;
            font-size: 1.4rem;
            color: var(--coffee);
            font-weight: 600;
        }

        .price span {
            font-size: 0.85rem;
            color: var(--text-light);
            font-weight: 400;
        }

        .add-to-cart {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: var(--espresso);
            color: var(--cream);
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .add-to-cart:hover {
            background: var(--coffee);
            transform: scale(1.1);
        }

        /* ===== FEATURES / PROCESS SECTION ===== */
        .process {
            background: var(--warm-white);
            padding: 120px 60px;
        }

        .process-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .process-card {
            text-align: center;
            padding: 40px 25px;
            background: var(--cream);
            border-radius: 20px;
            transition: all 0.4s ease;
        }

        .process-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(61, 43, 31, 0.08);
        }

        .process-icon {
            width: 70px;
            height: 70px;
            background: var(--latte);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 25px;
            font-size: 1.5rem;
            color: var(--espresso);
        }

        .process-card h3 {
            font-family: 'Noto Serif SC', serif;
            font-size: 1.2rem;
            color: var(--espresso);
            margin-bottom: 12px;
        }

        .process-card p {
            font-size: 0.9rem;
            color: var(--text-light);
            line-height: 1.6;
        }

        /* ===== GALLERY / AESTHETIC SECTION ===== */
        .gallery {
            padding: 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            min-height: 600px;
        }

        .gallery-image {
            overflow: hidden;
        }

        .gallery-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.8s ease;
        }

        .gallery-image:hover img {
            transform: scale(1.05);
        }

        .gallery-text {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 80px;
            background: var(--espresso);
            color: var(--cream);
        }

        .gallery-text .section-tag {
            color: var(--latte);
        }

        .gallery-text h2 {
            font-family: 'Noto Serif SC', serif;
            font-size: 2.5rem;
            margin-bottom: 25px;
            line-height: 1.3;
        }

        .gallery-text p {
            color: var(--latte);
            line-height: 1.9;
            margin-bottom: 20px;
            font-size: 1rem;
        }

        .gallery-text .cta-link {
            color: var(--cream);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-top: 20px;
            font-size: 0.95rem;
            letter-spacing: 1px;
            transition: gap 0.3s;
        }

        .gallery-text .cta-link:hover {
            gap: 18px;
        }

        /* ===== TESTIMONIALS ===== */
        .testimonials {
            background: var(--cream);
            padding: 120px 60px;
        }

        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .testimonial-card {
            background: var(--warm-white);
            padding: 40px;
            border-radius: 24px;
            position: relative;
            box-shadow: 0 5px 25px rgba(61, 43, 31, 0.05);
        }

        .testimonial-card::before {
            content: '"';
            font-family: 'Noto Serif SC', serif;
            font-size: 5rem;
            color: var(--latte);
            position: absolute;
            top: 10px;
            left: 25px;
            line-height: 1;
            opacity: 0.5;
        }

        .testimonial-text {
            font-size: 1rem;
            color: var(--text-light);
            line-height: 1.8;
            margin-bottom: 25px;
            position: relative;
            z-index: 1;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .author-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: var(--latte);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Noto Serif SC', serif;
            color: var(--espresso);
            font-weight: 600;
        }

        .author-info h4 {
            font-size: 1rem;
            color: var(--espresso);
            margin-bottom: 3px;
        }

        .author-info p {
            font-size: 0.8rem;
            color: var(--soft-brown);
        }

        /* ===== NEWSLETTER / CTA ===== */
        .newsletter {
            background: var(--espresso);
            padding: 100px 60px;
            text-align: center;
            color: var(--cream);
        }

        .newsletter h2 {
            font-family: 'Noto Serif SC', serif;
            font-size: 2.5rem;
            margin-bottom: 15px;
        }

        .newsletter p {
            color: var(--latte);
            margin-bottom: 40px;
            font-size: 1rem;
        }

        .newsletter-form {
            display: flex;
            gap: 15px;
            justify-content: center;
            max-width: 500px;
            margin: 0 auto;
        }

        .newsletter-form input {
            flex: 1;
            padding: 16px 25px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            background: rgba(255, 255, 255, 0.08);
            color: var(--cream);
            font-size: 0.95rem;
            outline: none;
            transition: all 0.3s;
        }

        .newsletter-form input::placeholder {
            color: var(--latte);
        }

        .newsletter-form input:focus {
            border-color: var(--gold);
            background: rgba(255, 255, 255, 0.12);
        }

        .newsletter-form button {
            padding: 16px 35px;
            background: var(--cream);
            color: var(--espresso);
            border: none;
            border-radius: 50px;
            font-size: 0.9rem;
            letter-spacing: 1px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 500;
        }

        .newsletter-form button:hover {
            background: var(--gold);
            color: var(--cream);
        }

        /* ===== FOOTER ===== */
        footer {
            background: #1a120e;
            color: var(--latte);
            padding: 80px 60px 40px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 60px;
            max-width: 1300px;
            margin: 0 auto 60px;
        }

        .footer-brand .logo {
            color: var(--cream);
            margin-bottom: 20px;
        }

        .footer-brand p {
            line-height: 1.8;
            font-size: 0.9rem;
            color: var(--soft-brown);
            max-width: 300px;
        }

        .footer-col h4 {
            color: var(--cream);
            font-size: 0.95rem;
            margin-bottom: 25px;
            letter-spacing: 2px;
            font-weight: 500;
        }

        .footer-col ul {
            list-style: none;
        }

        .footer-col ul li {
            margin-bottom: 12px;
        }

        .footer-col ul li a {
            color: var(--soft-brown);
            text-decoration: none;
            font-size: 0.9rem;
            transition: color 0.3s;
        }

        .footer-col ul li a:hover {
            color: var(--cream);
        }

        .social-links {
            display: flex;
            gap: 15px;
            margin-top: 25px;
        }

        .social-links a {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--latte);
            transition: all 0.3s;
        }

        .social-links a:hover {
            background: var(--coffee);
            color: var(--cream);
            transform: translateY(-3px);
        }

        .footer-bottom {
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 30px;
            text-align: center;
            font-size: 0.85rem;
            color: var(--soft-brown);
        }

        /* ===== CART SIDEBAR ===== */
        .cart-sidebar {
            position: fixed;
            top: 0;
            right: -450px;
            width: 450px;
            height: 100vh;
            background: var(--warm-white);
            z-index: 2000;
            box-shadow: -10px 0 50px rgba(0, 0, 0, 0.1);
            transition: right 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
        }

        .cart-sidebar.open {
            right: 0;
        }

        .cart-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4);
            z-index: 1999;
            opacity: 0;
            visibility: hidden;
            transition: all 0.4s;
        }

        .cart-overlay.open {
            opacity: 1;
            visibility: visible;
        }

        .cart-header {
            padding: 30px;
            border-bottom: 1px solid var(--latte);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .cart-header h3 {
            font-family: 'Noto Serif SC', serif;
            font-size: 1.3rem;
            color: var(--espresso);
        }

        .close-cart {
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--text-light);
            cursor: pointer;
            transition: color 0.3s;
        }

        .close-cart:hover {
            color: var(--espresso);
        }

        .cart-items {
            flex: 1;
            overflow-y: auto;
            padding: 20px 30px;
        }

        .cart-item {
            display: flex;
            gap: 15px;
            padding: 15px 0;
            border-bottom: 1px solid rgba(212, 197, 176, 0.3);
        }

        .cart-item img {
            width: 70px;
            height: 70px;
            object-fit: cover;
            border-radius: 12px;
        }

        .cart-item-info {
            flex: 1;
        }

        .cart-item-info h4 {
            font-size: 0.95rem;
            color: var(--espresso);
            margin-bottom: 4px;
        }

        .cart-item-info p {
            font-size: 0.8rem;
            color: var(--soft-brown);
            margin-bottom: 8px;
        }

        .cart-item-qty {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .qty-btn {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            border: 1px solid var(--latte);
            background: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-light);
            transition: all 0.3s;
        }

        .qty-btn:hover {
            background: var(--espresso);
            color: var(--cream);
            border-color: var(--espresso);
        }

        .cart-item-price {
            font-family: 'Noto Serif SC', serif;
            color: var(--coffee);
            font-weight: 600;
        }

        .remove-item {
            background: none;
            border: none;
            color: var(--rose);
            cursor: pointer;
            font-size: 0.85rem;
            transition: color 0.3s;
        }

        .remove-item:hover {
            color: #a05050;
        }

        .cart-footer {
            padding: 25px 30px;
            border-top: 1px solid var(--latte);
            background: var(--cream);
        }

        .cart-total {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            font-size: 1.1rem;
        }

        .cart-total span:first-child {
            color: var(--text-light);
        }

        .cart-total span:last-child {
            font-family: 'Noto Serif SC', serif;
            font-size: 1.4rem;
            color: var(--espresso);
            font-weight: 600;
        }

        .checkout-btn {
            width: 100%;
            padding: 16px;
            background: var(--espresso);
            color: var(--cream);
            border: none;
            border-radius: 50px;
            font-size: 1rem;
            letter-spacing: 2px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .checkout-btn:hover {
            background: var(--coffee);
        }

        .empty-cart {
            text-align: center;
            padding: 60px 20px;
            color: var(--text-light);
        }

        .empty-cart i {
            font-size: 3rem;
            color: var(--latte);
            margin-bottom: 20px;
            display: block;
        }

        /* ===== TOAST NOTIFICATION ===== */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: var(--espresso);
            color: var(--cream);
            padding: 14px 30px;
            border-radius: 50px;
            font-size: 0.9rem;
            z-index: 3000;
            opacity: 0;
            transition: all 0.4s ease;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 10px 40px rgba(61, 43, 31, 0.2);
        }

        .toast.show {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }

        /* ===== ANIMATIONS ===== */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        /* ===== SCROLL REVEAL ===== */
        .reveal {
            opacity: 0;
            transform: translateY(50px);
            transition: all 0.8s ease;
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 1024px) {
            .hero-visual { display: none; }
            .about { flex-direction: column; padding: 80px 40px; }
            .process-grid { grid-template-columns: repeat(2, 1fr); }
            .gallery { grid-template-columns: 1fr; }
            .testimonial-grid { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr 1fr; }
        }

        @media (max-width: 768px) {
            nav { padding: 15px 25px; }
            nav.scrolled { padding: 12px 25px; }
            .nav-links { display: none; }
            .hero-title { font-size: 2.8rem; }
            section { padding: 60px 25px; }
            .process-grid { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr; gap: 40px; }
            .cart-sidebar { width: 100%; right: -100%; }
            .about-stats { flex-direction: column; gap: 20px; }
        }
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav id="navbar">
        <div class="logo">
            <div class="logo-icon"><i class="fas fa-coffee"></i></div>
            洋语楼咖啡
        </div>
        <ul class="nav-links">
            <li><a href="#home">首页</a></li>
            <li><a href="#about">品牌故事</a></li>
            <li><a href="#products">精选咖啡</a></li>
            <li><a href="#process">烘焙工艺</a></li>
            <li><a href="#contact">联系我们</a></li>
        </ul>
        <div class="nav-icons">
            <i class="fas fa-search"></i>
            <div class="cart-icon-wrap" onclick="toggleCart()">
                <i class="fas fa-shopping-bag"></i>
                <span class="cart-count" id="cartCount">0</span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-bg-pattern"></div>
        <div class="floating-element float-1"></div>
        <div class="floating-element float-2"></div>
        <div class="floating-element float-3"></div>
        
        <div class="hero-content">
            <p class="hero-subtitle">SINCE 2018 · 精品咖啡</p>
            <h1 class="hero-title">
                洋语楼咖啡
                <span>YANGYULOU COFFEE</span>
            </h1>
            <p class="hero-desc">
                从世界咖啡产区甄选每一颗咖啡豆，以花艺美学诠释咖啡文化，让每一杯咖啡都成为生活中的艺术品。
            </p>
            <a href="#products" class="hero-cta">
                探索风味 <i class="fas fa-arrow-right"></i>
            </a>
        </div>

        <div class="hero-visual">
            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800&q=80" alt="Coffee Art">
        </div>
    </section>

    <!-- About Section -->
    <section class="about" id="about">
        <div class="about-image reveal">
            <img src="https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800&q=80" alt="Coffee Beans">
        </div>
        <div class="about-content reveal">
            <span class="section-tag">品牌故事</span>
            <h2>以花为媒，<br>以咖会友</h2>
            <p>
                洋语楼咖啡诞生于对精品咖啡的执着追求。我们相信，一杯好咖啡不仅是味蕾的享受，更是一种生活态度的表达。
            </p>
            <p>
                我们将花艺美学融入咖啡文化，在每一款产品中注入自然的灵感与艺术的温度。从埃塞俄比亚的耶加雪菲到哥伦比亚的慧兰，我们走遍世界咖啡产区，只为找到那一颗完美的咖啡豆。
            </p>
            <div class="about-stats">
                <div class="stat-item">
                    <h3>12+</h3>
                    <p>合作产区</p>
                </div>
                <div class="stat-item">
                    <h3>50K+</h3>
                    <p>忠实顾客</p>
                </div>
                <div class="stat-item">
                    <h3>6</h3>
                    <p>年匠心沉淀</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Products Section -->
    <section class="products" id="products">
        <div class="section-header reveal">
            <span class="section-tag">精选咖啡</span>
            <h2 class="section-title">当季风味</h2>
            <p class="section-desc">从世界各地精选的咖啡豆，每一款都有独特的风味故事</p>
        </div>

        <div class="products-grid">
            <div class="product-card reveal">
                <div class="product-image">
                    <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=600&q=80" alt="耶加雪菲">
                    <span class="product-tag">手冲推荐</span>
                </div>
                <div class="product-info">
                    <h3>耶加雪菲 · 花香</h3>
                    <p class="origin"><i class="fas fa-map-marker-alt"></i> 埃塞俄比亚 · 耶加雪菲产区</p>
                    <p class="description">明亮的柑橘酸质，伴随茉莉花香与蜂蜜甜感，口感轻盈优雅。</p>
                    <div class="product-footer">
                        <div class="price">¥128 <span>/ 227g</span></div>
                        <button class="add-to-cart" onclick="addToCart('耶加雪菲 · 花香', 128, 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=200&q=80')">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>

            <div class="product-card reveal">
                <div class="product-image">
                    <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&q=80" alt="瑰夏">
                    <span class="product-tag">限量臻选</span>
                </div>
                <div class="product-info">
                    <h3>巴拿马 · 瑰夏</h3>
                    <p class="origin"><i class="fas fa-map-marker-alt"></i> 巴拿马 · 翡翠庄园</p>
                    <p class="description">浓郁的玫瑰花香，热带水果风味，丝滑如绸的body，咖啡中的香槟。</p>
                    <div class="product-footer">
                        <div class="price">¥368 <span>/ 100g</span></div>
                        <button class="add-to-cart" onclick="addToCart('巴拿马 · 瑰夏', 368, 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=200&q=80')">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>

            <div class="product-card reveal">
                <div class="product-image">
                    <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=600&q=80" alt="曼特宁">
                    <span class="product-tag">经典深烘</span>
                </div>
                <div class="product-info">
                    <h3>苏门答腊 · 曼特宁</h3>
                    <p class="origin"><i class="fas fa-map-marker-alt"></i> 印度尼西亚 · 苏门答腊</p>
                    <p class="description">醇厚的草本香气，黑巧克力与烟熏风味，低酸度，回甘持久。</p>
                    <div class="product-footer">
                        <div class="price">¥98 <span>/ 227g</span></div>
                        <button class="add-to-cart" onclick="addToCart('苏门答腊 · 曼特宁', 98, 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=200&q=80')">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>

            <div class="product-card reveal">
                <div class="product-image">
                    <img src="https://images.unsplash.com/photo-1611854779393-1b2da9d400fe?w=600&q=80" alt="哥伦比亚">
                    <span class="product-tag">均衡之选</span>
                </div>
                <div class="product-info">
                    <h3>哥伦比亚 · 慧兰</h3>
                    <p class="origin"><i class="fas fa-map-marker-alt"></i> 哥伦比亚 · 慧兰省</p>
                    <p class="description">焦糖甜感，红苹果与坚果香气，酸苦平衡，适合日常饮用。</p>
                    <div class="product-footer">
                        <div class="price">¥108 <span>/ 227g</span></div>
                        <button class="add-to-cart" onclick="addToCart('哥伦比亚 · 慧兰', 108, 'https://images.unsplash.com/photo-1611854779393-1b2da9d400fe?w=200&q=80')">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>

            <div class="product-card reveal">
                <div class="product-image">
                    <img src="https://images.unsplash.com/photo-1587734195503-904fca47e0e9?w=600&q=80" alt="肯尼亚">
                    <span class="product-tag">果酸突出</span>
                </div>
                <div class="product-info">
                    <h3>肯尼亚 · AA TOP</h3>
                    <p class="origin"><i class="fas fa-map-marker-alt"></i> 肯尼亚 · 涅里产区</p>
                    <p class="description">强烈的黑醋栗与番茄酸质，红酒般的醇厚body，层次丰富。</p>
                    <div class="product-footer">
                        <div class="price">¥138 <span>/ 227g</span></div>
                        <button class="add-to-cart" onclick="addToCart('肯尼亚 · AA TOP', 138, 'https://images.unsplash.com/photo-1587734195503-904fca47e0e9?w=200&q=80')">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>

            <div class="product-card reveal">
                <div class="product-image">
                    <img src="https://images.unsplash.com/photo-1498804103079-a6351b050096?w=600&q=80" alt="云南">
                    <span class="product-tag">国产精品</span>
                </div>
                <div class="product-info">
                    <h3>云南 · 普洱日晒</h3>
                    <p class="origin"><i class="fas fa-map-marker-alt"></i> 中国 · 云南普洱</p>
                    <p class="description">热带水果与红酒发酵香气，甜感饱满，展现中国咖啡的独特魅力。</p>
                    <div class="product-footer">
                        <div class="price">¥88 <span>/ 227g</span></div>
                        <button class="add-to-cart" onclick="addToCart('云南 · 普洱日晒', 88, 'https://images.unsplash.com/photo-1498804103079-a6351b050096?w=200&q=80')">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="process" id="process">
        <div class="section-header reveal">
            <span class="section-tag">烘焙工艺</span>
            <h2 class="section-title">从种子到杯子</h2>
            <p class="section-desc">每一个环节都倾注匠心，只为呈现最完美的风味</p>
        </div>

        <div class="process-grid">
            <div class="process-card reveal">
                <div class="process-icon"><i class="fas fa-seedling"></i></div>
                <h3>严选产地</h3>
                <p>深入全球12个精品咖啡产区，与当地农户建立长期合作，确保每一颗咖啡豆的品质。</p>
            </div>
            <div class="process-card reveal">
                <div class="process-icon"><i class="fas fa-fire"></i></div>
                <h3>匠心烘焙</h3>
                <p>采用德国Probat烘焙机，根据每款豆子的特性定制烘焙曲线，精准把控每一秒。</p>
            </div>
            <div class="process-card reveal">
                <div class="process-icon"><i class="fas fa-flask"></i></div>
                <h3>品质检测</h3>
                <p>每一批咖啡豆都经过SCA认证杯测师的专业评测，确保风味稳定、品质如一。</p>
            </div>
            <div class="process-card reveal">
                <div class="process-icon"><i class="fas fa-truck"></i></div>
                <h3>新鲜送达</h3>
                <p>下单后48小时内新鲜烘焙并发货，采用单向排气阀包装，锁住最佳赏味期。</p>
            </div>
        </div>
    </section>

    <!-- Gallery Section -->
    <section class="gallery">
        <div class="gallery-image reveal">
            <img src="https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800&q=80" alt="Coffee Shop">
        </div>
        <div class="gallery-text reveal">
            <span class="section-tag">空间美学</span>
            <h2>咖啡与花的<br>诗意邂逅</h2>
            <p>
                洋语楼咖啡空间以自然花艺为设计灵感，将咖啡的醇厚与花朵的柔美完美融合。在这里，您可以品味一杯精心冲煮的咖啡，同时感受花艺带来的宁静与美好。
            </p>
            <p>
                我们定期举办咖啡品鉴会与花艺工作坊，邀请您一同探索咖啡与自然的无限可能。
            </p>
            <a href="#" class="cta-link">
                预约体验 <i class="fas fa-arrow-right"></i>
            </a>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials">
        <div class="section-header reveal">
            <span class="section-tag">顾客心声</span>
            <h2 class="section-title">他们这样说</h2>
        </div>

        <div class="testimonial-grid">
            <div class="testimonial-card reveal">
                <p class="testimonial-text">
                    洋语楼的耶加雪菲是我喝过最干净的手冲，花香非常突出，每次冲泡都是一种享受。包装也非常精美，送朋友很有面子。
                </p>
                <div class="testimonial-author">
                    <div class="author-avatar">林</div>
                    <div class="author-info">
                        <h4>林小姐</h4>
                        <p>资深咖啡爱好者</p>
                    </div>
                </div>
            </div>

            <div class="testimonial-card reveal">
                <p class="testimonial-text">
                    作为一个每天靠咖啡续命的上班族，洋语楼的豆子让我重新认识了什么是好咖啡。特别是云南普洱日晒，甜感惊人！
                </p>
                <div class="testimonial-author">
                    <div class="author-avatar">张</div>
                    <div class="author-info">
                        <h4>张先生</h4>
                        <p>设计师 · 上海</p>
                    </div>
                </div>
            </div>

            <div class="testimonial-card reveal">
                <p class="testimonial-text">
                    店里的花艺布置太美了，每次去都像走进了一个小型艺术展。咖啡和花的结合真的很有创意，强烈推荐大家去体验一下。
                </p>
                <div class="testimonial-author">
                    <div class="author-avatar">王</div>
                    <div class="author-info">
                        <h4>王女士</h4>
                        <p>花艺师 · 北京</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Newsletter -->
    <section class="newsletter" id="contact">
        <div class="reveal">
            <h2>订阅风味资讯</h2>
            <p>第一时间获取新品上市、限时优惠与咖啡知识分享</p>
            <form class="newsletter-form" onsubmit="event.preventDefault(); showToast('订阅成功！感谢您的关注');">
                <input type="email" placeholder="请输入您的邮箱地址" required>
                <button type="submit">立即订阅</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-grid">
            <div class="footer-brand">
                <div class="logo">
                    <div class="logo-icon"><i class="fas fa-coffee"></i></div>
                    洋语楼咖啡
                </div>
                <p>
                    以花为媒，以咖会友。我们致力于将世界精品咖啡与花艺美学带给每一位热爱生活的人。
                </p>
                <div class="social-links">
                    <a href="#"><i class="fab fa-weixin"></i></a>
                    <a href="#"><i class="fab fa-weibo"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-xiaohongshu"></i></a>
                </div>
            </div>

            <div class="footer-col">
                <h4>产品系列</h4>
                <ul>
                    <li><a href="#">单品手冲</a></li>
                    <li><a href="#">意式拼配</a></li>
                    <li><a href="#">挂耳咖啡</a></li>
                    <li><a href="#">咖啡器具</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>关于我们</h4>
                <ul>
                    <li><a href="#">品牌故事</a></li>
                    <li><a href="#">烘焙工坊</a></li>
                    <li><a href="#">线下门店</a></li>
                    <li><a href="#">加入我们</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>客户服务</h4>
                <ul>
                    <li><a href="#">配送说明</a></li>
                    <li><a href="#">退换政策</a></li>
                    <li><a href="#">常见问题</a></li>
                    <li><a href="#">联系客服</a></li>
                </ul>
            </div>
        </div>

        <div class="footer-bottom">
            <p> 洋语楼咖啡 Yangyulou Coffee. All rights reserved. 用心烘焙每一颗咖啡豆。</p>
        </div>
    </footer>

    <!-- Cart Sidebar -->
    <div class="cart-overlay" id="cartOverlay" onclick="toggleCart()"></div>
    <div class="cart-sidebar" id="cartSidebar">
        <div class="cart-header">
            <h3>购物车</h3>
            <button class="close-cart" onclick="toggleCart()"><i class="fas fa-times"></i></button>
        </div>
        <div class="cart-items" id="cartItems">
            <div class="empty-cart">
                <i class="fas fa-shopping-bag"></i>
                <p>购物车是空的</p>
            </div>
        </div>
        <div class="cart-footer" id="cartFooter" style="display: none;">
            <div class="cart-total">
                <span>合计</span>
                <span id="cartTotal">¥0</span>
            </div>
            <button class="checkout-btn" onclick="showToast('功能开发中，敬请期待！')">去结算</button>
        </div>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast">
        <i class="fas fa-check-circle"></i>
        <span id="toastMsg">已添加到购物车</span>
    </div>

    <script>
        // Navbar scroll effect
        window.addEventListener('scroll', () => {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Scroll reveal
        const revealElements = document.querySelectorAll('.reveal');
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, { threshold: 0.1 });

        revealElements.forEach(el => revealObserver.observe(el));

        // Cart functionality
        let cart = [];

        function addToCart(name, price, image) {
            const existing = cart.find(item => item.name === name);
            if (existing) {
                existing.qty++;
            } else {
                cart.push({ name, price, image, qty: 1 });
            }
            updateCart();
            showToast(`${name} 已添加到购物车`);
        }

        function removeFromCart(index) {
            cart.splice(index, 1);
            updateCart();
        }

        function updateQty(index, delta) {
            cart[index].qty += delta;
            if (cart[index].qty <= 0) {
                cart.splice(index, 1);
            }
            updateCart();
        }

        function updateCart() {
            const cartItems = document.getElementById('cartItems');
            const cartCount = document.getElementById('cartCount');
            const cartFooter = document.getElementById('cartFooter');
            const cartTotal = document.getElementById('cartTotal');

            const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);
            cartCount.textContent = totalQty;

            if (cart.length === 0) {
                cartItems.innerHTML = `
                    <div class="empty-cart">
                        <i class="fas fa-shopping-bag"></i>
                        <p>购物车是空的</p>
                    </div>
                `;
                cartFooter.style.display = 'none';
            } else {
                cartItems.innerHTML = cart.map((item, index) => `
                    <div class="cart-item">
                        <img src="${item.image}" alt="${item.name}">
                        <div class="cart-item-info">
                            <h4>${item.name}</h4>
                            <p>¥${item.price}</p>
                            <div class="cart-item-qty">
                                <button class="qty-btn" onclick="updateQty(${index}, -1)">-</button>
                                <span>${item.qty}</span>
                                <button class="qty-btn" onclick="updateQty(${index}, 1)">+</button>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div class="cart-item-price">¥${item.price * item.qty}</div>
                            <button class="remove-item" onclick="removeFromCart(${index})">删除</button>
                        </div>
                    </div>
                `).join('');
                cartFooter.style.display = 'block';
                const total = cart.reduce((sum, item) => sum + item.price * item.qty, 0);
                cartTotal.textContent = `¥${total}`;
            }
        }

        function toggleCart() {
            document.getElementById('cartSidebar').classList.toggle('open');
            document.getElementById('cartOverlay').classList.toggle('open');
            document.body.style.overflow = document.getElementById('cartSidebar').classList.contains('open') ? 'hidden' : '';
        }

        // Toast
        function showToast(msg) {
            const toast = document.getElementById('toast');
            document.getElementById('toastMsg').textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2500);
        }

        // Smooth scroll for nav links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>

</body>
</html>"""

# Save the HTML file
with open('/mnt/agents/output/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file saved successfully!")
print(f"File size: {len(html_content)} characters")
